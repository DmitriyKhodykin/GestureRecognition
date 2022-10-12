from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmarkList


class HandGestureRecognition:
    """The class recognizes conditional sign language by landmarks 
    on the palm of a human's hand.
    """
    
    def __init__(self, landmarks_list: NormalizedLandmarkList):
        self.landmarks_list = landmarks_list

    def gesture_to_action(self):
        """Recognizes gestures by the landmarks and returns a gesture code.

            * 0 - base of palm,
            * 4 - thumb tip,
            * 8 - index finger tip,
            * 12 - middle finger tip,
            * 16 - ring finger tip,
            * 20 - pinky tip.
        [x, y, z] - axes of landmarks.
        Docs: https://google.github.io/mediapipe/solutions/hands.html
        """
        result: str = ''
        keypoints = self._get_keypoints()

        # X axes
        keypoint_0x = keypoints[0]['x']
        keypoint_4x = keypoints[4]['x']
        keypoint_6x = keypoints[6]['x']
        keypoint_7x = keypoints[7]['x']
        keypoint_8x = keypoints[8]['x']
        keypoint_10x = keypoints[10]['x']
        keypoint_11x = keypoints[11]['x']
        keypoint_12x = keypoints[12]['x']
        keypoint_14x = keypoints[14]['x']
        keypoint_15x = keypoints[15]['x']
        keypoint_16x = keypoints[16]['x']
        keypoint_17x = keypoints[17]['x'] 
        keypoint_18x = keypoints[18]['x'] 
        keypoint_19x = keypoints[19]['x']
        keypoint_20x = keypoints[20]['x']

        # Y axes
        keypoint_0y = keypoints[0]['y']
        keypoint_1y = keypoints[1]['y']
        keypoint_3y = keypoints[3]['y']
        keypoint_4y = keypoints[4]['y']
        keypoint_5y = keypoints[5]['y']
        keypoint_6y = keypoints[6]['y']
        keypoint_7y = keypoints[7]['y'] 
        keypoint_8y = keypoints[8]['y']
        keypoint_9y = keypoints[9]['y']
        keypoint_10y = keypoints[10]['y']
        keypoint_11y = keypoints[11]['y'] 
        keypoint_12y = keypoints[12]['y']
        keypoint_13y = keypoints[13]['y']
        keypoint_14y = keypoints[14]['y']
        keypoint_15y = keypoints[15]['y'] 
        keypoint_16y = keypoints[16]['y']
        keypoint_17y = keypoints[17]['y']
        keypoint_18y = keypoints[18]['y']
        keypoint_19y = keypoints[19]['y']
        keypoint_20y = keypoints[20]['y']

        # Z axes
        keypoint_4z = keypoints[4]['z']
        keypoint_5z = keypoints[5]['z']
        keypoint_7z = keypoints[7]['z']

        # 1 Thumbs Up Gesture
        if (
            keypoint_4y < keypoint_3y
            and keypoint_5y < keypoint_9y
            and keypoint_8x > keypoint_7x
            and keypoint_12x > keypoint_11x 
            and keypoint_16x > keypoint_15x 
            and keypoint_20x > keypoint_19x 
            and keypoint_8x < keypoint_0x 
            and keypoint_12x < keypoint_0x 
            and keypoint_16x < keypoint_0x 
            and keypoint_20x < keypoint_0x 
        ):
            result = 'thumbs Up'

        elif (
            keypoint_4y < keypoint_3y
            and keypoint_5y < keypoint_9y
            and keypoint_8x < keypoint_7x
            and keypoint_12x < keypoint_11x 
            and keypoint_16x < keypoint_15x 
            and keypoint_20x < keypoint_19x 
            and keypoint_8x > keypoint_0x
            and keypoint_12x > keypoint_0x 
            and keypoint_16x > keypoint_0x 
            and keypoint_20x > keypoint_0x 
        ):
            result = 'thumbs Up'

        # 2 Thumbs Down Gesture
        elif (
            keypoint_4y > keypoint_3y 
            and keypoint_8x > keypoint_6x
            and keypoint_12x > keypoint_10x
            and keypoint_16x > keypoint_14x
            and keypoint_20x > keypoint_18x
            and keypoint_8x < keypoint_0x
            and keypoint_12x < keypoint_0x
            and keypoint_16x < keypoint_0x
            and keypoint_20x < keypoint_0x
            and keypoint_5y > keypoint_9y
        ):
            result = 'thumbs Down'

        elif (
            keypoint_4y > keypoint_3y
            and keypoint_8x < keypoint_6x
            and keypoint_12x < keypoint_10x
            and keypoint_16x < keypoint_14x
            and keypoint_20x < keypoint_18x
            and keypoint_8x > keypoint_0x
            and keypoint_12x > keypoint_0x
            and keypoint_16x > keypoint_0x
            and keypoint_16x > keypoint_0x
            and keypoint_5y > keypoint_9y
        ):
            result = 'thumbs Down'

        # 3 Keep in touch Gesture
        elif (
            keypoint_4y < keypoint_1y
            and keypoint_8x > keypoint_7x
            and keypoint_12x > keypoint_11x 
            and keypoint_16x > keypoint_15x
            and keypoint_20x < keypoint_18x
            and keypoint_0x > keypoint_17x
            and keypoint_5z < keypoint_7z
        ):
            result = 'Keep in touch'

        elif (
            keypoint_4y < keypoint_1y
            and keypoint_8x < keypoint_7x
            and keypoint_12x < keypoint_11x
            and keypoint_16x < keypoint_15x
            and keypoint_20x > keypoint_18x
            and keypoint_0x < keypoint_17x
            and keypoint_5z < keypoint_7z
        ):
            result = 'Keep in touch'

        # 4 Unity Gesture
        elif (
            keypoint_8y < keypoint_6y
            and keypoint_20y < keypoint_18y
            and keypoint_12y > keypoint_10y
            and keypoint_16y > keypoint_14y
            and keypoint_0y > keypoint_1y
        ):
            result = 'Unity'

        # 5 F... Gesture
        elif (
            keypoint_12y < keypoint_10y
            and keypoint_8y > keypoint_6y
            and keypoint_16y > keypoint_14y
            and keypoint_20y > keypoint_18y
        ):
            result = 'Fk'

        # 6 Victory Gesture TODO: Add restrictions
        elif (
            keypoint_8y < keypoint_5y
            and keypoint_12y < keypoint_9y
            and keypoint_16y > keypoint_14y
            and keypoint_20y > keypoint_18y
        ):
            result = 'Victory'

        # 7 It's okay Gesture
        elif (
            keypoint_20x > keypoint_16x
            and keypoint_16x > keypoint_12x
            and keypoint_8y > keypoint_6y
            and keypoint_0y > keypoint_1y
            and keypoint_12y < keypoint_11y
            and keypoint_16y < keypoint_15y
            and keypoint_20y < keypoint_19y
        ):
            result = 'Its okay'

        elif (
            keypoint_20x < keypoint_16x
            and keypoint_16x < keypoint_12x
            and keypoint_8y > keypoint_6y
            and keypoint_0y > keypoint_1y
            and keypoint_12y < keypoint_11y
            and keypoint_16y < keypoint_15y
            and keypoint_20y < keypoint_19y
        ):
            result = 'Its okay'

        # 8 We Stand Together Gesture
        elif (
            keypoint_5y < keypoint_7y
            and keypoint_9y < keypoint_11y
            and keypoint_13y < keypoint_15y
            and keypoint_17y < keypoint_19y
            and keypoint_7y < keypoint_0y
            and keypoint_11y < keypoint_0y
            and keypoint_15y < keypoint_0y
            and keypoint_19y < keypoint_0y
            and keypoint_4x > keypoint_6x
            and keypoint_4z < keypoint_5z
        ):
            result = 'We stand together'

        elif (
            keypoint_5y < keypoint_7y 
            and keypoint_9y < keypoint_11y
            and keypoint_13y < keypoint_15y
            and keypoint_17y < keypoint_19y
            and keypoint_7y < keypoint_0y
            and keypoint_11y < keypoint_0y
            and keypoint_15y < keypoint_0y
            and keypoint_19y < keypoint_0y
            and keypoint_4x < keypoint_6x
            and keypoint_4z < keypoint_5z
        ):
            result = 'We stand together'

        # 9 Palm Gesture
        elif (
            keypoint_4y < keypoint_3y
            and keypoint_12y < keypoint_11y
            and keypoint_16y < keypoint_15y
            and keypoint_20y < keypoint_19y
        ):
            result = 'Palm'

        else:
            result = 'Gesture not recognized'

        return result

    def _get_keypoints(self):
        """Returns the coordinates of 21 points recognized on the palm in 3D.
        """
        keypoints = []
        
        for data_point in self.landmarks_list.landmark:
            keypoints.append({
                'x': data_point.x,
                'y': data_point.y,
                'z': data_point.z
            })

        return keypoints
