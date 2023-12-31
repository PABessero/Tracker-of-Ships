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

    item_parent = window

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

    def make_images(self, parent=window, show_array=None):
        if show_array is None:
            show_array = []
        for show_item in show_array:
            if show_item.image_path != '':
                show_item.label = Label(parent, image=show_item.image, bg=self.bg)
                self.bind_to(show_item.update_background_color)
                show_item.label.grid(row=show_item.position.row,
                                     column=show_item.position.column,
                                     sticky=show_item.position.sticky)

    def popout_equipment(self):
        if self.equipment_parent == self.window:
            window = EquipmentWindow(self, "320x110")
            self.equipment_parent = window
        else:
            self.equipment_parent.destroy()
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
        # self.tmp_item_grid()

    def tmp_item_grid(self):

        # Placement Item Track
        Label(self.window, image=self.worldMap, bg=self.bg).grid(row=0, rowspan=11, column=8, columnspan=10, sticky=SE)
        Label(self.window, image=self.miniMap, bg=self.bg).grid(row=12, rowspan=3, column=8, columnspan=5, sticky=SE)
        self.window.columnconfigure(8, weight=10)

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
        self.worldMap = PhotoImage(file=r"assets/maps/worldMap.png")
        self.worldMap.image = self.worldMap

        self.miniMap = PhotoImage(file="assets/maps/mapGF.png")
        self.miniMap.image = self.miniMap

    # noinspection PyTypeChecker

    def get_info(self):
        if self.save.path != "":
            self.save.get_info()
            self.make_images(self.equipment_parent, self.save.equipments)
            self.make_images(self.equipment_parent, self.save.items)
            if self.save.current_zone is not None:
                print("Test")
                self.miniMap = PhotoImage(file=self.save.current_zone.image_path)
                self.miniMap.image = self.miniMap
                Label(self.window, image=self.miniMap, bg=self.bg).grid(row=12, rowspan=3, column=8, columnspan=5,
                                                                        sticky=SE)

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

    def __init__(self, parent, title: str = 'Test Window', geometry="300x100"):
        self.app = parent
        super().__init__(parent.window)

        self.geometry(geometry)
        self.title(title)


class EquipmentWindow(Window):
    def __init__(self, parent, geometry="300x100"):
        super().__init__(parent, "Equipment Window", geometry)
        self.attributes("-topmost", True)
        self.configure(bg=parent.bg)

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
