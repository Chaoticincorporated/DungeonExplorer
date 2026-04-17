# The script of the game goes in this file.


#classes
init python:
    class CharacterDataSheet:
        traits = []
        skills = [
            ("strength", 5),("dexterity", 5),("constitution", 5),
            ("intellect", 5),("charm", 5),("willPower", 5),
            ("insight", -10),("perception", -10),("craftsmenship", -10),
            ("lockPicking", -10),("lore", -10),("survival", -10),
            ("medicine", -10),("stealth", -10),("performance", -10),
            ("slightOfHand", -10),("intimidation", -10),("strategy", -10),
            ]
        inventory = []
        #stats
        level = 0
        hitpoints = 0
        gender = ""
        race = ""
        characterClass= ""
        height = ""
        build = "average"
        weight = 0 #weight is in pounds (lbs)
        #core skills:
        strength = 5
        dexterity = 5
        constitution = 5
        intellect = 5
        charm = 5
        willPower = 5
        #secondary skills
        insight = -10
        perception = -10
        craftsmenship = -10
        lockPicking = -10
        lore = -10
        survival = -10
        medicine = -10
        stealth = -10
        performance = -10
        slightOfHand = -10
        intimidation = -10
        strategy = -10
        #tertairy skills
        initiative = 0
        arcana = 0
        technique = 0
        #equipment
        makeUp = "nothing"
        shirt = "nothing"
        pants = "nothing"
        bra = "nothing"
        underWare = "nothing"
        headWare = "nothing"
        armour = "nothing"
        mainHand = "nothing"
        offHand = "nothing"
        #boolean variables
        hasHorns = False
        hasTail = False
        hasWings = False
        hasFreckles = False
        hasBeard = False
        hasHairAccents = False
        #appearance
        hairLength = "bald"
        hairStyle = ""
        hairColor = ""
        hairColorSecondary = ""
        eyeColor = ""
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
        def setRacialSkillBonuses(self, raceSkillBonus):
            for bonus in raceSkillBonus:
                match bonus[0]:
                    case "strength":
                        self.strength += bonus[1]
                    case "dexterity":
                        self.dexterity += bonus[1]
                    case "constitution":
                        self.constitution += bonus[1]
                    case "intellect":
                        self.intellect += bonus[1]
                    case "charm":
                        self.charm += bonus[1]
                    case "willPower":
                        self.willPower += bonus[1]
                    case "insight":
                        self.insight += bonus[1]
                    case "perception":
                        self.perception += bonus[1]
                    case "craftsmenship":
                        self.craftsmenship += bonus[1]
                    case "lockPicking":
                        self.lockPicking += bonus[1]
                    case "lore":
                        self.lore += bonus[1]
                    case "survival":
                        self.survival += bonus[1]
                    case "medicine":
                        self.medicine += bonus[1]
                    case "stealth":
                        self.stealth += bonus[1]
                    case "performance":
                        self.performance += bonus[1]
                    case "slightOfHand":
                        self.slightOfHand += bonus[1]
                    case "intimidation":
                        self.intimidation += bonus[1]
                    case "strategy":
                        self.strategy += bonus[1]
        def getInches(self):
            inches = 0
            for index in range(len(self.height)):
                if self.height[index] == ".":
                    inches += int(self.height[0:index]) * 12
                    if index == len(self.height)-3:
                        inches += int(self.height[index+1])
                        inches += int(height[index+2])
                    else:
                        inches += int(self.height[index+1])
                    break
            return inches
        def getWeight(self):
            match self.build:
                case "gaunt":
                    self.weight = self.getInches() * 1.5
                case "skinny":
                    self.weight = self.getInches() * 1.75
                case "lean":
                    self.weight = self.getInches() * 2
                case "lithe":
                    self.weight = self.getInches() * 2.25
                case "average":
                    self.weight = self.getInches() * 2.5
                case "broad":
                    self.weight = self.getInches() * 2.75
                case "bulky":
                    self.weight = self.getInches() * 3
                case "thick":
                    self.weight = self.getInches() * 3.25
                case "obese":
                    self.weight = self.getInches() * 3.5
        def getSkill(self, targetSkill):
            for skill in self.skills:
                if skill[0] == targetSkill:
                    targetSkill = skill[1]
                    break
            return targetSkill
        def addToSkill(self, targetSkill, amount):
            for skill in self.skills:
                if skill[0] == targetSkill:
                    skill[1] += amount
                    break
    
    def numeralRangeConstraints(minNum,maxNum,valueToCheck):
        if valueToCheck > maxNum:
            valueToCheck = maxNum
        elif valueToCheck < minNum:
            valueToCheck = minNum
        return valueToCheck

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
