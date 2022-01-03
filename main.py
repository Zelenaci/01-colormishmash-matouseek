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
        self.frameR = tk.Frame(self)
        self.frameR.pack()
        self.lblR = tk.Label(self.frameR, text='R') #rika se tomu widgety
        self.lblR.pack(side=tk.LEFT, anchor=tk.S) #umistime ho na screen
        self.varR = tk.IntVar()
        self.scaleR = tk.Scale(self.frameR, from_=0, to=255, orient=tk.HORIZONTAL, length=510, variable=self.varR) #from je keyword, tak se pise from_, aby to nebralo jako importovani
        self.scaleR.pack(side=tk.LEFT, anchor=tk.S)
        self.entryR = tk.Entry(self.frameR, width=5, textvariable=self.varR)
        self.entryR.pack(side=tk.LEFT, anchor=tk.S)

        #G
        self.frameG = tk.Frame(self)
        self.frameG.pack()
        self.lblG = tk.Label(self.frameG, text='G')
        self.lblG.pack(side=tk.LEFT, anchor=tk.S)
        self.varG = tk.IntVar()
        self.scaleG = tk.Scale(self.frameG, from_=0, to=255, orient=tk.HORIZONTAL, length=510,variable=self.varG) 
        self.scaleG.pack(side=tk.LEFT, anchor=tk.S)
        self.entryG = tk.Entry(self.frameG, width=5, textvariable=self.varG)
        self.entryG.pack(side=tk.LEFT, anchor=tk.S)

        #B
        self.frameB = tk.Frame(self)
        self.frameB.pack()
        self.lblB = tk.Label(self.frameB, text='B')
        self.lblB.pack(side=tk.LEFT, anchor=tk.S) 
        self.varB = tk.IntVar()
        self.scaleB = tk.Scale(self.frameB, from_=0, to=255, orient=tk.HORIZONTAL, length=510,variable=self.varB)
        self.scaleB.pack(side=tk.LEFT, anchor=tk.S)
        self.entryB = tk.Entry(self.frameB, width=5, textvariable=self.varB)
        self.entryB.pack(side=tk.LEFT, anchor=tk.S)

        self.canvasMain = tk.Canvas(width=510, height=100, background='#000000')
        self.canvasMain.pack()
        self.canvasMain.bind('<Button-1>', self.mousehandler)
        self.varMain = tk.StringVar()
        self.entryMain = tk.Entry(self, textvariable=self.varMain, state='readonly', readonlybackground='#eeeeee')
        self.entryMain.pack()

        self.btn = tk.Button(self, text="Quit", command=self.quit) #widget
        self.btn.pack()

        self.btn2 = tk.Button(self, text="About", command=self.quit) #widget
        self.btn2.pack()

        self.varR.trace('w', self.change)
        self.varG.trace('w', self.change)
        self.varB.trace('w', self.change)

        self.frameMem = tk.Frame(self)
        self.frameMem.pack()
        self.canvasMem = []

        for row in range(3):
            for column in range(7):
                canvas = tk.Canvas(self.frameMem, width=50, height=50, background='#abcdef')
                canvas.grid(row=row, column=column)
                canvas.bind('<Button-1>', self.mousehandler)
                self.canvasMem.append(canvas)

    def mousehandler(self, event):
        if self.cget('cursor') != 'pencil':
            self.config(cursor='pencil')
            self.color = event.widget.cget('background')
        elif self.cget('cursor') == 'pencil':
            self.config(cursor='')
            event.widget.config(background=self.color)

    def change(self, var, index, mode):
        
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        colorstring = f'#{r:02x}{g:02x}{b:02x}'
        self.canvasMain.config(background=colorstring)
        self.varMain.set(colorstring)

        self.varR.set(r)
        self.varG.set(g)
        self.varB.set(b)


    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()