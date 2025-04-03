import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pyautogui.size()

# Smooth movement parameters
smooth_factor = 8  # Increased for smoother motion
prev_x, prev_y = 0, 0

# Click cooldown
last_click_time = 0
click_cooldown = 0.3  # 300ms cooldown

# Capture video
cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip image horizontally for mirror effect
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get index finger and thumb tip positions
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Convert to screen coordinates
            x = int(index_finger_tip.x * screen_width)
            y = int(index_finger_tip.y * screen_height)

            # Apply moving average smoothing
            curr_x = (prev_x * (smooth_factor - 1) + x) / smooth_factor
            curr_y = (prev_y * (smooth_factor - 1) + y) / smooth_factor

            # Move the mouse smoothly
            pyautogui.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

            # Click detection (Thumb close to Index Finger)
            distance = np.hypot(thumb_tip.x - index_finger_tip.x, thumb_tip.y - index_finger_tip.y)
            current_time = time.time()

            if distance < 0.05 and (current_time - last_click_time) > click_cooldown:
                pyautogui.click()
                last_click_time = current_time  # Update click timestamp

    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()