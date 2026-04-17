init 2 python:
    bottomText = ""
    # index 0-5 are the core skills, 6-17 are the secondary skills, 18 is skill points
    charaCreationTempSkillMods = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    def setTempRacialBonuses(raceSkillBonus):
        skillArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for bonus in raceSkillBonus:
            match bonus[0]:
                case "strength":
                    skillArray[0] += bonus[1]
                case "dexterity":
                    skillArray[1] += bonus[1]
                case "constitution":
                    skillArray[2] += bonus[1]
                case "intellect":
                    skillArray[3] += bonus[1]
                case "charm":
                    skillArray[4] += bonus[1]
                case "willPower":
                    skillArray[5] += bonus[1]
                case "insight":
                    skillArray[6] += bonus[1]
                case "perception":
                    skillArray[7] += bonus[1]
                case "craftsmenship":
                    skillArray[8] += bonus[1]
                case "lockPicking":
                    skillArray[9] += bonus[1]
                case "lore":
                    skillArray[10] += bonus[1]
                case "survival":
                    skillArray[11] += bonus[1]
                case "medicine":
                    skillArray[12] += bonus[1]
                case "stealth":
                    skillArray[13] += bonus[1]
                case "performance":
                    skillArray[14] += bonus[1]
                case "slightOfHand":
                    skillArray[15] += bonus[1]
                case "intimidation":
                    skillArray[16] += bonus[1]
                case "strategy":
                    skillArray[17] += bonus[1]
                case "skillPoints":
                    skillArray[18] += bonus[1]
        return skillArray
    
screen character_creation_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "character_creation"
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "character_creation_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "character_creation_navigation_frame"

            frame:
                style "character_creation_content_frame"

                if scroll == "viewport":
                    vbox:
                        viewport:
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True
                            area (0, 0, 1400, 750)
                            side_yfill True

                            vbox:
                                spacing spacing

                                transclude
                        vbox:    
                            style_prefix "bottom_text_initial"
                            style "bottom_text_padding"
                            text _("")
                            text _("[bottomText]")
                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude
                    
                else:

                    transclude

    use character_creation_nav

style character_creation_outer_frame is empty
style character_creation_navigation_frame is empty
style character_creation_content_frame is empty
style character_creation_viewport is gui_viewport
style character_creation_side is gui_side
style character_creation_scrollbar is gui_vscrollbar

style character_creation_label is gui_label
style character_creation_label_text is gui_label_text

style bottom_text_padding is vbox

style bottom_text_initial_text:
    size 30

style character_creation_outer_frame:
    bottom_padding 45
    top_padding 100

    background "gui/overlay/game_menu.png"

style character_creation_navigation_frame:
    xsize 420
    yfill True

style character_creation_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style character_creation_viewport:
    xsize 1380

style character_creation_vscrollbar:
    unscrollable gui.unscrollable

style character_creation_side:
    spacing 15

style character_creation_label:
    xpos 75
    ysize 180

style character_creation_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

screen character_creation_nav():
    vbox:
        style_prefix "chara_creation_nav"
        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing
        
        text _("Skill Points: [skillPoints + charaCreationTempSkillMods[18]]")
        textbutton _("General") action [ShowMenu("general_details"), Hide("defining_character_appearance"), SetVariable("bottomText", "General Character Details")]
        if playerSheet.race != "":
            textbutton _("Appearance") action [ShowMenu("defining_character_appearance"), Hide("general_details"), SetVariable("bottomText", "Character appearance")]
style chara_creation_nav_button is gui_button
style chara_creation_nav_button_text is gui_button_text
style chara_creation_nav_text is gui_text

#style chara_creation_nav_text:


screen general_details():
    tag menu
        
    use character_creation_menu(_("General"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                vbox:
                    style_prefix "radio"
                    label _("Male or Female")
                    textbutton _("Male") action SetVariable("playerSheet.gender", "boy")
                    textbutton _("Female") action SetVariable("playerSheet.gender", "girl")
                viewport:
                    area (0, 0, 400, 400)
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True
                    vbox:
                        style_prefix "radio"
                        label _("Race")
                        for race in raceList:
                            textbutton _("[race.raceName.capitalize()]"): 
                                action [
                                SetVariable("playerSheet.race", race),
                                SetVariable("playerSheet.height", race.getRaceHeightAvg()), 
                                SetVariable("bottomText", race.raceName), 
                                SetVariable("charaCreationTempSkillMods", setTempRacialBonuses(race.raceSkillBonus))
                                ]
                                selected (playerSheet.race == race)
                viewport:
                    area (0, 0, 400, 400)
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True
                    vbox:
                        style_prefix "radio"
                        label _("Class")
                        textbutton _("Assassin") action [SetVariable("playerSheet.characterClass", "assassin"), SetVariable("bottomText", classDesc("assassin"))]
                        textbutton _("Barbarian") action [SetVariable("playerSheet.characterClass", "barbarian"), SetVariable("bottomText", classDesc("barbarian"))]
                        textbutton _("Bard") action [SetVariable("playerSheet.characterClass", "bard"), SetVariable("bottomText", classDesc("bard"))]
                        textbutton _("Cleric") action [SetVariable("playerSheet.characterClass", "cleric"), SetVariable("bottomText", classDesc("cleric"))]
                        textbutton _("Druid") action [SetVariable("playerSheet.characterClass", "druid"), SetVariable("bottomText", classDesc("druid"))]
                        textbutton _("Eldrich Knight") action [SetVariable("playerSheet.characterClass", "eldrich knight"), SetVariable("bottomText", classDesc("eldrich knight"))]
                        textbutton _("Fighter") action [SetVariable("playerSheet.characterClass", "fighter"), SetVariable("bottomText", classDesc("fighter"))]
                        textbutton _("Mystic") action [SetVariable("playerSheet.characterClass", "mystic"), SetVariable("bottomText", classDesc("mystic"))]
                        textbutton _("Paladin") action [SetVariable("playerSheet.characterClass", "paladin"), SetVariable("bottomText", classDesc("paladin"))]
                        textbutton _("Ranger") action [SetVariable("playerSheet.characterClass", "ranger"), SetVariable("bottomText", classDesc("ranger"))]
                        textbutton _("Scribe") action [SetVariable("playerSheet.characterClass", "scribe"), SetVariable("bottomText", classDesc("scribe"))]
                        textbutton _("Thief") action [SetVariable("playerSheet.characterClass", "thief"), SetVariable("bottomText", classDesc("thief"))]
                        textbutton _("Warlock") action [SetVariable("playerSheet.characterClass", "warlock"), SetVariable("bottomText", classDesc("warlock"))]
                        textbutton _("Warlord") action [SetVariable("playerSheet.characterClass", "warlord"), SetVariable("bottomText", classDesc("warlord"))]
                        textbutton _("Witch") action [SetVariable("playerSheet.characterClass", "witch"), SetVariable("bottomText", classDesc("witch"))]
                        textbutton _("Wizard") action [SetVariable("playerSheet.characterClass", "wizard"), SetVariable("bottomText", classDesc("wizard"))]
            text _("")
            label _("Core Skills(1 point each)")
            grid 3 2:
                #style "skill_rows"
                spacing 10
                hbox:
                    text _("Strength: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.strength", playerSheet.strength+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.strength + charaCreationTempSkillMods[0]]")
                        if playerSheet.strength > 0:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.strength", playerSheet.strength-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Dexterity: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.dexterity", playerSheet.dexterity+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.dexterity + charaCreationTempSkillMods[1]]")
                        if playerSheet.dexterity > 0:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.dexterity", playerSheet.dexterity-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Constitution: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.constitution", playerSheet.constitution+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.constitution + charaCreationTempSkillMods[2]]")
                        if playerSheet.constitution > 0:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.constitution", playerSheet.constitution-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Intellect: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.intellect", playerSheet.intellect+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.intellect + charaCreationTempSkillMods[3]]")
                        if playerSheet.intellect > 0:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.intellect", playerSheet.intellect-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Charm: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.charm", playerSheet.charm+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.charm + charaCreationTempSkillMods[4]]")
                        if playerSheet.charm > 0:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.charm", playerSheet.charm-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Willpower: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.willPower", playerSheet.willPower+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.willPower + charaCreationTempSkillMods[5]]")
                        if playerSheet.willPower > 0:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.willPower", playerSheet.willPower-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
            label _("Secondary Skills(1 point each)")
            grid 4 3:
                spacing 10
                style_prefix "skill_rows"
                hbox:
                    text _("Insight: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.insight", playerSheet.insight+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.insight + charaCreationTempSkillMods[6]]")
                        if playerSheet.insight > -20:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.insight", playerSheet.insight-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Perception: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.perception", playerSheet.perception+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.perception + charaCreationTempSkillMods[7]]")
                        if playerSheet.perception > -20:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.perception", playerSheet.perception-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Craftsmenship: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.craftsmenship", playerSheet.craftsmenship+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.craftsmenship + charaCreationTempSkillMods[8]]")
                        if playerSheet.craftsmenship > -20:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.craftsmenship", playerSheet.craftsmenship-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Lockpicking: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.lockPicking", playerSheet.lockPicking+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.lockPicking + charaCreationTempSkillMods[9]]")
                        if playerSheet.lockPicking > -20:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.lockPicking", playerSheet.lockPicking-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Lore: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.lore", playerSheet.lore+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.lore + charaCreationTempSkillMods[10]]")
                        if playerSheet.lore > -20:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.lore", playerSheet.lore-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Survival: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.survival", playerSheet.survival+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.survival + charaCreationTempSkillMods[11]]")
                        if playerSheet.survival > -20:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.survival", playerSheet.survival-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Medicine: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.medicine", playerSheet.medicine+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.medicine + charaCreationTempSkillMods[12]]")
                        if playerSheet.medicine > -20:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.medicine", playerSheet.medicine-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Stealth: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.stealth", playerSheet.stealth+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.stealth + charaCreationTempSkillMods[13]]")
                        if playerSheet.stealth > -20:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.stealth", playerSheet.stealth-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Performance: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.performance", playerSheet.performance+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.performance + charaCreationTempSkillMods[14]]")
                        if playerSheet.performance > -20:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.performance", playerSheet.performance-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Slight Of Hand: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.slightOfHand", playerSheet.slightOfHand+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.slightOfHand + charaCreationTempSkillMods[15]]")
                        if playerSheet.slightOfHand > -20:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.slightOfHand", playerSheet.slightOfHand-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Intimidation: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.intimidation", playerSheet.intimidation+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.intimidation + charaCreationTempSkillMods[16]]")
                        if playerSheet.intimidation > -20:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.intimidation", playerSheet.intimidation-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
                hbox:
                    text _("Strategy: ")
                    vbox:
                        if skillPoints + charaCreationTempSkillMods[18] >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.strategy", playerSheet.strategy+1)]
                        else:
                            textbutton _("+"):
                                action SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.strategy + charaCreationTempSkillMods[17]]")
                        if playerSheet.strategy > -20:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.strategy", playerSheet.strategy-1)]
                        else:
                            textbutton _("-"):
                                action SetVariable("bottomText", "Minimum skill level")
            text _("")

style skill_rows_text is gui_text
style skill_rows_vbox is vbox
style skill_rows_hbox is hbox

style skill_rows_vbox:
    box_align 0.5
style skill_rows_hbox:
    box_align 0.5
style skill_rows_text:
    textalign 0.5
#style skill_col_two is hbox
#style skill_col_three is hbox
#
#style skill_col_one:
#    xalign 1
#style skill_col_two:
#    xalign 0.5
#style skill_col_three:
#    xalign 0.75

#style stats_label:
#    top_margin gui.pref_spacing
#    bottom_margin 3
#
#style stats_label_text:
#    yalign 1.0
#
#style stats_vbox:
#    xsize 338
#
#style stats_radio_vbox:
#    spacing gui.pref_button_spacing
#style stats_radio_button:
#    properties gui.button_properties("radio_button")
#    foreground "gui/button/radio_[prefix_]foreground.png"
#style stats_radio_button_text:
#    properties gui.text_properties("radio_button")


# Cosmetic appearance
screen defining_character_appearance():
    tag menu

    python:
        if playerSheet.height != "" and playerSheet.height[len(playerSheet.height)-1] != "." and playerSheet.height[0] != "." and "." in playerSheet.height:
            playerSheet.height = str(numeralRangeConstraints(float(playerSheet.race.raceHeight[0]), float(playerSheet.race.raceHeight[2]), float(playerSheet.height)))
            if playerSheet.build != "":
                playerSheet.getWeight()
    use character_creation_menu(_("defining_character_appearance"), scroll="viewport"):
        vbox:
            style_prefix "appearance_selection"
            label _("Body type")
            text "your character's height, weight and build will have some effect on gameplay, like a narrow passage that bulky or tall character might not be able to traverse or certain physical tasks like pushing over a pillar will be hard for shorter or leaner characters, even if they have good strength."
            text _("")
            hbox:
                spacing 20
                vbox:
                    text _(showRaceHeight(playerSheet.race.raceName))
                    input:
                        value VariableInputValue("playerSheet.height") 
                        length 15
                        default playerSheet.height
                    #    changed charaCreationSetHeight
                        allow "0123456789."
                    
                vbox:
                    text "please select your characters build"
                    viewport:
                        area (0, 0, 250, 400)
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            textbutton _("Gaunt") action SetVariable("playerSheet.build", "gaunt")
                            textbutton _("Skinny") action SetVariable("playerSheet.build", "skinny")
                            textbutton _("Lean") action SetVariable("playerSheet.build", "lean")
                            textbutton _("Lithe") action SetVariable("playerSheet.build", "lithe")
                            textbutton _("Average") action SetVariable("playerSheet.build", "average")
                            textbutton _("Broad") action SetVariable("playerSheet.build", "broad")
                            textbutton _("Bulky") action SetVariable("playerSheet.build", "bulky")
                            textbutton _("Thick") action SetVariable("playerSheet.build", "thick")
                            textbutton _("Obese") action SetVariable("playerSheet.build", "obese")
                vbox:
                    text _("Your weight is [playerSheet.weight] lbs")
            text _("")
            label "Face Details"
            text _("")

style appearance_selection_text is gui_text
style appearance_selection_hbox is hbox

style appearance_selection_text:
    size 25

style appearance_selection_hbox:
    box_justify True

style appearance_selection_label is gui_label
style appearance_selection_label_text is gui_label_text