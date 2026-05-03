🧠 PPE Detection System (YOLOv8)
<p align="center"> <img src="https://img.shields.io/badge/YOLOv8-Object%20Detection-blue?style=for-the-badge"> <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge"> <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge"> </p>
🚀 Live Demo (Sample Output)
<p align="center"> <img src="https://github.com/user-attachments/assets/36d2b595-25f0-4175-8aa1-acfe1d30e881" width="400"/> </p>
📌 Overview

A real-time AI-based safety system that detects whether workers are wearing:
👷 Person
🪖 Helmet / ❌ No Helmet
🦺 Safety Vest / ❌ No Vest
⚠️ Automatically triggers alerts when safety violations are detected.

🔥 Features

✨ Real-time detection (Video/Webcam)
✨ PPE compliance monitoring
✨ Instant violation alerts
✨ Clean bounding boxes (YOLOv8 visualization)
✨ Lightweight & fast inference



🧠 How It Works
Input Video/Webcam
        ↓
YOLOv8 Model (best.pt)
        ↓
Object Detection
        ↓
Violation Check
        ↓
🚨 Alert Output


🛠️ Tech Stack
Technology	Usage
Python	Core Programming
OpenCV	Video Processing
YOLOv8	Object Detection
NumPy	Data Handling


📂 Project Structure
PPE-Detection/
│── best.pt
│── PPE_model.py
│── video9.mp4
│── requirements.txt
│── README.md


⚙️ Installation
git clone https://github.com/your-username/PPE-Detection.git
cd PPE-Detection
pip install -r requirements.txt

▶️ Run the Project
python PPE_model.py
📷 For webcam:
cap = cv2.VideoCapture(0)
🚨 Alert System
🚨 ALERT: NO-HELMET detected!
🚨 ALERT: NO-VEST detected!

📊 Model Info
Model: YOLOv8 (Custom-trained)
Framework: Ultralytics
Task: Object Detection

💡 Future Enhancements
🔔 Sound Alert System
🌐 Web App (Flask + React)
📱 Mobile Integration
☁️ Cloud Deployment
📊 Analytics Dashboard

🧑‍💻 Author.
Nidheesh Reddy
💻 AI/ML | Computer Vision | Full Stack Learner

⭐ Show Some Love
If you like this project, give it a ⭐ on GitHub!
