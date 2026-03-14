# The script of the game goes in this file.


#classes

         


#defining main character and traits
define pa = Character("[playerName]", color="BD0000")
$ skillPoints = 30
$ playerSheet = CharacterDataSheet()

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
            weight = 0
            hasHorns = False
            def __init__(self,gender,race,hairLength,hairStyle,hasHairAccents,
            hairColor,hairColorSecondary,eyeColor,hasFreckles,
            hasBeard,beardStyle,ears,hornStyle,faceStructure,
            skinColor,skinColorSecondary,body,upperArm,lowerArm,hands,
            thighs,calfs,feet,height,fitness,build,hasTail,hasWings,
            strength,dexterity,constitution,intellect,insight,charm,
            will,arcana,technique,initiative,level,hitpoints,characterClass
            ):
                self.gender = gender
                self.race = race
                #hair
                self.hairLength = hairLength
                self.hairStyle = hairStyle
                self.hasHairAccents = hasHairAccents
                self.hairColor = hairColor
                self.hairColorSecondary = hairColorSecondary
                #face/head
                self.eyeColor = eyeColor
                self.hasFreckles = hasFreckles
                self.hasBeard = hasBeard
                self.beardStyle = beardStyle
                self.ears = ears
                self.hornStyle = hornStyle
                self.faceStructure = faceStructure
                # body
                self.skinColor = skinColor
                self.skinColorSecondary = skinColorSecondary
                self.body = body
                self.upperArm = upperArm
                self.lowerArm = lowerArm
                self.hands = hands
                self.thighs = thighs
                self.calfs = calfs
                self.feet = feet
                self.height = height
                self.fitness = fitness
                self.build = build
                self.hasTail = hasTail
                self.hasWings = hasWings
                #stats
                self.strength = strength
                self.dexterity = dexterity
                self.constitution = constitution
                self.intellect = intellect
                self.insight = insight
                self.charm = charm
                self.will = will
                self.arcana = arcana
                self.technique = technique
                self.initiative = initiative
                self.level = level
                self.hitpoints = hitpoints
                self.characterClass = characterClass
    scene blackout
    "to character creation"
    jump characterCreation

label gameEnd:
    scene blackout
    "Game Over"

    # This ends the game.

    return
