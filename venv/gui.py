import tkinter as tk
from tkinter import ttk
from tkinter import *
import serial
import serial.tools.list_ports
import time
ports = serial.tools.list_ports.comports()
#print(ports)
commPort = 'None'
numConnection = len(ports)
strPort=[]
for i in range(0, numConnection):
    port = ports[i]
    strPort.append(str(port))
#print(strPort)
validports=[]
for i in range (0,len(strPort)):
       if 'Bluetooth' in strPort[i]:
           validports.append(strPort[i])
#print(validports)
coms=[]
for i in range (0,len(validports)):
       coms.append((validports[i][:5]))
#print(coms)
motor_R="1"
motor_L="2"
motor_S="0"
ser = serial.Serial(port="COM4", baudrate=115200)
def go_30(self):
    #print("in go")
    ser.write(bytes(motor_R, 'utf-8'))
    time.sleep(1)
def stop_now(self):
    #print("in go")
    ser.write(bytes(motor_S, 'utf-8'))
    time.sleep(1)

def com(event):
    #print(port_selc.get())
    new_windo=tk.Tk()
    new_windo.geometry("300x300")
    new_windo.title("Motion")
    new_windo.configure(background="#88FAE9")
    tk.Label(new_windo, text="Press . to run", font=("Times New Roman", 14), bg="#5BE752").pack(padx=40, pady=40)
    tk.Label(new_windo, text="Press 0 to stop", font=("Times New Roman", 14), bg="#FF0023").pack(padx=40, pady=60)

    ser.port=str(port_selc.get())
    new_windo.bind("<.>", go_30)
    new_windo.bind("<0>", stop_now)
    new_windo.mainloop()
window =tk.Tk()
window.geometry('400x400')
window.title("Motor Controller-Ports")
window.configure(background="#02F3E5")
#window.configure(background='#ffffff')
tk.Label(window, text="Chosse the Port",font=("Times New Roman",20),bg="#88FAE9").pack(padx=40,pady=40)
n = tk.StringVar()
port_selc = ttk.Combobox(window, width = 27, textvariable = n)
port_selc['values']=coms
port_selc['state'] = 'readonly'
port_selc.pack(padx=40,pady=40)



port_selc.bind('<<ComboboxSelected>>', com)


#print(str(ser.readline()))


window.mainloop()