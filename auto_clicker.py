import ctypes
import threading
import time

# Constants for mouse event flags
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

# Key codes for toggle and exit keys
VK_F8 = 0x77  # Virtual key code for F8
VK_ESC = 0x1B  # Virtual key code for Escape

# Global variables
running = False
delay = 0.01  # Delay between clicks in seconds

# Function to perform mouse click using ctypes
def mouse_click():
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# Function to run the auto clicker
def auto_clicker():
    global running
    while running:
        mouse_click()
        time.sleep(delay)

# Function to check if a key is pressed
def is_key_pressed(key_code):
    return ctypes.windll.user32.GetAsyncKeyState(key_code) & 0x8000 != 0

# Main function to manage the clicker
def main():
    global running, delay

    print("Auto Mouse Clicker")
    print("Press F8 to start/stop the auto clicker.")
    print("Press ESC to exit the program.")

    while True:
        if is_key_pressed(VK_F8):  # Toggle auto clicker
            if running:
                running = False
                print("Auto clicker stopped.")
            else:
                running = True
                print("Auto clicker started.")
                thread = threading.Thread(target=auto_clicker)
                thread.start()
            time.sleep(0.5)  # Debounce the key press

        if is_key_pressed(VK_ESC):  # Exit the program
            if running:
                running = False
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
