"""
Author: Jayamadu Gammune

This script implements a Hole Centering Tool using computer vision techniques.
It detects circular shapes (holes) from a webcam feed and provides visual feedback
to align these holes with a crosshair displayed on the screen.

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
"""


import cv2
import mediapipe as mp

def track_hand_gesture(frame, hands):
    # Initialize the drawing utilities from mediapipe
    mp_drawing = mp.solutions.drawing_utils
    
    # Convert the frame to RGB color space
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame using the hands detection model
    results = hands.process(frame_rgb)
    
    # Initialize the gesture variable
    gesture = None
    
    # Check if there are multiple hand landmarks detected
    if results.multi_hand_landmarks:
        # Iterate over each hand landmark
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw the landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            
            # Get the coordinates of the thumb tip, index finger tip, middle finger tip, ring finger tip, and pinky tip
            thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
            index_finger_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_finger_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_TIP]
            
            # Check for specific hand gestures based on the finger positions
            if thumb_tip.y < index_finger_tip.y and thumb_tip.x > index_finger_tip.x:
                gesture = 'Thumbs up'
            elif index_finger_tip.y < middle_finger_tip.y and middle_finger_tip.y < ring_finger_tip.y and ring_finger_tip.y < pinky_tip.y:
                gesture = 'Peace'
            elif middle_finger_tip.y < index_finger_tip.y and middle_finger_tip.y < ring_finger_tip.y:
                gesture = 'Middle finger'
            
            # If a gesture is detected, display it on the frame
            if gesture:
                cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # Return the frame with the detected gestures
    return frame

def main():
    # Open the video capture device
    cap = cv2.VideoCapture(0)
    
    # Initialize the hands detection model from mediapipe
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
    
    # Start the video capture loop
    while True:
        # Read a frame from the video capture device
        ret, frame = cap.read()
        
        # Break the loop if no frame is captured
        if not ret:
            break
        
        # Flip the frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)
        
        # Track hand gestures in the frame
        frame_with_gestures = track_hand_gesture(frame, hands)
        
        # Display the frame with the detected gestures
        cv2.imshow('Hand Gesture Tracker', frame_with_gestures)
        
        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture device and close all windows
    cap.release()
    cv2.destroyAllWindows()
    
    # Close the hands detection model
    hands.close()

if __name__ == "__main__":
    main()
