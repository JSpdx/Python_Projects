




from tkinter import *

from tkinter import ttk

from tkinter.filedialog import askdirectory
import tkinter as tk
import os


#import myGui_gui




class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):

        self.master = master
        self.master.minsize(700,250)
        self.master.maxsize(700,250)
        
        self.master.title("Check files")
        self.master.configure(bg='#f0f0f0')

#================================GUI+++++++++++++++++++++++++

    # Buttons
        self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...',command= self.getDir)
        self.btn_browse1.grid(row=1,column=0,padx=(20,0),pady=(70,0),sticky=W)


        self.txt_file1 = tk.Text(self.master)
        self.txt_file1.grid(row=1 ,column=1, columnspan=1, padx=(0, 50), pady=(0, 0))

#============================Functionality================================================

        
    

    def getDir(self):
        try:
            name = askdirectory()
            self.txt_file1.insert(END, name)
        except:
            print("No file exists")


      








if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
