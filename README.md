# Virtual Mouse using Hand Tracking

## Overview
This project implements a **Virtual Mouse** using hand tracking and gesture recognition. It allows users to control the mouse cursor using their hand movements and perform clicks with gestures.

## Features
- **Hand Tracking:** Detects and tracks hand movements in real-time.
- **Cursor Control:** Moves the mouse cursor based on index finger position.
- **Click Detection:** Performs a mouse click when the thumb and index finger come close.
- **Smooth Movement:** Uses filtering to reduce jitter and make movements smoother.
- **No Additional Hardware:** Works with a standard webcam.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install opencv-python mediapipe numpy pyautogui
```

## How It Works
1. **Capture Video:** Uses OpenCV to capture video from the webcam.
2. **Hand Detection:** MediaPipe processes the frames to detect hands.
3. **Finger Tracking:** Extracts key points for the index finger and thumb.
4. **Cursor Movement:** Converts hand movement into screen coordinates.
5. **Click Detection:** Triggers clicks when the index finger and thumb touch.

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Use your index finger to move the cursor.
3. Bring your thumb and index finger together to click.
4. Press 'q' to exit.

## Issues & Improvements
- **Jittery Movement?** Adjust smoothing parameters.
- **High Sensitivity?** Modify the scaling factor.
- **Too Many Clicks?** Increase the click detection threshold.

## Future Enhancements
- Implement Kalman Filter for smoother tracking.
- Add gesture-based right-click and scrolling.
- Improve accuracy using OpenSeeFace.

## Credits
- **MediaPipe Hands** for hand tracking.
- **OpenCV** for video processing.
- **PyAutoGUI** for controlling the cursor.

### Made with ❤️ by Devansh Rajan

