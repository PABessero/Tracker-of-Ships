import os
import time
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor

from data import Save


class App:
    _bg = "black"
    font = "Arial"
    fg = "white"
    width = 600
    height = 600

    window = Tk()

    equipment_parent = window

    save: Save = Save()

    canvas: tkinter.Canvas

    @property
    def bg(self):
        return self._bg

    @bg.setter
    def bg(self, value):
        self._bg = value

        for callback in self._bg_observers:
            callback(self._bg)

    def bind_to(self, callback):
        self._bg_observers.append(callback)

    def make_equipment_images(self, parent=equipment_parent):
        for equipment in self.save.equipments:
            if equipment.image_path != '':
                # if not hasattr(equipment, 'label'):
                equipment.label = Label(parent, image=equipment.image, bg=self.bg)
                self.bind_to(equipment.update_background_color)
                equipment.label.grid(row=equipment.position.row,
                                     column=equipment.position.column,
                                     sticky=equipment.position.sticky)

    def popout_equipment(self):
        window = EquipmentWindow(self)
        self.equipment_parent = window
        self.get_info()

    def update_save(self):
        if self.save.path != '':
            if self.save.last_update != os.stat(self.save.path).st_mtime:
                time.sleep(0.1)
                self.get_info()
                self.save.last_update = os.stat(self.save.path).st_mtime
        self.window.after(10, self.update_save)

    def alert_box(self):
        if askyesno('Warning', 'Are you sure you want to do this?'):
            self.window.destroy()

    def pick_background_color(self):
        self.bg = askcolor(self.bg, title="Test")[1] or "#0000a0"
        self.window.configure(bg=self.bg)
        self.tmp_item_grid()

    def tmp_item_grid(self):

        # Placement Item Track
        Label(self.window, image=self.worldMap, bg=self.bg).grid(row=0, rowspan=11, column=8, columnspan=10, sticky=SE)
        self.window.columnconfigure(8, weight=10)

        # Row = 0
        Label(self.window, image=self.deku_stick, bg=self.bg).grid(row=0, column=0, sticky=W)
        Label(self.window, image=self.deku_nut, bg=self.bg).grid(row=0, column=1, sticky=W)
        Label(self.window, image=self.bombs, bg=self.bg).grid(row=0, column=2, sticky=W)
        Label(self.window, image=self.bow, bg=self.bg).grid(row=0, column=3, sticky=W)
        Label(self.window, image=self.fireArrow, bg=self.bg).grid(row=0, column=4, sticky=W)
        Label(self.window, image=self.dinsFire, bg=self.bg).grid(row=0, column=5, sticky=W)

        # Row = 1
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

        # Row = 3

        Label(self.window, image=self.bottleEmpty, bg=self.bg).grid(row=3, column=0, sticky=W)
        Label(self.window, image=self.bottleEmpty, bg=self.bg).grid(row=3, column=1, sticky=W)
        Label(self.window, image=self.bottleEmpty, bg=self.bg).grid(row=3, column=2, sticky=W)
        Label(self.window, image=self.bottleEmpty, bg=self.bg).grid(row=3, column=3, sticky=W)
        Label(self.window, image=self.lightArrows, bg=self.bg).grid(row=3, column=4, sticky=W)
        Label(self.window, image=self.naryusLove, bg=self.bg).grid(row=3, column=5, sticky=W)

    def load_image_icon(self):
        # variable image
        # Image Menu Bar
        self.openicon = PhotoImage(file="assets/other/folder.png")
        self.openicon.image = self.openicon

        self.infoicon = PhotoImage(file="assets/other/info.png")
        self.infoicon.image = self.infoicon

        self.exiticon = PhotoImage(file="assets/other/logout.png")
        self.exiticon.image = self.exiticon

        self.popout_icon = PhotoImage(file=r"assets/other/popout.png")
        self.popout_icon.image = self.popout_icon

        self.popout_equipment_icon = PhotoImage(file=r"assets/other/popoutEquipment.png")
        self.popout_equipment_icon.image = self.popout_equipment_icon

        self.option_icon = PhotoImage(file=r"assets/other/Option.png")
        self.option_icon.image = self.option_icon

        self.background_color_option_icon = PhotoImage(file=r"assets/other/backgroundColorOption.png")
        self.background_color_option_icon.image = self.background_color_option_icon

    def load_image_item(self):
        # Image Items
        # Row 0
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

        # Row 1
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

        # row 2

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

        # row 3

        self.bottleEmpty = PhotoImage(file=r"assets/items/bottleEmpty.png")
        self.bottleEmpty.image = self.bottleEmpty

        self.bottleLetter = PhotoImage(file=r"assets/items/bottleLetter.png")
        self.bottleLetter.image = self.bottleLetter

        self.bottleRedPotion = PhotoImage(file=r"assets/items/bottleRedPotion.png")
        self.bottleRedPotion.image = self.bottleRedPotion

        self.bottleGreenPotion = PhotoImage(file=r"assets/items/bottleGreenPotion.png")
        self.bottleGreenPotion.image = self.bottleGreenPotion

        self.bottleBluePotion = PhotoImage(file=r"assets/items/bottleBluePotion.png")
        self.bottleBluePotion.image = self.bottleBluePotion

        self.bottleFish = PhotoImage(file=r"assets/items/bottleFish.png")
        self.bottleFish = self.bottleFish

        self.bottleBug = PhotoImage(file=r"assets/items/bottleBug.png")
        self.bottleBug = self.bottleBug

        self.bottleLonLonMilk = PhotoImage(file=r"assets/items/bottleLonLonMilk.png")
        self.bottleLonLonMilk = self.bottleLonLonMilk

        self.bottleLonLonMilkHalf = PhotoImage(file=r"assets/items/bottleLonLonMilkHalf.png")
        self.bottleLonLonMilkHalf = self.bottleLonLonMilkHalf

        self.bottleBlueFire = PhotoImage(file=r"assets/items/bottleBlueFire.png")
        self.bottleBlueFire = self.bottleBlueFire

        self.bottleBigPoe = PhotoImage(file=r"assets/items/bottleBigPoe.png")
        self.bottleBigPoe = self.bottleBigPoe

        self.bottlePoe = PhotoImage(file=r"assets/items/bottlePoe.png")
        self.bottlePoe = self.bottlePoe

        self.adultPocketEgg = PhotoImage(file=r"assets/items/adultPocketEgg.png")
        self.adultPocketEgg = self.adultPocketEgg

        self.adultPocketCucco = PhotoImage(file=r"assets/items/adultPocketCucco.png")
        self.adultPocketCucco = self.adultPocketCucco

        self.adultCojiro = PhotoImage(file=r"assets/items/adultCojiro.png")
        self.adultCojiro = self.adultCojiro

        self.adultOddMushroom = PhotoImage(file=r"assets/items/adultOddMushroom.png")
        self.adultOddMushroom = self.adultOddMushroom

        self.adultOddPotion = PhotoImage(file=r"assets/items/adultOddPotion.png")
        self.adultOddPotion = self.adultOddPotion

        self.adultPoachersSaw = PhotoImage(file=r"assets/items/adultPoachersSaw.png")
        self.adultPoachersSaw = self.adultPoachersSaw

        self.adultPocketEgg = PhotoImage(file=r"assets/items/adultPocketEgg.png")
        self.adultPocketEgg = self.adultPocketEgg

        self.adultPocketEgg = PhotoImage(file=r"assets/items/adultPocketEgg.png")
        self.adultPocketEgg = self.adultPocketEgg

        self.adultPocketEgg = PhotoImage(file=r"assets/items/adultPocketEgg.png")
        self.adultPocketEgg = self.adultPocketEgg

        self.adultPocketEgg = PhotoImage(file=r"assets/items/adultPocketEgg.png")
        self.adultPocketEgg = self.adultPocketEgg

        self.adultPocketEgg = PhotoImage(file=r"assets/items/adultPocketEgg.png")
        self.adultPocketEgg = self.adultPocketEgg
    # noinspection PyTypeChecker

    def get_info(self):
        if self.save.path != "":
            self.save.get_info()
            self.make_equipment_images(parent=self.equipment_parent)

    def get_path(self):
        file_path = tkinter.filedialog.askopenfilename()
        print("Path: " + file_path)
        if ".sav" in file_path:
            self.save.path = file_path
            self.save.last_update = os.stat(file_path).st_mtime
            self.get_info()
        else:
            print("File doesnt match the right extension")

    def __init__(self, title: str, geometry: str):

        self._bg_observers = []

        self.window.title(title)
        self.window.geometry(geometry)
        self.window.minsize(480, 360)
        self.window.iconbitmap("assets/other/enhancedDefence.ico")
        self.window.config(background=self.bg)

        self.window.after(10, self.update_save)

        self.load_image_icon()
        self.load_image_item()

        # menubar
        menubar = Menu(self.window)
        filemenu = Menu(menubar, tearoff=0)

        filemenu.add_command(label="Open", image=self.openicon, compound="left", command=self.get_path,
                             accelerator="Ctrl+O")
        filemenu.add_command(label="Get info", image=self.infoicon, compound="left", command=self.get_info)

        sub_menu_popout = Menu(filemenu, tearoff=0)
        filemenu.add_cascade(label="Popout", menu=sub_menu_popout, image=self.popout_icon, compound="left")
        sub_menu_popout.add_command(label="Popout Equipment", image=self.popout_equipment_icon, compound="left",
                                    command=self.popout_equipment)

        sub_menu_option = Menu(filemenu, tearoff=0)
        filemenu.add_cascade(label="Option", menu=sub_menu_option, image=self.option_icon, compound="left")
        sub_menu_option.add_command(label="Background Color Option", image=self.background_color_option_icon,
                                    compound="left", command=self.pick_background_color)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", image=self.exiticon, compound="left", command=self.alert_box)

        menubar.add_cascade(label="File", menu=filemenu)

        self.tmp_item_grid()

        # self.window.columnconfigure(0, weight=4)
        # self.window.columnconfigure(1, weight=1)

        self.window.config(menu=menubar)


class Window(tkinter.Toplevel):
    app: App

    def __init__(self, parent, title: str = 'Test Window'):
        self.app = parent
        super().__init__(parent.window)

        self.geometry('300x100')
        self.title(title)


class EquipmentWindow(Window):
    def __init__(self, parent):
        super().__init__(parent, "Equipment Window")

    def destroy(self):
        self.app.equipment_parent = self.app.window
        self.app.get_info()
        super().destroy()


class ItemWindow(Window):
    def __init__(self, parent):
        super().__init__(parent, "Item Window")

    def destroy(self):
        self.app.item_parent = self.app.window
        self.app.get_info()
        super().destroy()
