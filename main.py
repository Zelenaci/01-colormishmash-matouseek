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
        self.protocol('WM_DELETE_WINDOW', self.quit)

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
            
        self.colorLoad()

    def mousehandler(self, event):
        if self.cget('cursor') != 'pencil':
            self.config(cursor='pencil')
            self.color = event.widget.cget('background')
        elif self.cget('cursor') == 'pencil':
            self.config(cursor='')
            event.widget.config(background=self.color)

            if event.widget is self.canvasMain:
                self.canvasColor2Slids(self.canvasMain)


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

    def canvasColor2Slids(self, canvas):
        color = canvas.cget('background')
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        self.varR.set(r)
        self.varG.set(g)
        self.varB.set(b)

    def colorSave(self):
        with open('colors.txt', 'w') as f:
            f.write(self.canvasMain.cget('background') + '\n')
            for canvas in self.canvasMem:
                f.write(canvas.cget('background') + '\n')

    def colorLoad(self):
        with open('colors.txt', 'r') as f:
            colorcode = f.readline().strip()
            self.canvasMain.config(background=colorcode)
            self.canvasColor2Slids(self.canvasMain)
            for canvas in self.canvasMem:
                colorcode = f.readline().strip()
                canvas.config(background=colorcode)

    def quit(self, event=None):
        self.colorSave()
        super().quit()


app = Application()
app.mainloop()