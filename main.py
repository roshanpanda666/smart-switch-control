from switch import relayon, relayoff, setup_board, set_relay_pin, exit_board
import customtkinter as ctk
from facedetection import facedetect

current_theme = "dark-blue"

# Relay status text
relay_status = None

def update_status(text):
    relay_status.configure(text=f"Relay: {text}")

def turnrelayon():
    relayon()
    update_status("ON")

def turnrelayoff():
    relayoff()
    update_status("OFF")

def faceswitch():
    facedetect(on_face_detected=lambda: (relayon(), update_status("ON")))

def create_window(theme):
    global relay_status

    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme(theme)

    root = ctk.CTk()
    root.geometry("500x450")
    root.title("Smart Switch Control Panel")

    # Relay control buttons
    on = ctk.CTkButton(root, text="ON", command=turnrelayon, hover_color="purple")
    on.pack(pady=10, side="left")

    off = ctk.CTkButton(root, text="OFF", command=turnrelayoff, hover_color="purple")
    off.pack(pady=10,side="right")

    face = ctk.CTkButton(root, text="Face Detection Switch", command=faceswitch, hover_color="purple")
    face.pack(pady=10)

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
    relay_status.pack(pady=20)

    root.protocol("WM_DELETE_WINDOW", lambda: (exit_board(), root.destroy()))
    root.mainloop()

# Run GUI
create_window(current_theme)
