# 🧠 Smart Switch Control Panel

A Python-based Smart Switch Control Panel with GUI to control electronic devices via **face detection** and **relay switching** using serial communication (Arduino/ESP32). Built with `customtkinter` for a modern UI and OpenCV for computer vision.

---

## ⚙️ Features

- ✅ Face Detection using OpenCV (Haarcascade-based)
- ✅ Select and apply GPIO Pin for relay
- ✅ Select COM Port dynamically
- ✅ Turn ON/OFF relay manually
- ✅ Live relay status updates
- ✅ Smart automation: Lights turn ON when face is detected
- ✅ Modern, dark-themed GUI using CustomTkinter
- ✅ Terminal logs for debugging & actions

---

## 🧠 Computer Vision Feature

This app uses **OpenCV's Haar Cascade Classifier** to detect faces in real-time using a webcam.  
As soon as a face is detected, the system **automatically turns ON the connected relay** (e.g., for switching on lights).

This gives the “Iron Man” experience — walk into a room, and lights turn ON 😎⚡.

---

## 🖥️ Tech Stack

- Python 3.x
- **OpenCV** (Haarcascade face detection)
- **CustomTkinter** (Modern GUI)
- **PyFirmata** (Arduino communication)
- **PySerial** (Serial port detection/control)

---

## 🧪 How to Run

1. **Clone the repo**
```bash
git clone https://github.com/your-username/smart-switch-control.git
cd smart-switch-control
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
python main.py
```

---

## 📝 Usage

- Connect your Arduino/ESP32 to the computer.
- Connect relay to a valid digital pin (e.g., D9).
- Select correct **COM Port** and **Pin Number** in the GUI.
- Use ON/OFF buttons to manually control.
- Click "Face Detection Switch" to enable automation via webcam.

---

## 📦 Folder Structure

```
├── main.py             # GUI + logic
├── facedetection.py    # Face detection via OpenCV
├── switch.py           # Relay communication logic
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ✨ Demo

*Coming soon — animated GIF or video showing face-controlled light turning ON.*

---

## 👨‍💻 Author

**Sabyasachi Panda (aka Roshan)**  
MCA Student | Full Stack + AI Developer | Builder of cool tech

---

## 🔐 License

MIT License — Use freely, credit appreciated.