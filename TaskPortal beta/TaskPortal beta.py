import os
from tkinter import *
import subprocess
import time

win = Tk()

win.geometry("350x200")
win.title("Task Portal 0.1")

def startxplrb():
    subprocess.run(["C:\\Windows\\explorer.exe"])

def startmng():
    subprocess.run(['C:\\Windows\\System32\\taskmgr.exe'])

taskmng = Button(text="Диспетчер задач", command=startmng)
taskmng.place(y=0, x=0)

def startrgf():
    subprocess.run(["C:\\Windows\\System32\\regedt32.exe"])


startrg = Button(text="Редактор реестра", command=startrgf)
startrg.place(y=0, x=105)

startxplr = Button(text="Проводник", command=startxplrb)
startxplr.place(y=0, x=215)

win['bg'] = 'black'

win.mainloop()
