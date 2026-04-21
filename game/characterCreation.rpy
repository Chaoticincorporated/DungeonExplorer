label characterCreation:
    python:
        playerName = renpy.input(prompt='What is your name?', length=32)
        playerName = playerName.strip()

        if not playerName:
            playerName = "fuck"
        
        playerSheet.skills = [
            ["strength", 5],["dexterity", 5],["constitution", 5],
            ["intellect", 5],["charm", 5],["willPower", 5],
            ["insight", -10],["perception", -10],["craftsmenship", -10],
            ["lockPicking", -10],["lore", -10],["survival", -10],
            ["medicine", -10],["stealth", -10],["performance", -10],
            ["slightOfHand", -10],["intimidation", -10],["strategy", -10],
            ]
        playerSheet.bodyPartsBoolean = [False, False, False, False, False, False]
    call screen general_details
    pause

menu .genderSelection:
    "are you a boy or a girl" 
    "Boy":
        $ playerSheet.gender = "boy"
        $ playerSheet.hasBeard = True
    "Girl":
        $ playerSheet.gender = "girl"
        $ playerSheet.hasBeard = False
menu .raceSelection:
    "What race are you?"
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
menu .classSelectionOne:
    "What is your class"
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
    "next page":
        jump .classSelectionTwo
    "go back":
        jump .raceSelection
menu .classSelectionTwo:
    "What is your class"
    "previous page":
        jump .classSelectionOne
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
    "next page":
        jump .classSelectionThree
    "go back":
        jump .raceSelection
menu .classSelectionThree:
    "What is your class"
    "previous page":
        jump .classSelectionTwo
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
    "go back":
        jump .raceSelection
menu .classConfirmation:
    "So you are a [playerSheet.characterClass]?"
    "yes":
        "cool"
    "no":
        jump .classSelectionOne
label .cosmeticSelection:
    "The following option are purely cosmetic and will have no mechanical value outside of some NPCs having a preference."
menu .hairLengthSelection:
    "how long is your hair"
    "bald":
        $ playerSheet.hairLength = "bald"
        jump .eyeColorSelectionPageOne
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
    "curly":
        $ playerSheet.hairStyle = "curly"
    "straight":
        $ playerSheet.hairStyle = "straight"
    "pony tail" if playerSheet.hairLength != 'short':
        $ playerSheet.hairStyle = "pony tail"
    "go back":
        jump .hairLengthSelection
menu .hairColorSelectionPageOne:
    "what color is your hair"
    "white":
        $ playerSheet.hairColor = "white"
        jump .hasHairAccentsSelection
    "grey":
        $ playerSheet.hairColor = "grey"
        jump .hasHairAccentsSelection
    "black":
        $ playerSheet.hairColor = "black"
        jump .hasHairAccentsSelection
    "blonde":
        $ playerSheet.hairColor = "blonde"
        jump .hasHairAccentsSelection
    "light brown":
        $ playerSheet.hairColor = "light brown"
        jump .hasHairAccentsSelection
    "next page":
        jump .hairColorSelectionPageThree
    "go back":
        jump .hairStyleSelection
menu .hairColorSelectionPageTwo:
    "what color is your hair"
    "previous page":
        jump .hairColorSelectionPageOne
    "brown":
        $ playerSheet.hairColor = "brown"
        jump .hasHairAccentsSelection
    "dark brown":
        $ playerSheet.hairColor = "dark brown"
        jump .hasHairAccentsSelection
    "ginger":
        $ playerSheet.hairColor = "ginger"
        jump .hasHairAccentsSelection
    "orange":
        $ playerSheet.hairColor = "orange"
        jump .hasHairAccentsSelection
    "red":
        $ playerSheet.hairColor = "red"
        jump .hasHairAccentsSelection
    "next page":
        jump .hairColorSelectionPageThree
    "go back":
        jump .hairStyleSelection
menu .hairColorSelectionPageThree:
    "what color is your hair"
    "previous page":
        jump .hairColorSelectionPageTwo
    "golden":
        $ playerSheet.hairColor = "golden"
        jump .hasHairAccentsSelection
    "silver":
        $ playerSheet.hairColor = "silver"
        jump .hasHairAccentsSelection
    "pink":
        $ playerSheet.hairColor = "pink"
        jump .hasHairAccentsSelection
    "green":
        $ playerSheet.hairColor = "green"
        jump .hasHairAccentsSelection
    "lime":
        $ playerSheet.hairColor = "lime"
        jump .hasHairAccentsSelection
    "next page":
        jump .hairColorSelectionPageFour
    "go back":
        jump .hairStyleSelection
menu .hairColorSelectionPageFour:
    "what color is your hair"
    "previous page":
        jump .hairColorSelectionPageTree
    "cyan":
        $ playerSheet.hairColor = "cyan"
    "light blue":
        $ playerSheet.hairColor = "light blue"
    "blue":
        $ playerSheet.hairColor = "blue"
    "magenta":
        $ playerSheet.hairColor = "magenta"
    "purple":
        $ playerSheet.hairColor = "purple"
    "go back":
        jump .hairStyleSelection
menu .hasHairAccentsSelection:
    "do you want color accents in your hair"
    "yes":
        $ playerSheet.hasHairAccents = True
    "no": 
        $ playerSheet.hasHairAccents = False
        jump .eyeColorSelectionPageOne
menu .hairColorSecondarySelectionPageOne:
    "what color is your hair"
    "white":
        $ playerSheet.hairColor = "white"
        jump .eyeColorSelectionPageOne
    "grey":
        $ playerSheet.hairColor = "grey"
        jump .eyeColorSelectionPageOne
    "black":
        $ playerSheet.hairColor = "black"
        jump .eyeColorSelectionPageOne
    "blonde":
        $ playerSheet.hairColor = "blonde"
        jump .eyeColorSelectionPageOne
    "light brown":
        $ playerSheet.hairColor = "light brown"
        jump .eyeColorSelectionPageOne
    "next page":
        jump .hairColorSecondarySelectionPageThree
    "go back":
        jump .hasHairAccentsSelection
menu .hairColorSecondarySelectionPageTwo:
    "what color is your hair"
    "previous page":
        jump .hairColorSecondarySelectionPageOne
    "brown":
        $ playerSheet.hairColor = "brown"
        jump .eyeColorSelectionPageOne
    "dark brown":
        $ playerSheet.hairColor = "dark brown"
        jump .eyeColorSelectionPageOne
    "ginger":
        $ playerSheet.hairColor = "ginger"
        jump .eyeColorSelectionPageOne
    "orange":
        $ playerSheet.hairColor = "orange"
        jump .eyeColorSelectionPageOne
    "red":
        $ playerSheet.hairColor = "red"
        jump .eyeColorSelectionPageOne
    "next page":
        jump .hairColorSecondarySelectionPageThree
    "go back":
        jump .hasHairAccentsSelection
menu .hairColorSecondarySelectionPageThree:
    "what color is your hair"
    "previous page":
        jump .hairColorSecondarySelectionPageTwo
    "golden":
        $ playerSheet.hairColor = "golden"
        jump .eyeColorSelectionPageOne
    "silver":
        $ playerSheet.hairColor = "silver"
        jump .eyeColorSelectionPageOne
    "pink":
        $ playerSheet.hairColor = "pink"
        jump .eyeColorSelectionPageOne
    "green":
        $ playerSheet.hairColor = "green"
        jump .eyeColorSelectionPageOne
    "lime":
        $ playerSheet.hairColor = "lime"
        jump .eyeColorSelectionPageOne
    "next page":
        jump .hairColorSecondarySelectionPageFour
    "go back":
        jump .hasHairAccentsSelection
menu .hairColorSecondarySelectionPageFour:
    "what color is your hair"
    "previous page":
        jump .hairColorSecondarySelectionPageTree
    "cyan":
        $ playerSheet.hairColor = "cyan"
    "light blue":
        $ playerSheet.hairColor = "light blue"
    "blue":
        $ playerSheet.hairColor = "blue"
    "magenta":
        $ playerSheet.hairColor = "magenta"
    "purple":
        $ playerSheet.hairColor = "purple"
    "go back":
        jump .hasHairAccentsSelection
menu .eyeColorSelectionPageOne:
    "what color is your eyes"
    "blue":
        $ playerSheet.eyeColor = "blue"
    "green":
        $ playerSheet.eyeColor = "green"
    "brown":
        $ playerSheet.eyeColor = "brown"
    "light blue":
        $ playerSheet.eyeColor = "light blue"
    "next page":
        jump .eyeColorSelectionPageTwo
    "go back" if playerSheet.hasHairAccents and playerSheet.hairLength != 'bald':
        jump .hairColorSecondarySelectionPageOne
    "go back" if playerSheet.hairLength != 'bald':
        jump .hasHairAccentsSelection
    "go back" if playerSheet.hairLength == 'bald':
        jump .hairLengthSelection
menu .eyeColorSelectionPageTwo:
    "what color is your eyes"
    "previous page":
        jump .eyeColorSelectionPageOne
    "yellow":
        $ playerSheet.eyeColor = "yellow"
    "orange":
        $ playerSheet.eyeColor = "orange"
    "purple":
        $ playerSheet.eyeColor = "purple"
    "red":
        $ playerSheet.eyeColor = "red"
    "next page":
        jump .eyeColorSelectionPageThree
    "go back" if hasHairAccents:
        jump .hairColorSecondarySelectionPageOne
    "go back" if playerSheet.hairLength != 'bald':
        jump .hasHairAccentsSelection
    "go back" if playerSheet.hairLength == 'bald':
        jump .hairLengthSelection
menu .eyeColorSelectionPageThree:
    "what color is your eyes"
    "previous page":
        jump .eyeColorSelectionPageTwo
    "pink":
        $ playerSheet.eyeColor = "pink"
    "silver":
        $ playerSheet.eyeColor = "silver"
    "golden":
        $ playerSheet.eyeColor = "golden"
    "white":
        $ playerSheet.eyeColor = "white"
    "go back" if hasHairAccents:
        jump .hairColorSecondarySelectionPageOne
    "go back" if playerSheet.hairLength != 'bald':
        jump .hasHairAccentsSelection
    "go back" if playerSheet.hairLength == 'bald':
        jump .hairLengthSelection
menu .hasFrecklesSelection:
    "do you have freckles"
    "yes":
        $ playerSheet.hasFreckles = True
        if playerSheet.hasBeard! and playerSheet.hasHorns:
            jump .hornStyleSelection
        if playerSheet.hasBeard! and playerSheet.hasHorns!:
            jump .faceStructureSelection
    "no":
        $ playerSheet.hasFreckles = False
        if playerSheet.hasBeard! and playerSheet.hasHorns:
            jump .hornStyleSelection
        if playerSheet.hasBeard! and playerSheet.hasHorns!:
            jump .faceStructureSelection
    "go back":
        jump .eyeColorSelectionPageOne
menu .beardStyleSelection:
    "what style is your beard"
    "clean shaven":
        $ playerSheet.beardStyle = "clean shaven"
        if playerSheet.hasHorns!:
            jump .faceStructureSelection
    "stubble":
        $ playerSheet.beardStyle = "stubble"
        if playerSheet.hasHorns!:
            jump .faceStructureSelection
    "mustache":
        $ playerSheet.beardStyle = "mustache"
        if playerSheet.hasHorns!:
            jump .faceStructureSelection
    "short and full":
        $ playerSheet.beardStyle = "short and full"
        if playerSheet.hasHorns!:
            jump .faceStructureSelection
    "goatee":
        $ playerSheet.beardStyle = "goatee"
        if playerSheet.hasHorns!:
            jump .faceStructureSelection
    "medium unkept":
        $ playerSheet.beardStyle = "medium unkept"
        if playerSheet.hasHorns!:
            jump .faceStructureSelection
    "medium tidy":
        $ playerSheet.beardStyle = "medium tidy"
        if playerSheet.hasHorns!:
            jump .faceStructureSelection
    "long unkept":
        $ playerSheet.beardStyle = "long unkept"
        if playerSheet.hasHorns!:
            jump .faceStructureSelection
    "long tidy":
        $ playerSheet.beardStyle = "long tidys"
        if playerSheet.hasHorns!:
            jump .faceStructureSelection
    "viking braids":
        $ playerSheet.beardStyle = "viking braids"
        if playerSheet.hasHorns!:
            jump .faceStructureSelection
    "go back":
        jump .hasFrecklesSelection
menu .hornStyleSelection:
    ""
    "go back" if playerSheet.hasBeard:
        jump .beardStyleSelection
    "go back" if playerSheet.hasBeard!:
        jump .hasFrecklesSelection
menu .faceStructureSelection:
    "please enter your face structure"
    "charubic" if playerSheet.race == 'halfling' or playerSheet.race == 'harpy':
        $ playerSheet.faceStructure = "charubic"
    "delicate" if playerSheet.race != 'orc' or playerSheet.race != 'dwarf':
        $ playerSheet.faceStructure = "charubic"
    "regal":
        $ playerSheet.faceStructure = "charubic"
    "soft" if playerSheet.race != 'orc' or playerSheet.race != 'dwarf':
        $ playerSheet.faceStructure = "charubic"
    "chisled" if playerSheet.race != 'halfling' or playerSheet.race != 'elf' or playerSheet.race != 'arenae':
        $ playerSheet.faceStructure = "charubic"
    "block headed" if playerSheet.race == 'orc' or playerSheet.race == 'human':
        $ playerSheet.faceStructure = "charubic"
    "round" if playerSheet.race != 'orc' or playerSheet.race != 'elf' or playerSheet.race != 'arenae':
        $ playerSheet.faceStructure = "charubic"
    "gruff" if playerSheet.race == 'human' or playerSheet.race == 'orc' or playerSheet.race == 'dwarf':
        $ playerSheet.faceStructure = "charubic"
    "go back":
        if playerSheet.hasHorns:
            jump .hornStyleSelection
        if playerSheet.hasHorns! and playerSheet.hasBeard:
            jump .beardStyleSelection
        if playerSheet.hasBeard! and playerSheet.hasHorns!:
            jump .hasFrecklesSelection
label .tranitionToSkinColor:
    if playerSheet.race == 'oviur':
        $ playerSheet.skinColor = "black"
        jump skinColorSecondarySelection
menu .skinColorSelection:
    "What is your skin color"
    "white" if playerSheet.race == 'elf':
        $ playerSheet.skinColor = "white"
    "pale" if playerSheet.race != 'orc':
        $ playerSheet.skinColor = "pale"
    "baige" if playerSheet.race != 'elf' or playerSheet.race != 'orc':
        $ playerSheet.skinColor = "baige"
    "olive" if playerSheet.race != 'elf' playerSheet.race != 'orc':
        $ playerSheet.skinColor = "olive"
    "light brown" if playerSheet.race != 'elf' playerSheet.race != 'orc':
        $ playerSheet.skinColor = "light brown"
    "brown" if playerSheet.race != 'elf':
        $ playerSheet.skinColor = "brown"
    "dark brown" if playerSheet.race != 'elf':
        $ playerSheet.skinColor = "dark brown"
    "black" if playerSheet.race == 'orc' or playerSheet.race == 'human' or playerSheet.race == 'arenae':
        $ playerSheet.skinColor = "black"
    "bronze" if playerSheet.race == 'elf':
        $ playerSheet.skinColor = "bronze"
    "golden" if playerSheet.race == 'elf':
        $ playerSheet.skinColor = "golden"
    "silver" if playerSheet.race == 'elf':
        $ playerSheet.skinColor = "silver"
    "dark green" if playerSheet.race == 'orc':
        $ playerSheet.skinColor = "dark green"
    "go back":
        jump .faceStructureSelection
label .tranitionToHairColorSecondary:
    if playerSheet.race != 'arenae':
        $ playerSheet.skinColorSecondary = "none"
        jump statSelection
menu .skinColorSecondarySelection:
    "[secondarySkinColorDesc(playerSheet.race)]"
    "red":
        $ playerSheet.skinColorSecondary = "red"
    "green":
        $ playerSheet.skinColorSecondary = "green"
    "cyan":
        $ playerSheet.skinColorSecondary = "cyan"
    "blue":
        $ playerSheet.skinColorSecondary = "blue"
    "pink":
        $ playerSheet.skinColorSecondary = "pink"
    "magenta":
        $ playerSheet.skinColorSecondary = "magenta"
    "purple":
        $ playerSheet.skinColorSecondary = "purple"
    "orange":
        $ playerSheet.skinColorSecondary = "orange"
    "yellow":
        $ playerSheet.skinColorSecondary = "yellow"
    "lime":
        $ playerSheet.skinColorSecondary = "lime"
    "go back" if playerSheet.race == 'oviur':
        jump .faceStructureSelection
    "go back" if playerSheet.race != 'oviur':
        jump .skinColorSelection

