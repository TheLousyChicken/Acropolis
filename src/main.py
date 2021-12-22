###################### Main Application ######################
import tkinter as tk
from tkinter import *
from tkinter_custom_button import TkinterCustomButton

###################### create GUI ######################
def App():
    root = tk.Tk()
    root.title("Acropolis")
    root.geometry("900x720")
    
    ####### WINDOW MOD #######
    root.rowconfigure(0, minsize=800, weight=1)
    root.columnconfigure(1, minsize=800, weight=1)
    ###################### Main Logic Below ######################
    ### MAIN LABEL ###
    MainLabel = Label(
    text="Home Automation Project",
    foreground="white",
    background="black",
    width=900,
    height=10
    )
    
    ### ACTIVATION BUTTON ###
    Activate = TkinterCustomButton(text="Activate", corner_radius=10, command=root.destroy)
  
    ###################### Main Logic Above ######################
    Activate.pack(side=tk.BOTTOM)
    MainLabel.pack()
    root.update()
    root.mainloop()

# call App
App()

# on click send request to server/device

# device/server response