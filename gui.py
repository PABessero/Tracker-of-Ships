import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import *

from data import Save


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

        def alertbox():
            if askyesno('Warning', 'Are you sure you want to do this?'):
                quit(self)

        def get_info():
            self.save.get_info()

        self.window.title(title)
        self.window.geometry(geometry)
        self.window.minsize(480, 360)
        self.window.iconbitmap("assets/enhancedDefence.ico")
        self.window.config(background=self.background)

        menubar = Menu(self.window)
        filemenu = Menu(menubar, tearoff=0)
        openicon = PhotoImage(file="./folder.png")

        filemenu.add_command(label="Open ", image=openicon, compound="left", command=get_path)
        filemenu.add_command(label="Get info", command=get_info)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=alertbox)
        menubar.add_cascade(label="File", menu=filemenu)

        # frame = Frame(self.window, background=self.background)
        # frame.pack(expand=YES)

        # self.canvas = Canvas(frame, width=self.width, height=self.height, bg=self.background, bd=0,
        #                      highlightthickness=0)
        # self.canvas.grid(row=0, column=0, sticky=W)

        # entry_path = tkinter.Entry(self.window)
        # self.canvas.create_window(200, 140, window=entry_path)

        # path_button = ttk.Button(self.window, text='Set save path', command=get_path)
        # path_button.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)
        # # self.canvas.create_window(200, 180, window=path_button)
        #
        # info_button = ttk.Button(self.window, text='Get Info', command=get_info)
        # info_button.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

        panel = ttk.Panedwindow(self.window, height=300, width=600)
        panel.grid(column=0, row=20, rowspan=50, sticky=tkinter.S)
        # self.canvas.create_window(400, 180, window=info_button)

        self.window.columnconfigure(0, weight=4)
        self.window.columnconfigure(1, weight=1)

        self.window.config(menu=menubar)
