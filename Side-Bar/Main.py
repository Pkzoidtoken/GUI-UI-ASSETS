from tkinter import *
import threading
import time

#read about me :)
# My Youtube Channel : TipsJazzinferno

root  =  Tk()
root.geometry("776x627")

def hide():
    for i in reversed(range(65,150)):
        time.sleep(0.005)
        drop_down.config(width=i)

def show():
    for i in range(65,150):
        time.sleep(0.005)
        drop_down.config(width=i,background="#322D2D")

def task():
    task1 = threading.Thread(target=hide)
    task1.start()
    click.config(command=show_task)

def show_task():
    task1 = threading.Thread(target=show)
    task1.start()
    click.config(command=task)

# Create Frame widget
drop_down = Frame(root,bg="#322D2D",border=0,width=150,height=627)
drop_down.place(x=0,y=0)

menu_icon = PhotoImage(file="menu.png")
home_icon = PhotoImage(file="home.png")
Wallet_icon = PhotoImage(file="wallet.png")

#button hide & show
click = Button(drop_down,image=menu_icon,relief="groove",background="#322D2D",border=0,activebackground="#322D2D",command=task)
click.place(x=20,y=34)

home = Button(drop_down,image=home_icon,relief="groove",background="#322D2D",border=0,command=task)
home.place(x=20,y=104)

wallet = Button(drop_down,image=Wallet_icon,relief="groove",background="#322D2D",border=0,command=task)
wallet.place(x=20,y=160)

root.mainloop()

