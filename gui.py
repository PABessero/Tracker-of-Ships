import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *

from data import Save


class Window:
    bg = "black"
    font = "Arial"
    fg = "white"
    width = 600
    height = 600

    window = Tk()

    save: Save = Save()

    canvas: tkinter.Canvas

    def make_equipment_images(self):
        pass

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
        self.window.iconbitmap("assets/other/enhancedDefence.ico")
        self.window.config(background=self.bg)

        #variable image
        #Image Menu Bar
        self.openicon = PhotoImage(file="assets/other/folder.png")
        self.openicon.image = self.openicon

        self.infoicon = PhotoImage(file="assets/other/info.png")
        self.infoicon.image = self.infoicon

        self.exiticon = PhotoImage(file="assets/other/logout.png")
        self.exiticon.image = self.exiticon

        #Image Items
        #Row 0
        self.deku_stick = PhotoImage(file=r"assets/items/dekuStick.png")
        self.deku_stick.image = self.deku_stick

        self.deku_nut = PhotoImage(file=r"assets/items/dekuNut.png")
        self.deku_nut.image = self.deku_nut

        self.bombs = PhotoImage(file=r"assets/items/bombs.png")
        self.bombs.image = self.bombs

        self.bow = PhotoImage(file=r"assets/items/bow.png")
        self.bow.image = self.bow

        self.fireArrow = PhotoImage(file=r"assets/items/fireArrow.png")
        self.fireArrow.image = self.fireArrow

        self.dinsFire = PhotoImage(file=r"assets/items/dinsFire.png")
        self.dinsFire.image = self.dinsFire

        self.worldMap = PhotoImage(file=r"assets/maps/worldMap.png")
        self.worldMap.image = self.worldMap

        #Row 1
        self.fairy_Slingshot = PhotoImage(file=r"assets/items/fairySlingshot.png")
        self.fairy_Slingshot.image = self.fairy_Slingshot

        self.fairy_Ocarina = PhotoImage(file=r"assets/items/fairyOcarina.png")
        self.fairy_Ocarina.image = self.fairy_Ocarina

        self.ocarinaOfTime = PhotoImage(file=r"assets/items/ocarinaOfTime.png")
        self.ocarinaOfTime.image = self.ocarinaOfTime

        self.bombchus = PhotoImage(file=r"assets/items/bombchus.png")
        self.bombchus.image = self.bombchus

        self.hookshot = PhotoImage(file=r"assets/items/hookshot.png")
        self.hookshot.image = self.hookshot

        self.longshot = PhotoImage(file=r"assets/items/longshot.png")
        self.longshot.image = self.longshot

        self.iceArrow = PhotoImage(file=r"assets/items/iceArrows.png")
        self.iceArrow.image = self.iceArrow

        self.faroresWind = PhotoImage(file=r"assets/items/faroresWind.png")
        self.faroresWind.image = self.faroresWind

        #row 2

        self.boomerang = PhotoImage(file=r"assets/items/boomerang.png")
        self.boomerang.image = self.boomerang

        self.lensOfTruth = PhotoImage(file=r"assets/items/lensOfTruth.png")
        self.lensOfTruth.image = self.lensOfTruth

        self.magicBeans = PhotoImage(file=r"assets/items/magicBeans.png")
        self.magicBeans.image = self.magicBeans

        self.megatonHammer = PhotoImage(file=r"assets/items/megatonHammer.png")
        self.megatonHammer.image = self.megatonHammer

        self.lightArrows = PhotoImage(file=r"assets/items/lightArrows.png")
        self.lightArrows.image = self.lightArrows

        self.naryusLove = PhotoImage(file=r"assets/items/naryusLove.png")
        self.naryusLove.image = self.naryusLove

        #menubar
        menubar = Menu(self.window)
        filemenu = Menu(menubar, tearoff=0)

        filemenu.add_command(label="Open", image=self.openicon, compound="left", command=get_path, accelerator="Ctrl+O")
        filemenu.add_command(label="Get info", image=self.infoicon, compound="left", command=get_info)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", image=self.exiticon, compound="left", command=alertbox)
        menubar.add_cascade(label="File", menu=filemenu)

        #Placement Item Track
        Label(self.window, image=self.worldMap, bg=self.bg).grid(row=0, rowspan=3, column=6, sticky=W + E + N + S)

        #Row = 0
        Label(self.window, image=self.deku_stick, bg=self.bg).grid(row=0, column=0,sticky=W)
        Label(self.window, image=self.deku_nut, bg=self.bg).grid(row=0, column=1, sticky=W)
        Label(self.window, image=self.bombs, bg=self.bg).grid(row=0, column=2, sticky=W)
        Label(self.window, image=self.bow, bg=self.bg).grid(row=0, column=3, sticky=W)
        Label(self.window, image=self.fireArrow, bg=self.bg).grid(row=0, column=4, sticky=W)
        Label(self.window, image=self.dinsFire, bg=self.bg).grid(row=0, column=5, sticky=W)

        #Row = 1
        Label(self.window, image=self.fairy_Slingshot, bg=self.bg).grid(row=1, column=0, sticky=W)
        Label(self.window, image=self.fairy_Ocarina, bg=self.bg).grid(row=1, column=1, sticky=W)
        Label(self.window, image=self.bombchus, bg=self.bg).grid(row=1, column=2, sticky=W)
        Label(self.window, image=self.hookshot, bg=self.bg).grid(row=1, column=3, sticky=W)
        Label(self.window, image=self.iceArrow, bg=self.bg).grid(row=1, column=4, sticky=W)
        Label(self.window, image=self.faroresWind, bg=self.bg).grid(row=1, column=5, sticky=W)

        # Row = 2
        Label(self.window, image=self.boomerang, bg=self.bg).grid(row=2, column=0, sticky=W)
        Label(self.window, image=self.lensOfTruth, bg=self.bg).grid(row=2, column=1, sticky=W)
        Label(self.window, image=self.magicBeans, bg=self.bg).grid(row=2, column=2, sticky=W)
        Label(self.window, image=self.megatonHammer, bg=self.bg).grid(row=2, column=3, sticky=W)
        Label(self.window, image=self.lightArrows, bg=self.bg).grid(row=2, column=4, sticky=W)
        Label(self.window, image=self.naryusLove, bg=self.bg).grid(row=2, column=5, sticky=W)

        # self.window.columnconfigure(0, weight=4)
        # self.window.columnconfigure(1, weight=1)

        self.window.config(menu=menubar)
