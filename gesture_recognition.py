"""Module for palm gesture recognition and sending gesture codes to WebSocket.

Mediapipe open source cross-platform, customizable ML solutions for live and streaming media. 
docs: https://google.github.io/mediapipe/solutions/hands.html

Broadcasting messages with websockets.
docs: https://websockets.readthedocs.io/en/stable/topics/broadcast.html
"""
import logging

logging.basicConfig(
    filename="back_test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

import asyncio
import json
import websockets

import cv2
import mediapipe as mp

from gesture_recognition.guesture_dict import gesture_dictionary
from gesture_recognition.hand_gestures import HandGestureRecognition
from gesture_recognition.transformers import ImageTransforming as IMT


CLIENTS = set()


async def handler(websocket):
    CLIENTS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CLIENTS.remove(websocket)
        logging.debug("Websocket was removed")


async def broadcast(message):
    for websocket in CLIENTS.copy():
        try:
            await websocket.send(message)
        except websockets.ConnectionClosed:
            logging.info("Websocket Connection Closed")


async def broadcast_messages():
    video_stream = cv2.VideoCapture(0)  # Or http://<ip>:<port>/video
    palm_detector = PalmDetection()

    with palm_detector.get_palm_ibject() as hands:

        while video_stream.isOpened():
            success, image = video_stream.read()
            if not success:
                logging.error("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            if cv2.waitKey(1) & 0xFF == ord('q'):
                logging.info("KeyboardInterrupt.")
                break

            # Change color before results to improve performance.
            try:
                IMT(image).change_color(cv2.COLOR_BGR2RGB)
                results = hands.process(image)
                IMT(image).change_color(cv2.COLOR_RGB2BGR)
            except Exception as error_message:
                logging.error(error_message)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Drawing palms landmarks.
                    palm_detector.drawing_palms(image, hand_landmarks)
                    
                    # Action recognition.
                    try:
                        gesture_recognition = HandGestureRecognition(hand_landmarks)
                        palm_gesture = gesture_recognition.gesture_to_action()
                        palm_gesture_code = gesture_dictionary[palm_gesture]
                    except Exception as error_message:
                        logging.error(error_message)

                    await asyncio.sleep(0)
                    message = palm_gesture_code  # Gesture recognition output
                    await broadcast(json.dumps({"gesture": message}))


async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await broadcast_messages()  # runs forever


class PalmDetection:
    
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

    def get_palm_ibject(
        self,
        complexity=0,
        detection_level=0.5,
        tracking_level=0.5,
        hands_count=2
    ):
        model = self.mp_hands.Hands(
            model_complexity = complexity,
            min_detection_confidence = detection_level,
            min_tracking_confidence = tracking_level,
            max_num_hands=hands_count
        )
        return model

    def drawing_palms(self, image, landmarks):
        
        drawed_landmarks = self.mp_drawing.draw_landmarks(
            image,
            landmarks,
            self.mp_hands.HAND_CONNECTIONS,
            self.mp_drawing_styles.get_default_hand_landmarks_style(),
            self.mp_drawing_styles.get_default_hand_connections_style()
        )
        return drawed_landmarks


if __name__ == "__main__":
    print("Run WebSocket on localhost:8765")
    asyncio.run(main())
