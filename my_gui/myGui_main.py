




from tkinter import *
import tkinter as tk


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
        self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...')
        self.btn_browse1.grid(row=1,column=0,padx=(20,0),pady=(70,0),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...')
        self.btn_browse2.grid(row=2,column=0,padx=(20,0),pady=(20,0),sticky=W)

        self.btn_check = tk.Button(self.master,width=12,height=3,text='Check for files...')
        self.btn_check.grid(row=3,column=0, columnspan=1, rowspan=2, padx=(20,0),pady=(20,0),sticky=W)
        
        self.btn_close = tk.Button(self.master,width=12,height=3,text='Close Program')
        self.btn_close.grid(row=3,column=3, rowspan=2, padx=(450,0),pady=(20,0), sticky=E)

        #entry forms
        self.txt_file1 = tk.Entry(self.master, text='')
        self.txt_file1.grid(row=1 ,column=1, columnspan=3, padx=(20, 0), pady=(70, 0), sticky=W+E)
        self.txt_file2 = tk.Entry(self.master, text='')
        self.txt_file2.grid(row=2 ,column=1, columnspan=3, padx=(20, 0), pady=(20, 0), sticky=W+E)




        #tried to use this to configure the columns, but no luck
##        col_count, row_count = root.grid_size() 
##        for col in range(col_count):
##            root.grid_columnconfigure(4, minsize=175)
        

    













if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
