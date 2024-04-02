import tkinter as tk
import serial
import threading
import subprocess

# Define Arduino serial port and baud rate
SERIAL_PORT = 'com6'  # Change this to your Arduino's serial port
BAUD_RATE = 9600

# Function to read data from Arduino continuously
def read_from_arduino():
    global arduino_data
    while True:
        if ser.in_waiting > 0:
            arduino_data = ser.readline().decode().strip()
            print("Received from Arduino:", arduino_data)

# Function to send command to Arduino
def send_command(arduino_code):
    ser.write(arduino_code.encode())
    print("Sent to Arduino:", arduino_code)

# Function to update GUI with Arduino data
def update_gui():
    label.config(text=arduino_data)
    root.after(100, update_gui)  # Update every 100 milliseconds

# Initialize Tkinter
root = tk.Tk()
root.title("Arduino Live Update Interface")
root.geometry("400x300")  # Set the window size

# Create a label to display Arduino data
arduino_data = "Waiting for data..."
label = tk.Label(root, text=arduino_data, font=('Helvetica', 18))
label.pack(pady=20)

# Initialize serial communication with Arduino
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print("Serial port opened successfully")
except serial.SerialException as e:
    print("Error opening serial port:", e)

# Start a thread to continuously read data from Arduino
thread = threading.Thread(target=read_from_arduino)
thread.daemon = True
thread.start()

# Function to compile and upload code to Arduino
# def compile_and_upload(sketch_file):
#     try:
#         subprocess.run(['arduino', '--board', 'arduino:avr:uno', '--port', SERIAL_PORT, '--upload', sketch_file])
#         print("Code uploaded successfully")
#     except subprocess.CalledProcessError as e:
#         print("Error uploading code:", e)

# Define functions for each sketch

def send_auto():
    data = "auto"
    ser.write(data.encode())
    
def send_on():
    data = "on"
    ser.write(data.encode())


def send_off():
    data = "off"
    ser.write(data.encode())
# Create buttons to upload sketches

button_auto = tk.Button(root, text="Auto", width=15, command=send_auto)
button_auto.pack(pady=5)

button_on = tk.Button(root, text="On", width=15, command=send_on)
button_on.pack(pady=5)

button_off = tk.Button(root, text="Off", width=15, command=send_off)
button_off.pack(pady=5)
# Start updating the GUI
update_gui()

# Run the Tkinter event loop
root.mainloop()