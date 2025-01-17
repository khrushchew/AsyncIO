from tkinter import ttk
import tkinter as tk
import time
from threading import Thread

root = tk.Tk()
root.geometry('300x300+150+150')

def thread_sleep():
    time.sleep(10)
    lab['text'] = int(lab['text']) + 10

def new_thread():
    t1 = Thread(target=thread_sleep)
    t1.start()

btn = ttk.Button(root, text='Run', command=new_thread)
btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

lab = ttk.Label(root, text='0')
lab.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

root.mainloop()
