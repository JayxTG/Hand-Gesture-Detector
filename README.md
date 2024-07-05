# Hand Gesture Tracker ✋

Hand Gesture Tracker is a real-time vision-based application designed to detect and recognize specific hand gestures using a webcam. This tool utilizes computer vision techniques and the Mediapipe library to detect hand landmarks and recognize gestures like "Thumbs Up", "Peace", and "Middle Finger".

## Features 🔧

- **Real-time Gesture Detection:** Detect hand gestures using a webcam in real-time.
- **Gesture Recognition:** Recognize specific gestures such as "Thumbs Up", "Peace", and "Middle Finger".
- **Visual Feedback:** Display the detected gesture on the screen in real-time.

## How It Works 🛠️

The tool captures video from a connected webcam, processes each frame to detect hand landmarks using Mediapipe, and analyzes the positions of specific landmarks to identify gestures. Once a gesture is recognized, it displays the gesture on the video feed.

## Setup and Usage 🚀

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Hand-Gesture-Tracker.git
   cd Hand-Gesture-Tracker
   ```
2. ** Install Dependencies: Ensure you have Python installed along with the necessary libraries: **
   ```bash
      pip install opencv-python mediapipe
   ```
3. ** Run the Application: Execute the hand_gesture_tracker.py script to start the application: **
  ```bash
   python hand_gesture_tracker.py
   ```
4. ** Usage: **
- Position your hand in view of the webcam.
- The application will detect and recognize gestures, displaying the recognized gesture on the video feed.
- Press 'q' on your keyboard to close the application and release the webcam.

## Dependencies 📦
- OpenCV
- Mediapipe

## Contributing 🤝
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License 📄
This project is open-source and available under the MIT License. See the LICENSE file for more details.
