import json


class Dungeon:
    name: str
    boss_key: bool = False
    compass: bool = False
    map: bool = False

    image_path: str

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

    def __init__(self, name, image_path: str):
        self.name = name
        self.image_path = image_path

    def __str__(self):
        return 'Name: ' + self.name + ' Boss Key: ' + str(self.boss_key) + ' Compass: ' + str(
            self.compass) + ' Map: ' + str(self.map)

    def __eq__(self, other: str):
        return self.name == other


class Equipment:
    pass


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

    def parse_equipment(self, equipment):
        pass

    def create_or_update_dungeon(self, dungeon_name: str, binary: int, image_path: str = ''):
        if dungeon_name in self.dungeons:
            print('Has ' + dungeon_name)
        else:
            self.dungeons.append(Dungeon(dungeon_name, ''))

        index = self.dungeons.index(dungeon_name)

        self.dungeons[index].parse_bin(binary)

    def get_info(self):
        with open(self.path, "r") as saveFile:
            data = saveFile.read()
        data = json.loads(data)
        self.make_data(data['sections']['base']['data'])
