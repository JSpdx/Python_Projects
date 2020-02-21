
from tkinter import *

from tkinter import ttk

from tkinter.filedialog import askdirectory
import tkinter as tk
import os
import sqlite3
import shutil
import time
#from datetime import datetime



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):

        self.master = master
        self.master.minsize(700,250)
        self.master.maxsize(700,250)
        
        self.master.title("Move all .txt files in a directory")
        self.master.configure(bg='#f0f0f0')

#================================GUI+++++++++++++++++++++++++

    # Buttons
        self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Source',command= self.getSourceDir)
        self.btn_browse1.grid(row=1,column=0,padx=(20,0),pady=(70,0),sticky=W)

        self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Destination',command= self.getDestDir)
        self.btn_browse2.grid(row=2,column=0,padx=(20,0),pady=(20,0),sticky=W)

        self.btn_check = tk.Button(self.master,width=12,height=3,text='Move .txt files',command=self.transfer_txt_files)
        self.btn_check.grid(row=3,column=0, columnspan=1, rowspan=2, padx=(20,0),pady=(20,0),sticky=W)
        
        self.btn_close = tk.Button(self.master,width=12,height=3,text='Close Program',command=root.destroy)
        self.btn_close.grid(row=3,column=3, rowspan=2, padx=(450,0),pady=(20,0), sticky=E)

        
    #entry forms
        self.form1 = tk.Entry(self.master, text='')
        self.form1.grid(row=1 ,column=1, columnspan=3, padx=(20, 0), pady=(70, 0), sticky=W+E)

        self.form2 = tk.Entry(self.master, text='')
        self.form2.grid(row=2 ,column=1, columnspan=3, padx=(20, 0), pady=(20, 0), sticky=W+E)


#============================Functionality================================================

        
    

    def getSourceDir(self):
        try:
            name = askdirectory(title='Choose source directory')
            self.form1.insert(END, name)
        except:
            print("No file exists")

    def getDestDir(self):
        try:
            name = askdirectory()
            self.form2.insert(END, name)
        except:
            print("No file exists")

    def transfer_txt_files(self):
        source = self.form1.get()
        destination = self.form2.get()
        for file in os.listdir(source):
            if file.endswith(".txt"):
                mtime = os.path.getmtime(os.path.join(source, file))
                lastmodified = time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(mtime))
                self.add_to_db(file, lastmodified)
                print(file, lastmodified)
                shutil.move(os.path.join(source, file).replace("\\","/"),destination)

    def add_to_db(self, file, lastmodified):        
        conn = sqlite3.connect('myGuiDB.db')
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS txtTbl(files TEXT, last_modified datetime);")
            conn.commit()
            cur.execute('INSERT INTO txtTbl (files, last_modified) VALUES (?,?)', (file, lastmodified)) 
        conn.close()
        

    
      



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
