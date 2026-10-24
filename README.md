# FaceMood 😊

**Real-Time Face Detection and Facial Emotion Recognition using Python and OpenCV**

FaceMood is a beginner-friendly computer vision project that uses a webcam to detect human faces in real time. It is designed to explore face detection and facial emotion estimation using Python and computer vision libraries.

## ✨ Features

- Real-time webcam video capture
- Face detection using OpenCV
- Facial emotion estimation using DeepFace
- Displays detected faces and emotion labels on the video feed

## 🛠️ Technologies Used

- Python
- OpenCV
- DeepFace
- Computer Vision

## 📁 Project Files

- `webcam_test.py` — Tests webcam access and video capture.
- `face_detection.py` — Detects faces in webcam frames.
- `emotion_detection.py` — Estimates facial emotions using DeepFace.

## ⚙️ Installation

1. Install Python.
2. Clone or download this repository.
3. Install the required libraries:

```bash
pip install opencv-python deepface
```

If DeepFace reports a missing dependency, install the dependency mentioned in the error message.

## ▶️ How to Run

Run these commands from the project folder:

```bash
python webcam_test.py
```

```bash
python face_detection.py
```

```bash
python emotion_detection.py
```

Allow webcam access if prompted. Press `q` to quit the video window, if supported by the running script.

## 🔒 Privacy

The project uses webcam video for live processing. Run it only with appropriate camera permissions and consent from anyone being recorded.

## 🚀 Future Improvements

- Improve emotion-estimation reliability.
- Add a simple graphical user interface.
- Improve performance and error handling.
- Document testing and limitations.

## 👩‍💻 Author

**Ramandeep Rimpy**

GitHub: [@ramandeeprimpy29-rgb](https://github.com/ramandeeprimpy29-rgb)

---

*This project is intended for learning and experimentation. Facial emotion predictions are estimates and should not be treated as reliable measurements of a person's internal emotional state.*
