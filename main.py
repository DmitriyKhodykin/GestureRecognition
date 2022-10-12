import asyncio

from gesture_recognition.gesture_recognition import main


if __name__ == "__main__":
    print("App starting on WebSocket on :8765...")
    asyncio.run(main())
