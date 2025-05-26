# 🦾 Bionic Hand — Real-Time Servo Control with Computer Vision

This is a robotics project Im building from scratch at 15 years old — a **computer-vision-controlled bionic hand**. It uses **MediaPipe** hand tracking, Python, A bit of C++, and an Arduino to replicate human finger movement with servos and 3D-printed fingers.

This system tracks **hand gestures directly from a camera**, translating finger positions into real-time servo angles — no physical sensors required.

---

## 🎥 Demo

*Coming soon

---

## 🧠 How It Works

1. **Hand Tracking**  
   - Uses [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands) to detect 21 hand landmarks from a webcam feed.

2. **Angle Calculation**  
   - Measures the angle of each finger by comparing key joint landmarks.
   - Maps the angle to servo-compatible values (0°–180°).

3. **Servo Control**  
   - Sends commands to an Arduino using `pyFirmata`.
   - Controls 5 servos, one per finger (starting with index).

---

## 🛠️ Tech Stack

- Python 3
- MediaPipe
- OpenCV
- PyFirmata (Arduino control)
- Arduino Uno / Nano
- MG90s micro servos
- 3D-printed finger mechanism (custom design)

---

## 📁 Project Structure
```plaintext
bionic-hand/
├── main.py                 # Entry point — reads webcam
├── preprocessors.py        # Landmark detection & angle calculation
├── indexServoControl.py    # Controls index finger servo (more to be added)
├── README.md               # You're reading it!
```

## 🤝 Collaboration
I'm happy for others to learn from or build on this project, but I'm currently not seeking collaboration.  
