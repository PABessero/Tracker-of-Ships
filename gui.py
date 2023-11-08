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
        openicon = PhotoImage(file="assets/other/folder.png")
        openicon.image = openicon

        infoicon = PhotoImage(file="assets/other/info.png")
        infoicon.image = infoicon

        exiticon = PhotoImage(file="assets/other/logout.png")
        exiticon.image = exiticon

        #Image Items
        #Row 0
        deku_stick = PhotoImage(file=r"assets/items/dekuStick.png")
        deku_stick.image = deku_stick

        deku_nut = PhotoImage(file=r"assets/items/dekuNut.png")
        deku_nut.image = deku_nut

        bombs = PhotoImage(file=r"assets/items/bombs.png")
        bombs.image = bombs

        bow = PhotoImage(file=r"assets/items/bow.png")
        bow.image = bow

        fireArrow = PhotoImage(file=r"assets/items/fireArrow.png")
        fireArrow.image = fireArrow

        dinsFire = PhotoImage(file=r"assets/items/dinsFire.png")
        dinsFire.image = dinsFire

        worldMap = PhotoImage(file=r"assets/maps/worldMap.png")
        worldMap.image = worldMap

        #Row 1
        fairy_Slingshot = PhotoImage(file=r"assets/items/fairySlingshot.png")
        fairy_Slingshot.image = fairy_Slingshot

        fairy_Ocarina = PhotoImage(file=r"assets/items/fairyOcarina.png")
        fairy_Ocarina.image = fairy_Ocarina

        ocarinaOfTime = PhotoImage(file=r"assets/items/ocarinaOfTime.png")
        ocarinaOfTime.image = ocarinaOfTime

        bombchus = PhotoImage(file=r"assets/items/bombchus.png")
        bombchus.image = bombchus

        hookshot = PhotoImage(file=r"assets/items/hookshot.png")
        hookshot.image = hookshot

        longshot = PhotoImage(file=r"assets/items/longshot.png")
        longshot.image = longshot

        iceArrow = PhotoImage(file=r"assets/items/iceArrows.png")
        iceArrow.image = iceArrow

        faroresWind = PhotoImage(file=r"assets/items/faroresWind.png")
        faroresWind.image = faroresWind

        #row 2

        boomerang = PhotoImage(file=r"assets/items/boomerang.png")
        boomerang.image = boomerang

        lensOfTruth = PhotoImage(file=r"assets/items/lensOfTruth.png")
        lensOfTruth.image = lensOfTruth

        magicBeans = PhotoImage(file=r"assets/items/magicBeans.png")
        magicBeans.image = magicBeans

        megatonHammer = PhotoImage(file=r"assets/items/megatonHammer.png")
        megatonHammer.image = megatonHammer

        lightArrows = PhotoImage(file=r"assets/items/lightArrows.png")
        lightArrows.image = lightArrows

        naryusLove = PhotoImage(file=r"assets/items/naryusLove.png")
        naryusLove.image = naryusLove

        #menubar
        menubar = Menu(self.window)
        filemenu = Menu(menubar, tearoff=0)

        filemenu.add_command(label="Open", image=openicon, compound="left", command=get_path, accelerator="Ctrl+O")
        filemenu.add_command(label="Get info", image=infoicon, compound="left", command=get_info)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", image=exiticon, compound="left", command=alertbox)
        menubar.add_cascade(label="File", menu=filemenu)

        #Placement Item Track
        Label(self.window, image=worldMap, bg=self.bg).grid(row=0, rowspan=3, column=6, sticky=W + E + N + S)

        #Row = 0
        Label(self.window, image=deku_stick, bg=self.bg).grid(row=0, column=0,sticky=W)
        Label(self.window, image=deku_nut, bg=self.bg).grid(row=0, column=1, sticky=W)
        Label(self.window, image=bombs, bg=self.bg).grid(row=0, column=2, sticky=W)
        Label(self.window, image=bow, bg=self.bg).grid(row=0, column=3, sticky=W)
        Label(self.window, image=fireArrow, bg=self.bg).grid(row=0, column=4, sticky=W)
        Label(self.window, image=dinsFire, bg=self.bg).grid(row=0, column=5, sticky=W)

        #Row = 1
        Label(self.window, image=fairy_Slingshot, bg=self.bg).grid(row=1, column=0, sticky=W)
        Label(self.window, image=fairy_Ocarina, bg=self.bg).grid(row=1, column=1, sticky=W)
        Label(self.window, image=bombchus, bg=self.bg).grid(row=1, column=2, sticky=W)
        Label(self.window, image=hookshot, bg=self.bg).grid(row=1, column=3, sticky=W)
        Label(self.window, image=iceArrow, bg=self.bg).grid(row=1, column=4, sticky=W)
        Label(self.window, image=faroresWind, bg=self.bg).grid(row=1, column=5, sticky=W)

        # Row = 2
        Label(self.window, image=boomerang, bg=self.bg).grid(row=2, column=0, sticky=W)
        Label(self.window, image=lensOfTruth, bg=self.bg).grid(row=2, column=1, sticky=W)
        Label(self.window, image=magicBeans, bg=self.bg).grid(row=2, column=2, sticky=W)
        Label(self.window, image=megatonHammer, bg=self.bg).grid(row=2, column=3, sticky=W)
        Label(self.window, image=lightArrows, bg=self.bg).grid(row=2, column=4, sticky=W)
        Label(self.window, image=naryusLove, bg=self.bg).grid(row=2, column=5, sticky=W)

        # self.window.columnconfigure(0, weight=4)
        # self.window.columnconfigure(1, weight=1)

        self.window.config(menu=menubar)
