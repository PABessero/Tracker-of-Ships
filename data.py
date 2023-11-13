import json
import tkinter

from PIL import ImageTk, Image


class Dungeon:
    name: str
    boss_key: bool = False
    compass: bool = False
    map: bool = False
    small_keys: int = 0

    image_path: str

    def parse_bin(self, binary):
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

    def __init__(self, name, image_path: str):
        self.name = name
        self.image_path = image_path

    def __str__(self):
        return 'Name: ' + self.name + '\n Boss Key: ' + str(self.boss_key) + '\n Compass: ' + str(
            self.compass) + '\n Map: ' + str(self.map) + '\n Small Keys: ' + str(self.small_keys)

    def __eq__(self, other: str):
        return self.name == other


class Position:
    column: int = 0
    row: int = 0
    sticky = tkinter.W

    def __init__(self, column: int = 0, row: int = 0, sticky=tkinter.W):
        self.column = column
        self.row = row
        self.sticky = sticky


class ShownItem(object):
    name: str = ''
    image_path: str = ''
    obtained: bool = False
    position: Position = Position()

    # label: tkinter.Label

    def update_background_color(self, bg):
        if hasattr(self, 'label'):
            self.label.configure(bg=bg)

    def set_obtained(self, obtained):
        self.obtained = obtained
        if self.image_path != '':
            self.image = ImageTk.PhotoImage(Image.open(self.image_path))
            if not self.obtained:
                colored = Image.open(self.image_path)
                colored.load()
                alpha = colored.split()[-1]
                img_gray = colored.convert("L").convert("RGB")
                img_gray.putalpha(alpha)
                self.image = ImageTk.PhotoImage(img_gray)

    def __init__(self, name: str, image_path: str = ''):
        self.name = name
        self.image_path = image_path

        if self.image_path != '':
            self.image = ImageTk.PhotoImage(Image.open(self.image_path))

    def __str__(self):
        return 'Item: ' + self.name + (" (Y)" if self.obtained else " (N)")

    def __eq__(self, other: str):
        return self.name == other


class Equipment(ShownItem):

    def __init__(self, name: str, image_path: str = ''):
        super().__init__(name, image_path)


class Item(ShownItem):

    def __init__(self, name: str, image_path: str = '', position: Position = Position()):
        super().__init__(name, image_path)
        self.name = name
        self.image_path = image_path
        self.position = position

        if self.image_path != '':
            self.image = ImageTk.PhotoImage(Image.open(self.image_path))


class Save:
    path: str = ''
    doubleMagic: bool = False
    doubleDefense: bool = False
    magic: bool = False

    last_update: int = 0

    dungeons: [Dungeon] = []
    equipments: [Equipment] = []
    items: [Item] = []

    def make_data(self, data):
        self.doubleDefense = data['isDoubleDefenseAcquired']
        self.doubleMagic = data['isDoubleMagicAcquired']

        self.parse_dungeons(data['inventory']['dungeonItems'], data['inventory']['dungeonKeys'])
        self.parse_equipment(data['inventory']['equipment'])
        self.parse_inventory(data['inventory']['items'])

    def parse_dungeons(self, dungeons, dungeon_keys):
        self.create_or_update_dungeon('Deku Tree', dungeons[0], dungeon_keys[0])
        self.create_or_update_dungeon('Dodongo Cavern', dungeons[1], dungeon_keys[1])
        self.create_or_update_dungeon('Jabu-Jabu', dungeons[2], dungeon_keys[2])
        self.create_or_update_dungeon('Forest Temple', dungeons[3], dungeon_keys[3])
        self.create_or_update_dungeon('Fire Temple', dungeons[4], dungeon_keys[4])
        self.create_or_update_dungeon('Water Temple', dungeons[5], dungeon_keys[5])
        self.create_or_update_dungeon('Spirit Temple', dungeons[6], dungeon_keys[6])
        self.create_or_update_dungeon('Shadow Temple', dungeons[7], dungeon_keys[7])
        self.create_or_update_dungeon('Bottom of the Well', dungeons[8], dungeon_keys[8])
        self.create_or_update_dungeon('Ice Cavern', dungeons[9], dungeon_keys[9])
        self.create_or_update_dungeon('Ganon Tower', dungeons[10], dungeon_keys[10])
        self.create_or_update_dungeon('Gerudo Training Ground', dungeons[11], dungeon_keys[11])
        self.create_or_update_dungeon('Thieves Hideout', dungeons[12], dungeon_keys[12])
        self.create_or_update_dungeon('Inside Ganon Castle', dungeons[13], dungeon_keys[13])
        self.create_or_update_dungeon('Ganon Tower (Collapsing)', dungeons[14], dungeon_keys[14])
        self.create_or_update_dungeon('Inside Ganon Castle (collapsing)', dungeons[15], dungeon_keys[15])
        self.create_or_update_dungeon('Treasure Box Shop', dungeons[16], dungeon_keys[16])
        self.create_or_update_dungeon('Gohma Lair', dungeons[17], dungeon_keys[17])
        self.create_or_update_dungeon('King Dodongo Lair', dungeons[18], dungeon_keys[18])
        self.create_or_update_dungeon('Barinade Lair', dungeons[19])

    def parse_equipment(self, equipment: int):
        self.create_or_update_equipment('Kokiri Sword', bin(equipment >> 0)[-1],
                                        r'assets/items/equipKokiriSword.png', Position(0, 4, tkinter.W))
        self.create_or_update_equipment('Master Sword', bin(equipment >> 1)[-1],
                                        r'assets/items/equipMasterSword.png', Position(1, 4, tkinter.W))
        self.create_or_update_equipment('Giant Knife & Biggoron', bin(equipment >> 2)[-1],
                                        r'assets/items/equipBiggoronsSword.png', Position(2, 4, tkinter.W))
        # self.create_or_update_equipment('Goron Sword (Broken)', bin(equipment >> 3)[-1],
        #                                 r'assets/items/equipBrokenKnife.png', Position(3, 4, tkinter.W))
        self.create_or_update_equipment('Deku Shield', bin(equipment >> 4)[-1],
                                        r'assets/items/equipDekuShield.png', Position(3, 4, tkinter.W))
        self.create_or_update_equipment('Hylian Shield', bin(equipment >> 5)[-1],
                                        r'assets/items/equipHylianShield.png', Position(4, 4, tkinter.W))
        self.create_or_update_equipment('Mirror Shield', bin(equipment >> 6)[-1],
                                        r'assets/items/equipMirrorShield.png', Position(5, 4, tkinter.W))
        self.create_or_update_equipment('Kokiri Tunic', bin(equipment >> 8)[-1],
                                        r'assets/items/equipKokiriTunic.png', Position(0, 5, tkinter.W))
        self.create_or_update_equipment('Goron Tunic', bin(equipment >> 9)[-1],
                                        r'assets/items/equipGoronTunic.png', Position(1, 5, tkinter.W))
        self.create_or_update_equipment('Zora Tunic', bin(equipment >> 10)[-1],
                                        r'assets/items/equipZoraTunic.png', Position(2, 5, tkinter.W))
        self.create_or_update_equipment('Kokiri Boots', bin(equipment >> 12)[-1],
                                        r'assets/items/equipKokiriBoots.png', Position(3, 5, tkinter.W))
        self.create_or_update_equipment('Iron Boots', bin(equipment >> 13)[-1],
                                        r'assets/items/equipIronBoots.png', Position(4, 5, tkinter.W))
        self.create_or_update_equipment('Hover Boots', bin(equipment >> 14)[-1],
                                        r'assets/items/equipHoverBoots.png', Position(5, 5, tkinter.W))

    def parse_inventory(self, items: [int]):
        # if bin(items[0] >> 1)[-1] == '0'
        print(bin(items[0]))
        self.create_or_update_item("Deku Stick", "0" if items[0] == 0 else "1",
                                   r'assets/items/dekuStick.png', Position(0, 0, tkinter.W))
        self.create_or_update_item("Deku Nut", "0" if items[1] == 1 else "1",
                                   r'assets/items/dekuNut.png', Position(1, 0, tkinter.W))
        self.create_or_update_item("Bomb", "0" if items[2] == 2 else "1",
                                   r'assets/items/bombs.png', Position(2, 0, tkinter.W))
        self.create_or_update_item("Fairy Bow", "0" if items[3] == 3 else "1",
                                   r'assets/items/bow.png', Position(3, 0, tkinter.W))
        self.create_or_update_item("Fire Arrow", "0" if items[4] == 4 else "1",
                                   r'assets/items/fireArrow.png', Position(4, 0, tkinter.W))
        self.create_or_update_item("Din's Fire", "0" if items[5] == 5 else "1",
                                   r'assets/items/dinsFire.png', Position(5, 0, tkinter.W))

        self.create_or_update_item("Fairy Slingshot", "0" if items[6] == 6 else "1",
                                   r'assets/items/fairySlingshot.png', Position(0, 1, tkinter.W))
        if items[7] == 8:
            self.create_or_update_item("Ocarina of Time", "0" if items[7] == 8 else "1",
                                       r'assets/items/ocarinaOfTime.png', Position(1, 1, tkinter.W))
            self.delete_item("Fairy Ocarina")
        else:
            self.create_or_update_item("Fairy Ocarina", "0" if items[7] == 7 else "1",
                                       r'assets/items/fairyOcarina.png', Position(1, 1, tkinter.W))
            self.delete_item("Ocarina of Time")
        self.create_or_update_item("Bombchu", "0" if items[8] == 9 else "1",
                                   r'assets/items/bombchus.png', Position(2, 1, tkinter.W))
        if items[9] == 11:
            self.create_or_update_item("Longshot", "0" if items[9] == 11 else "1",
                                       r'assets/items/longshot.png', Position(3, 1, tkinter.W))
            self.delete_item("Hookshot")
        else:
            self.create_or_update_item("Hookshot", "0" if items[9] == 10 else "1",
                                       r'assets/items/hookshot.png', Position(3, 1, tkinter.W))
            self.delete_item("Longshot")
        self.create_or_update_item("Ice Arrow", "0" if items[10] == 12 else "1",
                                   r'assets/items/iceArrows.png', Position(4, 1, tkinter.W))
        self.create_or_update_item("Farore's Wind", "0" if items[11] == 13 else "1",
                                   r'assets/items/faroresWind.png', Position(5, 1, tkinter.W))

        self.create_or_update_item("Boomerang", "0" if items[12] == 14 else "1",
                                   r'assets/items/boomerang.png', Position(0, 2, tkinter.W))
        self.create_or_update_item("Lens of Truth", "0" if items[13] == 15 else "1",
                                   r'assets/items/lensOfTruth.png', Position(1, 2, tkinter.W))
        self.create_or_update_item("Magic Bean", "0" if items[14] == 16 else "1",
                                   r'assets/items/magicBeans.png', Position(2, 2, tkinter.W))
        self.create_or_update_item("Megaton Hammer", "0" if items[15] == 17 else "1",
                                   r'assets/items/megatonHammer.png', Position(3, 2, tkinter.W))
        self.create_or_update_item("Light Arrow", "0" if items[16] == 18 else "1",
                                   r'assets/items/lightArrows.png', Position(4, 2, tkinter.W))
        self.create_or_update_item("Nayru's Love", "0" if items[17] == 19 else "1",
                                   r'assets/items/nayrusLove.png', Position(5, 2, tkinter.W))

        #Bouble For pour les 4 slots a bouteille
        slots = 18
        for column in range(4):
            self.delete_item("Bottle Empty" + str(slots))
            self.delete_item("Red Potion" + str(slots))
            self.delete_item("Green Potion" + str(slots))
            self.delete_item("Blue Potion" + str(slots))
            self.delete_item("Bottled Fairy" + str(slots))
            self.delete_item("Fish" + str(slots))
            self.delete_item("Bottle Lon Lon Milk" + str(slots))
            self.delete_item("Ruto's Letter" + str(slots))
            self.delete_item("Blue Fire" + str(slots))
            self.delete_item("Bug" + str(slots))
            self.delete_item("Big Poe" + str(slots))
            self.delete_item("Bottle Lon Lon Milk Half" + str(slots))
            self.delete_item("Poe" + str(slots))
            if items[slots] == 20 or items[slots] == 255:
                self.create_or_update_item("Bottle Empty" + str(slots), "0" if items[slots] == 20 else "1",
                                        r'assets/items/bottleEmpty.png', Position(column, 3, tkinter.W))

            elif items[slots] == 21:
                self.create_or_update_item("Red Potion" + str(slots), "0" if items[slots] == 21 else "1",
                                           r'assets/items/bottleRedPotion.png', Position(column, 3, tkinter.W))

            elif items[slots] == 22:
                self.create_or_update_item("Green Potion" + str(slots), "0" if items[slots] == 22 else "1",
                                           r'assets/items/bottleGreenPotion.png', Position(column, 3, tkinter.W))

            elif items[slots] == 23:
                self.create_or_update_item("Blue Potion" + str(slots), "0" if items[slots] == 23 else "1",
                                           r'assets/items/bottleBluePotion.png', Position(column, 3, tkinter.W))

            elif items[slots] == 24:
                self.create_or_update_item("Bottled Fairy" + str(slots), "0" if items[slots] == 24 else "1",
                                           r'assets/items/bottleBottledFairy.png', Position(column, 3, tkinter.W))

            elif items[slots] == 25:
                self.create_or_update_item("Fish" + str(slots), "0" if items[slots] == 25 else "1",
                                           r'assets/items/bottleFish.png', Position(column, 3, tkinter.W))

            elif items[slots] == 26:
                self.create_or_update_item("Bottle Lon Lon Milk" + str(slots), "0" if items[slots] == 26 else "1",
                                           r'assets/items/bottleLonLonMilk.png', Position(column, 3, tkinter.W))

            elif items[slots] == 27:
                self.create_or_update_item("Ruto's Letter" + str(slots), "0" if items[slots] == 27 else "1",
                                           r'assets/items/bottleLetter.png', Position(column, 3, tkinter.W))

            elif items[slots] == 28:
                self.create_or_update_item("Blue Fire" + str(slots), "0" if items[slots] == 28 else "1",
                                           r'assets/items/bottleBlueFire.png', Position(0, 3, tkinter.W))

            elif items[slots] == 29:
                self.create_or_update_item("Bug" + str(slots), "0" if items[slots] == 29 else "1",
                                           r'assets/items/bottleBug.png', Position(column, 3, tkinter.W))

            elif items[slots] == 30:
                self.create_or_update_item("Big Poe" + str(slots), "0" if items[slots] == 30 else "1",
                                           r'assets/items/bottleBigPoe.png', Position(column, 3, tkinter.W))

            elif items[slots] == 31:
                self.create_or_update_item("Bottle Lon Lon Milk Half" + str(slots), "0" if items[slots] == 31 else "1",
                                           r'assets/items/bottleLonLonMilkHalf.png', Position(column, 3, tkinter.W))

            elif items[slots] == 32:
                self.create_or_update_item("Poe" + str(slots), "0" if items[slots] == 32 else "1",
                                           r'assets/items/bottlePoe.png', Position(column, 3, tkinter.W))

            slots = slots + 1

    def create_or_update_dungeon(self, dungeon_name: str, binary: int, dungeon_keys: int = 0, image_path: str = ''):
        if dungeon_name in self.dungeons:
            pass
        else:
            self.dungeons.append(Dungeon(dungeon_name, ''))

        index = self.dungeons.index(dungeon_name)

        self.dungeons[index].parse_bin(binary)
        self.dungeons[index].small_keys = dungeon_keys

    def create_or_update_equipment(self, equipment_name, obtained: str = "0",
                                   image_path: str = "", position: Position = Position()):
        if equipment_name in self.equipments:
            pass
        else:
            self.equipments.append(Equipment(equipment_name))

        index = self.equipments.index(equipment_name)

        self.equipments[index].position = position
        self.equipments[index].image_path = image_path

        if obtained == "0":
            self.equipments[index].set_obtained(False)
        else:
            self.equipments[index].set_obtained(True)

    def create_or_update_item(self, item_name, obtained: str = "0",
                              image_path: str = "", position: Position = Position()):
        print(item_name)
        print(obtained)
        if item_name in self.items:
            pass
        else:
            self.items.append(Item(item_name, image_path=image_path, position=position))

        index = self.items.index(item_name)

        if obtained == "1":
            self.items[index].set_obtained(False)
        else:
            self.items[index].set_obtained(True)

    def delete_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)

    def get_info(self):
        with open(self.path, "r") as saveFile:
            data = saveFile.read()
        data = json.loads(data)
        self.make_data(data['sections']['base']['data'])
