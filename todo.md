# ✅ Smart Switch Control System — To-Do Progress

## 🔧 Functional Features

- [x] Relay ON/OFF switch (Manual control via GUI)
- [x] Face Detection Trigger (Relay ON on face detection)
- [x] Remote MongoDB-triggered Switch (Relay ON on new insert)
- [x] Custom Pin Selection from Dropdown (1–15)
- [x] Custom Port Selection from Dropdown (COM1–COM10)
- [x] MongoDB Atlas Client Integration
- [x] Remote Control Active Tag in UI
- [ ] Relay OFF on MongoDB condition (e.g. specific field or value)
- [ ] Log every event (ON/OFF, Face Trigger, Mongo Trigger) to a local file
- [ ] Notifications (e.g. popup or sound when triggered remotely)

## 🎨 UI Enhancements

- [x] Dark Theme using `customtkinter`
- [x] Relay Status Label (ON/OFF display)
- [x] face detection control
- [x] Remote Control Status Label (Visible on activation)
- [ ] Add icons or animations for better UI/UX
- [ ] Add minimize-to-tray functionality
- [ ] work on web dashboard 
- [ ] work on remote on off panel 

## 🧠 AI/Automation

- [x] Face Detection integrated with physical control (via `facedetection.py`)
- [ ] Add face registration (Only known faces trigger relay)
- [ ] ML-based smart switching based on past usage pattern

## 🧪 Testing

- [ ] Add unit tests for switch module
- [ ] Add MongoDB mocking for offline testing

## 📦 Deployment

- [ ] Convert script to `.exe` using `pyinstaller`
- [ ] Auto-start on boot (Windows/Linux)

---

Last Updated: **2025-05-22**
