# The script of the game goes in this file.


#classes
init python:
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
        strength = 1
        dexterity = 1
        constitution = 1
        intellect = 1
        charm = 1
        willPower = 1
        insight = 0
        perception = 0
        initiative = 0
        arcana = 0
        technique = 0
        level = 0
        hitpoints = 0
        characterClass= ""

    skillPoints = 30
         


#defining main character and traits
define pa = Character("[playerName]", color="BD0000")


image blackout = "#000"
image playerSanctum = im.Scale('The_Sanctum.png', 1920, 1080)
image passageOne = im.Scale('dungeon_passage_one.png', 1920, 1080)


# The game starts here.

label start:
    
    $ playerSheet = CharacterDataSheet()
    
    scene blackout
    
    "to character creation"
    jump characterCreation

label gameEnd:
    scene blackout
    "Game Over"

    # This ends the game.

    return
