# Gesture-Volume-Control

Control your computer’s **audio volume using hand gestures** through your webcam — completely touch-free!  
This project uses **OpenCV**, **MediaPipe**, and **PyCaw** to detect hand landmarks and map the distance between your thumb and index finger to your system’s volume level.  

# Overview  
The **Gesture-Based Volume Control** project is an interactive computer vision application that enables users to adjust system volume in real time.  
By analyzing the position of your fingers captured via webcam, it offers an intuitive and contactless way to manage volume — ideal for hands-free environments.  

# Features  
- Real-time hand tracking  
- Volume adjustment using thumb-index distance  
- On-screen volume bar for visual feedback
- Smooth performance and responsiveness  
- Works with any standard webcam  

# Technologies Used  
- **Python 3.x**  
- **OpenCV** – for video capture and image processing  
- **MediaPipe** – for hand detection and landmark tracking  
- **PyCaw** – for controlling the system audio (Windows)  
- **NumPy** – for mathematical operations  

# How It Works
1. Webcam captures your hand in real time.
2. MediaPipe detects landmarks on your hand.
3. The distance between the thumb tip and index finger tip is calculated.
4. This distance is mapped to a volume level (0% – 100%).
5. The system volume changes dynamically.
6. An on-screen bar provides visual feedback of the current volume.

