#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk

# from tkinter import ttk

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit) #propojuje udalost s nejakou akci, zmackneme esc - program quitne

        self.lblR = tk.Label(self, text='R') #rika se tomu widgety
        self.lblR.pack() #umistime ho na screen
        self.scaleR = tk.Scale(from_=0, to=255, orient=tk.HORIZONTAL, length=510, command=self.change) #from je keyword, tak se pise from_, aby to nebralo jako importovani
        self.scaleR.pack()

        self.lblG = tk.Label(self, text='G')
        self.lblG.pack()
        self.scaleG = tk.Scale(from_=0, to=255, orient=tk.HORIZONTAL, length=510,  command=self.change) 
        self.scaleG.pack()

        self.lblB = tk.Label(self, text='B')
        self.lblB.pack() 
        self.scaleB = tk.Scale(from_=0, to=255, orient=tk.HORIZONTAL, length=510,  command=self.change)
        self.scaleB.pack()

        self.canvasMain = tk.Canvas(width=510, height=100, background='#000000')
        self.canvasMain.pack()

        self.btn = tk.Button(self, text="Quit", command=self.quit) #widget
        self.btn.pack()

        self.btn2 = tk.Button(self, text="About", command=self.quit) #widget
        self.btn2.pack()

    def change(self, event):
        
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.canvasMain.config(background=f'#{r:02x}{g:02x}{b:02x}')


    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()