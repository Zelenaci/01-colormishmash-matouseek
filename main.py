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

        #R
        self.frameR = tk.Frame()
        self.frameR.pack()
        self.lblR = tk.Label(self.frameR, text='R') #rika se tomu widgety
        self.lblR.pack(side=tk.LEFT, anchor=tk.S) #umistime ho na screen
        self.varR = tk.StringVar()
        self.scaleR = tk.Scale(self.frameR, from_=0, to=255, orient=tk.HORIZONTAL, length=510, variable=self.varR, command=self.change) #from je keyword, tak se pise from_, aby to nebralo jako importovani
        self.scaleR.pack(side=tk.LEFT, anchor=tk.S)
        self.entryR = tk.Entry(self.frameR, width=5, textvariable=self.varR)
        self.entryR.pack(side=tk.LEFT, anchor=tk.S)

        #G
        self.frameG = tk.Frame()
        self.frameG.pack()
        self.lblG = tk.Label(self.frameG, text='G')
        self.lblG.pack(side=tk.LEFT, anchor=tk.S)
        self.varG = tk.StringVar()
        self.scaleG = tk.Scale(self.frameG, from_=0, to=255, orient=tk.HORIZONTAL, length=510,variable=self.varG,  command=self.change) 
        self.scaleG.pack(side=tk.LEFT, anchor=tk.S)
        self.entryG = tk.Entry(self.frameG, width=5, textvariable=self.varG)
        self.entryG.pack(side=tk.LEFT, anchor=tk.S)

        #B
        self.frameB = tk.Frame()
        self.frameB.pack()
        self.lblB = tk.Label(self.frameB, text='B')
        self.lblB.pack(side=tk.LEFT, anchor=tk.S) 
        self.varB = tk.StringVar()
        self.scaleB = tk.Scale(self.frameB, from_=0, to=255, orient=tk.HORIZONTAL, length=510,variable=self.varB,  command=self.change)
        self.scaleB.pack(side=tk.LEFT, anchor=tk.S)
        self.entryB = tk.Entry(self.frameB, width=5, textvariable=self.varB)
        self.entryB.pack(side=tk.LEFT, anchor=tk.S)

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

        self.varR.set(r)
        self.varG.set(g)
        self.varB.set(b)


    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()