from tkinter import *
import threading
import time

root = Tk()
root.geometry("600x400")

#toggle function
def animate_on():
    for i in range(40,160):
        time.sleep(0.007)
        icon.place(x=i,y=40)

def animate_off():
    for i in reversed(range(40,160)):
        time.sleep(0.007)
        icon.place(x=i,y=40)

def toggle_on(e):
    task1 = threading.Thread(target=animate_on)
    task1.start()
    icon.bind("<Button-1>",toggle_off)

def toggle_off(e):
    task1 = threading.Thread(target=animate_off)
    task1.start()
    icon.bind("<Button-1>",toggle_on)

#toggle image
icon_photo = PhotoImage(file="icon.png")
toggle_photo = PhotoImage(file="toggle.png")

#toggle label
toggle = Label(root,image=toggle_photo,border=0)
toggle.place(x=30,y=30)

icon = Label(root,image=icon_photo,border=0,background="#0E6BE9")
icon.place(x=40,y=40)

#toggle button bind
icon.bind("<Button-1>",toggle_on)

root.mainloop()