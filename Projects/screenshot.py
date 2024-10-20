import time
import pyautogui
import pyscreeze
import tkinter as tk

def screenshot():
    name =int(round(time.time() * 1000))
    name = 'F:/desktop/probaba/Sceenshots/{}.png'.format(name)

    img = pyautogui.screenshot(name)


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text ="Take Screenshot",
    command= screenshot)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="Quit",
    command= quit)

close.pack(side=tk.LEFT)
root.mainloop()