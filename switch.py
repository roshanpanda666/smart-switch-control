from pyfirmata import Arduino
import time

# Default values (can be changed dynamically)
board = None
RELAY_PIN = 9

def setup_board(port):
    global board
    try:
        board = Arduino(port)
        print(f"Connected to board on {port}")
    except Exception as e:
        print(f"Error connecting to {port}: {e}")
        board = None

def set_relay_pin(pin):
    global RELAY_PIN
    RELAY_PIN = pin
    print(f"Relay pin set to {RELAY_PIN}")

def relayon():
    if board:
        board.digital[RELAY_PIN].write(0)
        print("Relay is turned ON")
    else:
        print("Board not connected")

def relayoff():
    if board:
        board.digital[RELAY_PIN].write(1)
        print("Relay is turned OFF")
    else:
        print("Board not connected")

def exit_board():
    if board:
        board.exit()
        print("Board connection closed")
