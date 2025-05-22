from switch import relayon, relayoff, setup_board, set_relay_pin, exit_board
import customtkinter as ctk
from facedetection import facedetect
from data import connect_to_mongodb, watch_new_inserts
import threading
from pymongo import MongoClient
from datetime import datetime


current_theme = "dark-blue"

connection_string = "mongodb+srv://roshan:roshanpwd@cluster0.uf1x9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)


db = client["dataa"]
collection = db["upload"]

# Relay and remote status text
relay_status = None
remote_status = None

def update_status(text):
    relay_status.configure(text=f"Relay: {text}")

def update_remote_status(text):
    remote_status.configure(text=text)

def turnrelayon():
    relayon()
    update_status("ON")
    dataa = {
    "status": "Working",
    "relay":"ON",
    "timestamp": datetime.now(),
    "medium":"manual on"
    }

# Insert the data
    result = collection.insert_one(dataa)

# Print inserted ID
    print("Inserted ID:", result.inserted_id)

def turnrelayoff():
    relayoff()
    update_status("OFF")
    dataa = {
    "status": "Working",
    "relay":"OFF",
    "timestamp": datetime.now(),
    "medium":"manual-off"
    }
    # Insert the data
    result = collection.insert_one(dataa)

# Print inserted ID
    print("Inserted ID:", result.inserted_id)

def faceswitch():
    facedetect(on_face_detected=lambda: (relayon(), update_status("ON")))
    dataa = {
    "status": "Working",
    "relay":"ON",
    "timestamp": datetime.now(),
    "medium":"face detected"
    }
    # Insert the data
    result = collection.insert_one(dataa)

# Print inserted ID
    print("Inserted ID:", result.inserted_id)

def handle_new_data(data):
    print("🚨 New data received from MongoDB:", data)
    relayon()
    update_status("ON")
    dataa = {

    "status": "Working",
    "relay":"ON",
    "timestamp": datetime.now(),
    "medium":"cloud"
    }
    # Insert the data
    result = collection.insert_one(dataa)

# Print inserted ID
    print("Inserted ID:", result.inserted_id)

def remoteswitch():
    print("✅ Remote switch active...")

    connection_string = "mongodb+srv://roshan:roshanpwd@cluster0.uf1x9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = connect_to_mongodb(connection_string)
    collection = client["test"]["dataas"]

    # Update UI to show remote control is active
    update_remote_status("Remote Control: ACTIVE ✅")

    watcher_thread = threading.Thread(target=watch_new_inserts, args=(collection, handle_new_data), daemon=True)
    watcher_thread.start()

def create_window(theme):
    global relay_status, remote_status

    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme(theme)

    root = ctk.CTk()
    root.geometry("500x480")
    root.title("Smart Switch Control Panel")

    # Relay control buttons
    on = ctk.CTkButton(root, text="ON", command=turnrelayon, hover_color="purple")
    on.pack(pady=10, side="left")

    off = ctk.CTkButton(root, text="OFF", command=turnrelayoff, hover_color="purple")
    off.pack(pady=10, side="right")

    face = ctk.CTkButton(root, text="Face Detection Switch", command=faceswitch, hover_color="purple")
    face.pack(pady=10)

    remote = ctk.CTkButton(root, text="Turn On Remote Switch", command=remoteswitch, hover_color="purple")
    remote.pack(pady=10)

    # Dropdown to select pin (1 to 15)
    pin_var = ctk.StringVar(value="Select Pin")
    pin_dropdown = ctk.CTkOptionMenu(root, variable=pin_var, values=[str(i) for i in range(1, 16)])
    pin_dropdown.pack(pady=10)

    def apply_pin():
        try:
            pin = int(pin_var.get())
            set_relay_pin(pin)
        except ValueError:
            print("Invalid pin selection")

    apply_pin_btn = ctk.CTkButton(root, text="Apply Pin", command=apply_pin)
    apply_pin_btn.pack(pady=5)

    # Dropdown to select port (COM1 to COM10)
    port_var = ctk.StringVar(value="Select Port")
    port_dropdown = ctk.CTkOptionMenu(root, variable=port_var, values=[f"COM{i}" for i in range(1, 11)])
    port_dropdown.pack(pady=10)

    def apply_port():
        port = port_var.get()
        setup_board(port)

    apply_port_btn = ctk.CTkButton(root, text="Apply Port", command=apply_port)
    apply_port_btn.pack(pady=5)

    # Status text at the bottom
    relay_status = ctk.CTkLabel(root, text="Relay: OFF", text_color="white")
    relay_status.pack(pady=10)

    remote_status = ctk.CTkLabel(root, text="", text_color="green")
    remote_status.pack(pady=5)

    root.protocol("WM_DELETE_WINDOW", lambda: (exit_board(), root.destroy()))
    root.mainloop()

# Run GUI
create_window(current_theme)
