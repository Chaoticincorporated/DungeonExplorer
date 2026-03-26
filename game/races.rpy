#(minHeight,averageHeight,maxHeight) the whole number represents feet and the decimal represents inches
$ humanHeight = (4.6,5.5,6.4)
$ elfHeight = (4.3,5.0,5.10)
$ dwarfHeight = (3.11,4.6,5.2)
$ orcHeight = (4.9,5.9,6.10)
$ haflingHeight = (2.5,3.3,4.1)
$ arenaeHeight = (4.2,5.2,6.3)
$ harpyHeight = (4.0,4.9,5.8)
$ oviurHeight = (3.9,4.5,5.1)

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

python:
    def showRaceHeight(race):
        if race == "human":
            return "Please input a height between [humanHeight[0]] and [humanHeight[2]]:"
        if race == "elf":
            return "Please input a height between [elfHeight[0]] and [elfHeight[2]]:"
        if race == "dwarf":
            return "Please input a height between [dwarfHeight[0]] and [dwarfHeight[2]]:"
        if race == "orc":
            return "Please input a height between [orcHeight[0]] and [orcHeight[2]]:"
        if race == "halfling":
            return "Please input a height between [halflingHeight[0]] and [halflingHeight[2]]:"
        if race == "Arenae":
            return "Please input a height between [arenaeHeight[0]] and [arenaeHeight[2]]:"
        if race == "harpy":
            return "Please input a height between [harpyHeight[0]] and [harpyHeight[2]]:"
        if race == "Oviur":
            return "Please input a height between [oviurHeight[0]] and [oviurHeight[2]]:"
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