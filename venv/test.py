#import tkinter module
import tkinter as tk

#create window
window = tk.Tk()

#provide size to window
window.geometry("300x300")

#create frame
fr = tk.Frame(window, bg= "orange")

#add text label to frame
tk.Label(fr, text="Hello From Educative !!!").pack(padx=40,pady=40)

fr.pack()

window.mainloop()