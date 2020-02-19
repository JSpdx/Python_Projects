








from tkinter import *
import tkinter as tk
from tkinter import messagebox

#Importing other modules
#for project
import phonebook_gui
import phonebook_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):

        #define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #height, width
        self.master.maxsize(500,300)
        #This centerWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg='#f0f0f0')
        #This protocol method is a tkinter built-in method to catch if
        #the user clicks the upper corner, "X" on WIndows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))

        #load in the GUI widgets from a separate module,
        #keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
