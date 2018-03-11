import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import W, N, E, S

class MainAppView(tk.Frame):
   
    def start_gui(self,ok = True):     
        if ok:
            self.mainloop()
        else:
            self.master.destroy()

    def createWidgets(self):
        self.title = tk.Label(
                self, text = " Tomograf")
        self.title.grid(
            row=0, column=0,columnspan=4, sticky = tk.E+tk.W )

      
        self.img1 = Image.open(r"C:\Users\Phil\Desktop\git\iwm\iwm_rentgen\main_app\img\brain_tomography.gif")
        self.photo1 = ImageTk.PhotoImage(self.img1)
        self.cv1 = tk.Canvas()
        self.cv1.grid(row=1, sticky='NS')
        self.cv1.create_image(10, 10, image=self.photo1, anchor='nw') 

        self.one = tk.Button(self)
        self.one["text"] = "Task 1"
        self.one.grid(row=2, column=0)

        self.two = tk.Button(self)
        self.two["text"] = "Task 2"
        self.two.grid(row=2, column=1)
     
        self.three = tk.Button(self)
        self.three["text"] = "Task 3"
        self.three.grid(row=2, column=2)

        self.four = tk.Button(self)
        self.four["text"] = "Task 4"
        self.four.grid(row=2, column=3)

        self.five = tk.Button(self)
        self.five["text"] = "Task 5"
        self.five.grid(row=2, column=4)



    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        # option is needed to put the main label in the window
        self.createWidgets()

        
    


