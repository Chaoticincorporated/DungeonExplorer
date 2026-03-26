# The script of the game goes in this file.


#classes

         


#defining main character and traits
define pa = Character("[playerName]", color="BD0000")
$ skillPoints = 30


image blackout = "#000"
image playerSanctum = im.Scale('The_Sanctum.png', 1920, 1080)
image passageOne = im.Scale('dungeon_passage_one.png', 1920, 1080)


# The game starts here.

label start:
    python:
        class CharacterDataSheet:
            traits = []
            skills = []
            inventory = []
            makeUp = "nothing"
            shirt = "nothing"
            pants = "nothing"
            bra = "nothing"
            underWare = "nothing"
            headWare = "nothing"
            armour = "nothing"
            mainHand = "nothing"
            offHand = "nothing"
            hitpoints = 0
            weight = 0
            hasHorns = False
            gender = ""
            race = ""
            hairLength = ""
            hairStyle = ""
            hasHairAccents = ""
            hairColor = ""
            hairColorSecondary = ""
            eyeColor = ""
            hasFreckles = ""
            hasBeard = ""
            beardStyle = ""
            ears = ""
            hornStyle = ""
            faceStructure = ""
            skinColor = ""
            skinColorSecondary = ""
            body = ""
            upperArm = ""
            lowerArm = ""
            hands = ""
            thighs = ""
            calfs = ""
            feet = ""
            height = ""
            build = ""
            hasTail = ""
            hasWings = ""
            strength = ""
            dexterity = ""
            constitution = ""
            intellect = ""
            insight = ""
            charm = ""
            will = ""
            arcana = ""
            technique = ""
            initiative = ""
            level = 0
            hitpoints = 0
            characterClass= ""
    $ playerSheet = CharacterDataSheet()
    
    scene blackout
    
    "to character creation [playerSheet.makeUp]"
    jump characterCreation

label gameEnd:
    scene blackout
    "Game Over"

    # This ends the game.

    return
