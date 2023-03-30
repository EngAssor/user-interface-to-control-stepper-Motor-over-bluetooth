import tkinter as tk
import time
from tkinter import ttk
import serial
motor_R="1"
motor_L="2"
motor_S="0"
def go_30(self):
    print("in go")
    ser.write(bytes(motor_R, 'utf-8'))
    time.sleep(1)
def stop_now(self):
    print("in stop")
    ser.write(bytes(motor_S, 'utf-8'))
    time.sleep(1)

window =tk.Tk()
window.geometry('200x200')
ser = serial.Serial(port=str('COM15'),baudrate=115200)
window.bind("<.>", go_30)
window.bind("<0>", stop_now)
window.mainloop()
