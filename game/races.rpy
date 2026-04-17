
init 1 python:
    class raceDetails:
        def __init__(self, raceName, raceHeight, raceSkillBonus, racialTraits):
            self.raceName = raceName
            #(minHeight,averageHeight,maxHeight) the whole number represents feet and the decimal represents inches
            self.raceHeight = raceHeight
            #A list of tuples, each tuple has two entries first being the skill name and the second is how much it is increased by.
            #"skillPoints" can also be inputted for the first slot of the tuple to indicate that the character gets extra skill points.
            self.raceSkillBonus = raceSkillBonus
            self.racialTraits = racialTraits
        def getRaceHeight(self):
            return "Please input a height between [self.raceHeight[0]] and [self.raceHeight[2]]:"
        def getRaceHeightAvg(self):
            return self.raceHeight[1]
    
    
    human = raceDetails("human",
        ("4.6","5.5","6.4"),
        [("skillPoints", 20)],
        "") #20
    shifter = raceDetails("shifter",
        ("4.6","5.5","6.4"),
        [("charm", 5), ("performance", 5), ("skillPoints", 10)],
        "") #20
    elf = raceDetails("elf",
        ("4.3","5.0","5.10"),
        [("dexterty", 4), ("intellect", 3), ("willPower", 3), ("insight", 2), ("perception", 2), ("stealth", 2), ("medicine", 2), ("survival", 1), ("lore", 1)],
        "") #20
    halfElf = raceDetails("half-elf",
        ("4.4","5.2","6.1"),
        [("dexterty", 3), ("intellect", 3), ("willPower", 2), ("perception", 2), ("stealth", 2), ("insight", 1), ("skillPoints", 7)],
        "") #20
    dwarf = raceDetails("dwarf",
        ("3.11","4.6","5.2"),
        [("willPower", 5), ("craftsmenship", 5), ("strength", 4), ("strategy", 3), ("constitution", 3), ("insight", 2), ("lore", 1), ("survival", 1), ("performance", -1), ("charm", -1), ("dexterity", -2)],
        "") #24-4
    orc = raceDetails("orc",
        ("4.9","5.9","6.10"),
        [("strength", 5), ("constitution", 5), ("intimidation", 4), ("survival", 3), ("willPower", 3), ("perception", 2), ("stealth", 1), ("medicine", 1), ("lore", 1), ("performance", -1), ("charm", -2), ("lockPicking", -2)],
        "") #25-5
    halfling = raceDetails("halfling",
        ("2.5","3.1","3.8"),
        [("dexterity", 5), ("charm", 4), ("willPower", 3), ("stealth", 3), ("slightOfHand", 3), ("lockPicking", 2), ("craftsmenship", 2),("skillPoints", 6), ("intimidation", -4), ("strength", -4)],
        "") #28-8
    arenae = raceDetails("arenae",
        ("4.2","5.2","6.3"),
        [("charm", 5), ("intellect", 4), ("medicine", 4), ("insight", 4), ("dexterty", 3), ("stealth", 2), ("slightOfHand", 1),("strength", -1), ("intimidation", -2)],
        "") #23-3
    harpy = raceDetails("harpy",
        ("4.0","4.9","5.8"),
        [("dexterity", 6), ("charm", 6), ("intellect", 4), ("performance", 4), ("strategy", 3), ("slightOfHand", 2), ("perception", 2), ("survival", 1), ("willPower", 1), ("constitution", -2), ("intimidation", -3), ("strength", -4)],
        "") #29-9
    oviur = raceDetails("oviur",
        ("3.9","4.5","5.1"),
        [("strength", 10), ("dexterity", 8), ("performance", 7), ("constitution", 6), ("stealth", 3), ("survival", 2), ("intimidation", -2), ("lockPicking", -3), ("insight", -5), ("charm", -6)],
        "") #36-16
    goblin = raceDetails("goblin",
        ("2.9","3.1","3.6"),
        [("dexterity", 5), ("strategy", 4), ("slightOfHand", 3), ("stealth", 3), ("craftsmenship", 3), ("lockPicking", 3), ("perception", 2), ("intellect", 1), ("constitution", -1), ("willPower", -1), ("strength", -2)],
        "") # 24-4
    minotaur = raceDetails("minotaur",
        ("7.6","8.11","10.4"),
        [("strength", 8), ("constitution", 6), ("intimidation", 5), ("survival", 4), ("perception", 3), ("lore", 3), ("intellect", -1), ("performance", -2), ("slightOfHand", -3), ("charm", -3)],
        "") #29-9
    avalite = raceDetails("avalite",
        ("4.2","5.7","6.8"),
        [("charm", 9), ("performance", 9), ("insight", 5), ("constitution", 3), ("intellect", 2), ("dexterity", 2), ("survival", -2), ("strength", -3), ("intimidation", -5)],
        "") #30-10
    dryad = raceDetails("dryad",
        ("4.11","5.6","5.11"),
        [("intellect", 6), ("charm", 5), ("willPower", 4), ("insight", 4), ("medicine", 3), ("survival", 3), ("dexterity", 2), ("craftsmenship", -2), ("intimidation", -3)],
        "") #25-5
    lycanthrope = raceDetails("lycanthrope",
        ("5.11","6.9","7.7"),
        [("strength", 7), ("perception", 6), ("survival", 5), ("intimidation", 4), ("constitution", 4), ("stealth", 3), ("dexterity", 2), ("insight", -2), ("performance", -2), ("lockPicking", -3), ("charm", -4)],
        "") #31-11
    #gnome
    #dragonkin
    #batfolk - name tbd
    #catfolk - name tbd
    #mantisfolk - name tbd
    raceList = [human,shifter,elf,halfElf,dwarf,orc,halfling,arenae,harpy,oviur,goblin,minotaur,avalite,dryad,lycanthrope]

    def raceDesc(race):
        description = ""
        if race == "human":
            description = "its humans"
        if race == "shifter":
            description = "a race of humanoids capaple altering their appearance"
        if race == "elf":
            description = "its elves"
        if race == "half-elf":
            description = "its half-elves"
        if race == "dwarf":
            description = "its dwarves"
        if race == "orc":
            description = "its orcs"
        if race == "halfling":
            description = "its halflings"
        if race == "arenae":
            description = "serpentine humanoids, whom share many characteristics with elves"
        if race == "harpy":
            description = "its harpies"
        if race == "oviur":
            description = "Nimble humaniods adept at stalking the corridors of the dungeon. standing shorter then a human, they have inky black skin and hair, pale white teeth and bioluminescent markings across their body"
        if race == "avalite":
            description = "beautiful abyssal humanoids, descendents of the succubi and incubi"
        if race == "minotaur":
            description = "its minotaurs"
        if race == "goblin":
            description = "its goblins"
        if race == "dryad":
            description = "its dryads"
        if race == "lycanthrope":
            description = "its lycanthropes"
        return description

    def showRaceHeight(race):
        if race == "human":
            return "Please input a height between [human.raceHeight[0]] and [human.raceHeight[2]]:"
        if race == "shifter":
            return "Please input a height between [shifter.raceHeight[0]] and [shifter.raceHeight[2]]:"
        if race == "elf":
            return "Please input a height between [elf.raceHeight[0]] and [elf.raceHeight[2]]:"
        if race == "dwarf":
            return "Please input a height between [dwarf.raceHeight[0]] and [dwarf.raceHeight[2]]:"
        if race == "orc":
            return "Please input a height between [orc.raceHeight[0]] and [orc.raceHeight[2]]:"
        if race == "halfling":
            return "Please input a height between [halfling.raceHeight[0]] and [halfling.raceHeight[2]]:"
        if race == "Arenae":
            return "Please input a height between [arenae.raceHeight[0]] and [arenae.raceHeight[2]]:"
        if race == "harpy":
            return "Please input a height between [harpy.raceHeight[0]] and [harpy.raceHeight[2]]:"
        if race == "Oviur":
            return "Please input a height between [oviur.raceHeight[0]] and [oviur.raceHeight[2]]:"
    def getHeightAvg(race):
        if race == "human":
            return humanHeight[1]
        if race == "elf":
            return elfHeight[1]
        if race == "dwarf":
            return dwarfHeight[1]
        if race == "orc":
            return orcHeight[1]
        if race == "halfling":
            return halflingHeight[1]
        if race == "Arenae":
            return arenaeHeight[1]
        if race == "harpy":
            return harpyHeight[1]
        if race == "Oviur":
            return oviurHeight[1]
    def secondarySkinColorDesc(race):
        if race == "Arenae":
            return "what color are your markings"
        if race == "Oviur":
            return "what color are your bioluminescent markings"

label raceDesc(race):
    if race == "human":
        "its humans"
    if race == "elf":
        "its elves"
    if race == "dwarf":
        "its dwarves"
    if race == "orc":
        "its orcs"
    if race == "halfling":
        "its halflings"
    if race == "Arenae":
        "serpentine humanoids, whom share many characteristics with elves"
    if race == "harpy":
        "its harpies"
    if race == "Oviur":
        "Nimble humaniods adept at stalking the corridors of the dungeon. standing shorter then a human, they have inky black skin and hair, pale white teeth and bioluminescent markings across their body"
