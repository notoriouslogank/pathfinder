class Dwarf:
    """Generate a stat sheet for a basic dwarf.

    Returns:
        obj: Dwarf
    """

    CON = 2
    WIS = 2
    CHA = -2
    darkvision = True
    weapons = ["battleaxes", "heavy picks", "warhammers"]
    languages = [
        "common",
        "dwarven",
        "CHOICE: giant, gnome, goblin, orc, terran, undercommon",
    ]

    def dwarf(self):
        """Create a dwarf.

        Returns:
            dict: Dwarf summary
        """
        attributes = [
            Dwarf.CON,
            Dwarf.WIS,
            Dwarf.CHA,
            Dwarf.darkvision,
            Dwarf.weapons,
            Dwarf.languages,
        ]

        self.CON = attributes[0]
        self.WIS = attributes[1]
        self.CHA = attributes[2]
        self.darkvision = attributes[3]
        self.weapons = attributes[4]
        self.languages = attributes[5]
        self.summary = {
            "CON": self.CON,
            "WIS": self.WIS,
            "CHA": self.CHA,
            "Darkvision": self.darkvision,
            "Weapon Proficiency": self.weapons,
            "Languages": self.languages,
        }
        return self.summary


class Halfling:
    DEX = 2
    CHA = 2
    STR = -2
    perception = 2
    weapons = ["slings"]
    languages = ["common", "halfling", "CHOICE: dwarven, elven, gnome, goblin"]

    def halfling(self):
        attributes = [
            Halfling.CHA,
            Halfling.DEX,
            Halfling.STR,
            Halfling.perception,
            Halfling.weapons,
            Halfling.languages,
        ]

        self.CHA = attributes[0]
        self.DEX = attributes[1]
        self.STR = attributes[2]
        self.perception = attributes[3]
        self.weapons = attributes[4]
        self.languages = attributes[5]
        self.summary = {
            "CHA": self.CHA,
            "DEX": self.DEX,
            "STR": self.STR,
            "Perception": self.perception,
            "Weapon Proficiency": self.weapons,
            "Languages": self.languages,
        }
        return self.summary


class Gnome:
    CON = 2
    CHA = 2
    STR = -2
    lowlight = True
    perception = 2
    weapons = ["none"]
    languages = [
        "common",
        "gnome",
        "sylvan",
        "CHOOSE: draconic, dwarven, elven, giant, goblin, orc",
    ]

    def gnome(self):
        attributes = [
            Gnome.CON,
            Gnome.CHA,
            Gnome.STR,
            Gnome.lowlight,
            Gnome.perception,
            Gnome.weapons,
            Gnome.languages,
        ]

        self.CON = attributes[0]
        self.CHA = attributes[1]
        self.STR = attributes[2]
        self.lowlight = attributes[3]
        self.perception = attributes[4]
        self.weapons = attributes[5]
        self.languages = attributes[6]
        self.summary = {
            "CON": self.CON,
            "WIS": self.CHA,
            "STR": self.STR,
            "Lowlight vision: ": self.lowlight,
            "Perception": self.perception,
            "Weapon Proficiency": self.weapons,
            "Languages": self.languages,
        }
        return self.summary


class Halforc:
    plusone = "+1 to any ability score"
    darkvision = True
    weapons = ["greataxes", "falchions"]
    languages = ["common", "orc", "CHOOSE: abyssal, draconic, giant, gnoll, goblin"]

    def halforc(self):

        attributes = [
            Halforc.plusone,
            Halforc.darkvision,
            Halforc.weapons,
            Halforc.languages,
        ]

        self.plusone = attributes[0]
        self.darkvision = attributes[1]
        self.weapons = attributes[2]
        self.languages = attributes[3]
        self.summary = {
            "Ability: ": self.plusone,
            "Darkvision": self.darkvision,
            "Weapon Proficiency": self.weapons,
            "Languages": self.languages,
        }
        return self.summary


class Halfelf:
    plusone = "+1 to any ability score"
    darkvision = True
    weapons = ["none"]
    languages = ["common", "elven", "CHOOSE: any"]

    def halfelf(self):
        attributes = [
            Halfelf.plusone,
            Halfelf.darkvision,
            Halfelf.weapons,
            Halfelf.languages,
        ]

        self.plusone = attributes[0]
        self.darkvision = attributes[1]
        self.weapons = attributes[2]
        self.languages = attributes[3]
        self.summary = {
            "Ability": self.plusone,
            "Darkvision": self.darkvision,
            "Weapon Proficiency": self.weapons,
            "Languages": self.languages,
        }


def DWARF():
    """Create the summary info."""
    Dwarf.dwarf()
    info = ("RACE: " + "DWARF", race.summary)
    print(info)


def GNOME():
    Gnome.gnome()
    info = ("RACE: " + "GNOME", race.summary)
    print(info)


def HALFLING():
    Halfling.halfling()
    info = ("RACE: " + "HALFLING", race.summary)
    print(info)


def HALFORC():
    race.halforc()
    info = ("RACE: " + "HALFORC", race.summary)
    print(info)


def HALFELF():
    Halfelf.halfelf()
    info = ("RACE: " + "HALFELF", race.summary)
    print(info)
