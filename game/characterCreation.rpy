label characterCreation:
    python:
        playerName = renpy.input(prompt='What is your name', length=32)
        playerName = playerName.strip()

        if not playerName:
            playerName = "fuck"

menu .genderSelection:
    "are you a boy or a girl" 
    "Boy":
        $ playerSheet.gender = "boy"
        $ playerSheet.hasBeard = True
    "Girl":
        $ playerSheet.gender = "girl"
        $ playerSheet.hasBeard = False
menu .raceSelection:
    "What race are you"
    "Human":
        $ playerSheet.race = "human"
        call raceDesc(playerSheet.race)
    "Elf":
        $ playerSheet.race = "elf"
        call raceDesc(playerSheet.race)
    "Dwarf":
        $ playerSheet.race = "dwarf"
        call raceDesc(playerSheet.race)
    "Orc":
        $ playerSheet.race = "orc"
        call raceDesc(playerSheet.race)
    "Halfling":
        $ playerSheet.race = "halfling"
        call raceDesc(playerSheet.race)
    "Arenae":
        $ playerSheet.race = "arenae"
        call raceDesc(playerSheet.race)
    "Harpy":
        $ playerSheet.race = "harpy"
        call raceDesc(playerSheet.race)
    "Oviur":
        $ playerSheet.race = "oviur"
        call raceDesc(playerSheet.race)
menu .raceConfirmation:
    "So you are a [playerSheet.race]?"
    "yes":
        "cool"
    "no":
        jump .raceSelection
menu .classSelection:
    "What race are you"
    "Assassin":
        $ playerSheet.characterClass = "assassin"
        call classDesc(playerSheet.characterClass)
    "Barbarian":
        $ playerSheet.characterClass = "barbarian"
        call classDesc(playerSheet.characterClass)
    "Bard":
        $ playerSheet.characterClass = "bard"
        call classDesc(playerSheet.characterClass)
    "Cleric":
        $ playerSheet.characterClass = "cleric"
        call classDesc(playerSheet.characterClass)
    "Druid":
        $ playerSheet.characterClass = "druid"
        call classDesc(playerSheet.characterClass)
    "Eldrich Knight":
        $ playerSheet.characterClass = "eldrich knight"
        call classDesc(playerSheet.characterClass)
    "Fighter":
        $ playerSheet.characterClass = "fighter"
        call classDesc(playerSheet.characterClass)
    "Mystic":
        $ playerSheet.characterClass = "mystic"
        call classDesc(playerSheet.characterClass)
    "Paladin":
        $ playerSheet.characterClass = "paladin"
        call classDesc(playerSheet.characterClass)
    "Ranger":
        $ playerSheet.characterClass = "ranger"
        call classDesc(playerSheet.characterClass)
    "Scribe":
        $ playerSheet.characterClass = "scribe"
        call classDesc(playerSheet.characterClass)
    "Thief":
        $ playerSheet.characterClass = "thief"
        call classDesc(playerSheet.characterClass)
    "Warlock":
        $ playerSheet.characterClass = "warlock"
        call classDesc(playerSheet.characterClass)
    "Warlord":
        $ playerSheet.characterClass = "warlord"
        call classDesc(playerSheet.characterClass)
    "Witch":
        $ playerSheet.characterClass = "witch"
        call classDesc(playerSheet.characterClass)
    "Wizard":
        $ playerSheet.characterClass = "wizard"
        call classDesc(playerSheet.characterClass)
menu .classConfirmation:
    "So you are a [playerSheet.characterClass]?"
    "yes":
        "cool"
    "no":
        jump .classSelection
label .cosmeticSelection:
    "The following option are purely cosmetic and will have no mechanical value outside of some NPCs having a preference."
menu .hairLengthSelection:
    "how long is your hair"
    "bald":
        $ playerSheet.hairLength = "bald"
        jump .eyeColorSelection
    "short":
        $ playerSheet.hairLength = "short"
    "shoulder length":
        $ playerSheet.hairLength = "shoulder length"
    "long":
        $ playerSheet.hairLength = "long"
    "to the waist":
        $ playerSheet.hairLength = "extra long"
menu .hairStyleSelection:
    "what style is your hair"
menu .hairColorSelection:
    "what color is your hair"
menu .hasHairAccentsSelection:
    "do you want color accents in your hair"
menu .eyeColorSelection:
    "what color is your eyes"
menu .hasFrecklesSelection:
    "do you have freckles"
menu .beardStyleSelection:
    "what style is your beard"
    "clean shaven":
        $ playerSheet.beardStyle = "clean shaven"
    "stubble":
        $ playerSheet.beardStyle = "stubble"
    "mustache":
        $ playerSheet.beardStyle = "mustache"
    "short and full":
        $ playerSheet.beardStyle = "short and full"
    "goatee":
        $ playerSheet.beardStyle = "goatee"
    "medium unkept":
        $ playerSheet.beardStyle = "medium unkept"
    "medium tidy":
        $ playerSheet.beardStyle = "medium tidy"
    "long unkept":
        $ playerSheet.beardStyle = "long unkept"
    "long tidy":
        $ playerSheet.beardStyle = "long tidys"
    "viking braids":
        $ playerSheet.beardStyle = "viking braids"
    "go back":
        jump .hasFrecklesSelection
menu .hornStyleSelection:
    ""
menu .faceStructureSelection:
    ""
menu .skinColorSelection:
    ""
menu .skinColorSecondarySelection:
    ""
label .statSelection:
    "The following will have varying degrees of mechanical value, and as such will often cost skill points to adjust them."
    $ playerSheet.fitness = "average"
    $ playerSheet.build = "average"
menu .heightSelection:
    ""
menu .buildSelection:
    ""
menu .fitnessSelection:
    ""
menu .hasBeardSelection:
    ""
menu .hasBeardSelection:
    ""
menu .hasBeardSelection:
    ""
menu .hasBeardSelection:
    ""
menu .hasBeardSelection:
    ""
menu .hasBeardSelection:
    ""
menu .hasBeardSelection:
    ""
menu .hasBeardSelection:
    ""
menu .hasBeardSelection:
    ""
menu .hasBeardSelection:
    ""
