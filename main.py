# import
import tkinter
from tkinter import *
from tkinter import filedialog

import json


class Dungeon:
    name: str
    boss_key: bool = False
    compass: bool = False
    map: bool = False

    def parse_bin(self, binary):
        print(binary)
        print(bin(binary))
        if bin(binary)[-1] == '1':
            self.boss_key = True
        else:
            self.boss_key = False

        if bin(binary >> 1)[-1] == '1':
            self.compass = True
        else:
            self.compass = False

        if bin(binary >> 2)[-1] == '1':
            self.map = True
        else:
            self.map = False

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Name: ' + self.name + ' Boss Key: ' + str(self.boss_key) + ' Compass: ' + str(
            self.compass) + ' Map: ' + str(self.map)

    def __eq__(self, other: str):
        return self.name == other


class Save:
    path: str
    doubleMagic: bool = False
    doubleDefense: bool = False
    magic: bool = False

    dungeons: [Dungeon] = []

    def make_data(self, data):
        self.doubleDefense = data['isDoubleDefenseAcquired']
        self.doubleMagic = data['isDoubleMagicAcquired']

        self.parse_dungeons(data['inventory']['dungeonItems'])

        print('Double Defense: ' + str(self.doubleDefense))
        print('Double Magic: ' + str(self.doubleMagic))

        # print(''.join(str(dungeon) for dungeon in self.dungeons))
        for dungeon in self.dungeons:
            print(dungeon)

    def parse_dungeons(self, dungeons):
        self.create_or_update_dungeon('Deku Tree', dungeons[0])
        self.create_or_update_dungeon('Dodongo Cavern', dungeons[1])
        self.create_or_update_dungeon('Jabu-Jabu', dungeons[2])
        self.create_or_update_dungeon('Forest Temple', dungeons[3])
        self.create_or_update_dungeon('Fire Temple', dungeons[4])
        self.create_or_update_dungeon('Water Temple', dungeons[5])
        self.create_or_update_dungeon('Spirit Temple', dungeons[6])
        self.create_or_update_dungeon('Shadow Temple', dungeons[7])
        self.create_or_update_dungeon('Bottom of the Well', dungeons[8])
        self.create_or_update_dungeon('Ice Cavern', dungeons[9])
        self.create_or_update_dungeon('Ganon Tower', dungeons[10])
        self.create_or_update_dungeon('Gerudo Training Ground', dungeons[11])
        self.create_or_update_dungeon('Thieves Hideout', dungeons[12])
        self.create_or_update_dungeon('Inside Ganon Castle', dungeons[13])
        self.create_or_update_dungeon('Ganon Tower (Collapsing)', dungeons[14])
        self.create_or_update_dungeon('Inside Ganon Castle (collapsing)', dungeons[15])
        self.create_or_update_dungeon('Treasure Box Shop', dungeons[16])
        self.create_or_update_dungeon('Gohma Lair', dungeons[17])
        self.create_or_update_dungeon('King Dodongo Lair', dungeons[18])
        self.create_or_update_dungeon('Barinade Lair', dungeons[19])

    def create_or_update_dungeon(self, dungeon_name: str, binary: int):
        if dungeon_name in self.dungeons:
            print('Has ' + dungeon_name)
        else:
            self.dungeons.append(Dungeon(dungeon_name))

        index = self.dungeons.index(dungeon_name)

        self.dungeons[index].parse_bin(binary)

    def get_info(self):
        with open(self.path, "r") as saveFile:
            data = saveFile.read()
        data = json.loads(data)
        self.make_data(data['sections']['base']['data'])


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
            self.save.get_info()

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
