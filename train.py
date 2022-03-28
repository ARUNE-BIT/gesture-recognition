# import necessary packages for hand gesture recognition project using Python OpenCV

import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils



# Initialize the webcam for Hand Gesture Recognition Python project
cap = cv2.VideoCapture(0)

while True:
  # Read each frame from the webcam
  _, frame = cap.read()
  x , y, c = frame.shape

  # Flip the frame vertically
  frame = cv2.flip(frame, 1)

  framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  # Get hand landmark prediction
  result = hands.process(framergb)

  className = ''

  # post process the result
  if result.multi_hand_landmarks:
      landmarks = []
      for handslms in result.multi_hand_landmarks:
          for lm in handslms.landmark:
              # print(id, lm)
              lmx = int(lm.x * x)
              lmy = int(lm.y * y)

              landmarks.append([lmx, lmy])

          # Drawing landmarks on frames
          mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)


  # Show the final output
  cv2.imshow("Output", frame)
  if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows()