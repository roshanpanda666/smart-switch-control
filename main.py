from switch import relayon, relayoff, setup_board, set_relay_pin, exit_board
import customtkinter as ctk
from facedetection import facedetect
from data import connect_to_mongodb, watch_new_inserts
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os
import threading

# Load environment variables
load_dotenv()

# Global MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["dataa"]
collection = db["upload"]

# UI theme
current_theme = "dark-blue"

# Relay and remote status text
relay_status = None
remote_status = None

# Helper to log data to MongoDB
def log_to_mongo(relay_value, medium):
    try:
        data = {
            "status": "Working",
            "relay": relay_value,
            "timestamp": datetime.now(),
            "medium": medium
        }
        result = collection.insert_one(data)
        print("Inserted ID:", result.inserted_id)
    except Exception as e:
        print("❌ MongoDB insert failed:", e)

# UI Update functions
def update_status(text):
    relay_status.configure(text=f"Relay: {text}")

def update_remote_status(text):
    remote_status.configure(text=text)

# Relay Controls
def turnrelayon():
    relayon()
    update_status("ON")
    log_to_mongo("ON", "manual-on")

def turnrelayoff():
    relayoff()
    update_status("OFF")
    log_to_mongo("OFF", "manual-off")

def faceswitch():
    facedetect(on_face_detected=lambda: (relayon(), update_status("ON")))
    log_to_mongo("ON", "face detected")

# Mongo Watch Callback
def handle_new_data(data):
    print("🚨 New data received from MongoDB:", data)
    relayon()
    update_status("ON")
    log_to_mongo("ON", "cloud")

# Remote Control Activation
def remoteswitch():
    print("✅ Remote switch active...")
    update_remote_status("Remote Control: ACTIVE ✅")
    remote_collection = client["test"]["dataas"]
    watcher_thread = threading.Thread(target=watch_new_inserts, args=(remote_collection, handle_new_data), daemon=True)
    watcher_thread.start()

# GUI Window
def create_window(theme):
    global relay_status, remote_status

    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme(theme)

    root = ctk.CTk()
    root.geometry("500x480")
    root.title("Smart Switch Control Panel")

    # Buttons
    ctk.CTkButton(root, text="ON", command=turnrelayon, hover_color="purple").pack(pady=10, side="left")
    ctk.CTkButton(root, text="OFF", command=turnrelayoff, hover_color="purple").pack(pady=10, side="right")
    ctk.CTkButton(root, text="Face Detection Switch", command=faceswitch, hover_color="purple").pack(pady=10)
    ctk.CTkButton(root, text="Turn On Remote Switch", command=remoteswitch, hover_color="purple").pack(pady=10)

    # Relay Pin
    pin_var = ctk.StringVar(value="Select Pin")
    ctk.CTkOptionMenu(root, variable=pin_var, values=[str(i) for i in range(1, 16)]).pack(pady=10)
    ctk.CTkButton(root, text="Apply Pin", command=lambda: set_relay_pin(int(pin_var.get()) if pin_var.get().isdigit() else 0)).pack(pady=5)

    # COM Port
    port_var = ctk.StringVar(value="Select Port")
    ctk.CTkOptionMenu(root, variable=port_var, values=[f"COM{i}" for i in range(1, 11)]).pack(pady=10)
    ctk.CTkButton(root, text="Apply Port", command=lambda: setup_board(port_var.get())).pack(pady=5)

    # Status Texts
    relay_status = ctk.CTkLabel(root, text="Relay: OFF", text_color="white")
    relay_status.pack(pady=10)

    remote_status = ctk.CTkLabel(root, text="", text_color="green")
    remote_status.pack(pady=5)

    # Exit cleanly
    root.protocol("WM_DELETE_WINDOW", lambda: (exit_board(), root.destroy()))
    root.mainloop()

# Run GUI
create_window(current_theme)
