# 👁️ Eye Detection

### Real-Time Face, Eye, Iris & Gaze Tracking with Python, OpenCV and MediaPipe

A Python-based real-time computer vision project that uses a webcam to detect and track facial and eye-related landmarks. The project explores **face detection, eye tracking, iris tracking, gaze analysis, and gesture detection** as a foundation for future hands-free computer interaction.

> 🚧 **Project Status:** In Development

---

## 📌 Project Overview

**Eye Detection** is a real-time computer vision project developed using **Python, OpenCV, and MediaPipe**.

The system captures live video from a webcam and processes the frames to identify facial and eye-related information. The project is being developed incrementally, starting from camera access and face detection and progressing toward eye, iris, gaze, and gesture-based interaction.

The long-term goal is to build a foundation for **hands-free computer control**, including applications such as gaze-based navigation and accessibility-focused interfaces.

---

## ✨ Key Features

### Currently Implemented / Developed

* 🎥 Real-time webcam video capture
* 🙂 Face detection/tracking
* 👁️ Eye-related landmark detection
* 🔵 Iris detection/tracking experiments
* 👀 Gaze detection/analysis module
* 🤏 Eye/gesture detection module
* 🧠 MediaPipe-based landmark processing
* ⚡ Real-time OpenCV frame processing
* 🧩 Modular Python scripts for individual computer-vision tasks

### Not Yet Fully Implemented

The following are **development goals rather than completed features**:

* ❌ Reliable blink-to-control interaction
* ❌ Complete gaze-based computer control
* ❌ Production-ready Instagram/Reels navigation
* ❌ Fully integrated hands-free control system

---

## 🔄 How It Works

The project follows a modular computer-vision pipeline:

```text
Webcam
   │
   ▼
Video Frame Capture
   │
   ▼
OpenCV Processing
   │
   ▼
MediaPipe Face / Landmark Processing
   │
   ├── Face Detection
   │
   ├── Eye Detection
   │
   ├── Iris Detection
   │
   ├── Gaze Analysis
   │
   └── Gesture Detection
   │
   ▼
Visual Output / Analysis
```

Each stage is separated into Python modules so that individual components can be tested and improved independently.

---

## 🛠️ Technologies Used

| Technology               | Purpose                                       |
| ------------------------ | --------------------------------------------- |
| **Python**               | Core programming language                     |
| **OpenCV**               | Webcam access and real-time image processing  |
| **MediaPipe**            | Face and facial landmark processing           |
| **NumPy**                | Numerical processing used by the vision stack |
| **MediaPipe Task Model** | Facial landmark model processing              |
| **VS Code**              | Development environment                       |

### Environment Used

```text
Python 3.13.14
OpenCV / OpenCV-Contrib 5.0.0.93
MediaPipe 1.0.1
NumPy 2.5.3
Windows
```

---

## 📁 Project Structure

The project is organized into separate scripts for different stages of the computer-vision pipeline:

```text
cd Eye-detection/
│
├── test_camera.py
├── face_detection.py
├── iris_detection.py
├── eye_detection.py
├── gaze_detection.py
├── gesture_detection.py
├── reel_control.py
│
├── face_landmarker.task
│
└── venv/
```

### File Responsibilities

| File                   | Purpose                                                 |
| ---------------------- | ------------------------------------------------------- |
| `test_camera.py`       | Tests webcam/camera access                              |
| `face_detection.py`    | Face detection/tracking experiments                     |
| `iris_detection.py`    | Iris detection/tracking                                 |
| `eye_detection.py`     | Eye-related detection and landmark processing           |
| `gaze_detection.py`    | Gaze estimation/analysis                                |
| `gesture_detection.py` | Eye/gesture detection experiments                       |
| `reel_control.py`      | Intended integration point for hands-free reel controls |
| `face_landmarker.task` | MediaPipe facial landmark model                         |
| `venv/`                | Local Python virtual environment                        |

> **Note:** `reel_control.py` is treated as an integration/development module rather than a completed reel-control implementation.

---

## 📦 Requirements

Recommended environment:

* Windows 10/11
* Python 3.13.x
* Webcam
* Visual Studio Code or another Python-compatible IDE
* Working internet connection for package installation

Required Python packages include:

```text
opencv-contrib-python
mediapipe
numpy
```

The project environment also uses MediaPipe-related dependencies such as:

```text
matplotlib
sounddevice
flatbuffers
absl-py
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
Eye-detection
```

### 2. Create a Virtual Environment

Windows PowerShell:

```powershell
python -m venv venv
```

### 3. Activate the Environment

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, use an appropriate PowerShell execution-policy setting for your local environment.

### 4. Install Dependencies

```powershell
pip install opencv-contrib-python mediapipe numpy
```

If a `requirements.txt` file is added to the repository later, installation can instead be simplified to:

```powershell
pip install -r requirements.txt
```

---

## ▶️ How to Run

Start by verifying that the webcam works:

```powershell
python test_camera.py
```

Then individual modules can be tested separately.

### Face Detection

```powershell
python face_detection.py
```

### Iris Detection

```powershell
python iris_detection.py
```

### Eye Detection

```powershell
python eye_detection.py
```

### Gaze Detection

```powershell
python gaze_detection.py
```

### Gesture Detection

```powershell
python gesture_detection.py
```

### Reel Control Module

```powershell
python reel_control.py
```

> `reel_control.py` is currently intended as the integration layer for future hands-free controls.

---

## 🧑‍💻 Usage

1. Connect a working webcam.
2. Activate the project's virtual environment.
3. Run the required Python module.
4. Allow the application to access the camera.
5. Position your face clearly within the camera frame.
6. Observe the real-time computer-vision output.
7. Test individual detection modules independently before integrating them.

For development and debugging, it is recommended to test the modules in this order:

```text
Camera
  ↓
Face
  ↓
Eyes
  ↓
Iris
  ↓
Gaze
  ↓
Gestures
  ↓
Future Computer Control
```

---

## 🖥️ Output / Expected Result

When a detection module is running successfully, the webcam feed is processed in real time and relevant detection information is displayed over the video.

Depending on the module, the output may include:

* Face detection information
* Eye-related landmarks
* Iris tracking indicators
* Gaze-related information
* Gesture/detection feedback

The exact visual output depends on the individual Python script being executed.

---

## 📸 Screenshots

Add project screenshots here after capturing the final outputs.

### Webcam / Face Detection

```text
[ Add screenshot here ]
```

### Eye / Iris Detection

```text
[ Add screenshot here ]
```

### Gaze Detection

```text
[ Add screenshot here ]
```

### Gesture Detection

```text
[ Add screenshot here ]
```

Example Markdown for GitHub:

```markdown
![Face Detection](screenshots/face_detection.png)
![Eye Detection](screenshots/eye_detection.png)
![Iris Detection](screenshots/iris_detection.png)
![Gaze Detection](screenshots/gaze_detection.png)
```

---

## ✅ Current Capabilities

The current project demonstrates practical work with:

* Real-time webcam processing
* OpenCV-based computer vision
* MediaPipe facial landmark processing
* Face detection
* Eye detection/landmark tracking
* Iris detection experiments
* Gaze detection experiments
* Gesture detection experiments
* Modular Python project organization

The project is currently focused on **building and validating the computer-vision components** required for future hands-free interaction.

---

## 🚀 Future Enhancements

Planned improvements include:

* 👀 More reliable gaze-direction estimation
* 😉 Robust blink detection
* 📱 Gaze-based next/previous reel navigation
* ▶️ Blink-based play/pause control
* 🖱️ Hands-free cursor interaction
* 🎯 Improved calibration and accuracy
* ⚡ Better real-time performance
* 🧠 More robust gesture classification
* ♿ Accessibility-focused interaction features
* 🔗 Complete integration of detection modules into one application

### Planned Interaction Concept

```text
Eye / Gaze Input
       │
       ▼
Computer Vision Processing
       │
       ▼
Gesture / Gaze Classification
       │
       ▼
User Intent
       │
       ├── Next Reel
       ├── Previous Reel
       └── Play / Pause
```

---

## 🧠 Challenges & Learning Outcomes

This project has provided hands-on experience with several practical computer-vision challenges.

### Challenges

* Working with real-time webcam frames
* Handling facial landmark detection
* Understanding eye and iris landmarks
* Processing gaze-related information
* Managing MediaPipe model files
* Working with Python virtual environments
* Debugging computer-vision pipelines
* Integrating multiple independent detection modules

### Learning Outcomes

Through this project, I gained practical experience in:

* Python-based computer vision
* OpenCV
* MediaPipe
* Facial landmark processing
* Real-time image processing
* Modular project development
* Debugging vision-based applications
* Designing a foundation for human-computer interaction

---

## 💡 Applications

The technology explored in this project can potentially be applied to:

* ♿ Accessibility-focused computer interfaces
* 🖥️ Hands-free computer interaction
* 👁️ Gaze-based navigation
* 🎮 Gesture-controlled applications
* 📱 Touch-free media navigation
* 🧪 Computer-vision research and experimentation
* 🤖 Human-computer interaction systems

---

## 🤝 Contributing

Contributions and suggestions are welcome.

To contribute:

```bash
# Fork the repository

# Create a new branch
git checkout -b feature/improvement

# Make your changes

# Commit your changes
git commit -m "Add improvement"

# Push the branch
git push origin feature/improvement
```

Then open a Pull Request with a clear description of the changes.

---

## 📄 License

This project is intended primarily as a learning and portfolio project.

A specific open-source license can be added to the repository through a `LICENSE` file when the project is ready for external contributions and redistribution.

---

## 👨‍💻 Author

**Rajat Jaiswal**

B.Tech — Data Science Engineering

Interested in:

* Python
* Data Science
* Artificial Intelligence
* Machine Learning
* Computer Vision
* Human-Computer Interaction

---

## ⭐ Project Status

```text
🟢 Webcam Processing
🟢 Face Detection
🟢 Eye Detection
🟢 Iris Detection
🟡 Gaze Detection
🟡 Gesture Detection
🟡 Integration
🔵 Hands-Free Control — Future Development
```

If you find this project useful or interesting, consider giving the repository a ⭐.
