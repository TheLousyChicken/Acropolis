###################### Main Application ######################
import tkinter as tk
from tkinter import *
from tkinter_custom_button import TkinterCustomButton
import controller
import ip_address

###################### create GUI ######################
def App():
    root = tk.Tk()
    root.title("Acropolis")
    # root.geometry("600x600")
    ###################### Logic Below ######################
    
    label = tk.Label(root, text="Acropolis!")
    label2 = tk.Label(root, text="SUP")
    
    ###################### Logic Above ######################
    label2.grid(row=0, column=0)
    label.grid(row=1, column=1)
    root.mainloop()

# call App
App()

# on click send request to server/device

# device/server response