# import
import tkinter
from tkinter import *
from tkinter import filedialog

import json


class Save:
    path: str
    doubleMagic: bool = False
    doubleDefense: bool = False
    magic: bool = False

    def switch(self, line: str):
        if ":" in line:
            key, value = line.split(':')
            key = key.strip()
            key = key.strip("\"")
            value = value.strip()

            if "isDoubleDefenseAcquired" in key:
                print(key)
                print(value)
                if line[-1] == "0":
                    self.doubleDefense = False
                    print("No double defense")
                else:
                    self.doubleDefense = True
                    print("Has double defense")
                    print(line[-1])

            if "isDoubleMagicAcquired" in key:
                print(key)

                print(value)

                if line[-1] == "0":
                    self.doubleMagic = False
                    print("No double magic")
                else:
                    self.doubleMagic = True
                    print("Has double magic")
                    print(line[-1])

    def get_info2(self):
        lines = []
        with open(self.path, "r") as saveFile:
            # curLine = saveFile.readline()
            data = saveFile.read()
            lines = data.strip().split("\n")
            print(data)
            test = json.loads(data)
            # while curLine != "":
            #     self.switch(curLine.strip())
        print(len(lines))
        for line in lines:
            self.switch(line.strip(','))
        print(test)



class Window:
    background = "black"
    font = "Arial"
    fg = "white"
    width = 600
    height = 600

    window = Tk()

    save: Save = Save()

    canvas: tkinter.Canvas

    def __init__(self, title: str, geometry: str):
        def get_path():
            file_path = tkinter.filedialog.askopenfilename()
            print("Path: " + file_path)
            if ".sav" in file_path:
                self.save.path = file_path
            else:
                print("File doesnt match the right extension")

        def get_info():
            self.save.get_info2()

        self.window.title(title)
        self.window.geometry(geometry)
        self.window.minsize(480, 360)
        self.window.iconbitmap("assets/enhancedDefence.ico")
        self.window.config(background=self.background)

        frame = Frame(self.window, background=self.background)
        frame.pack(expand=YES)

        self.canvas = Canvas(frame, width=self.width, height=self.height, bg=self.background, bd=0,
                             highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky=W)

        entry_path = tkinter.Entry(self.window)
        self.canvas.create_window(200, 140, window=entry_path)

        path_button = tkinter.Button(text='Set save path', command=get_path)
        self.canvas.create_window(200, 180, window=path_button)

        info_button = tkinter.Button(text='Get Info', command=get_info)
        self.canvas.create_window(400, 180, window=info_button)


test = Window(title="Ship Tracker", geometry="1080x720")
test.window.mainloop()
