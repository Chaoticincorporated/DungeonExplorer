init 2 python:
    bottomText = ""
    # index 0-5 are the core skills, 6-17 are the secondary skills, 18 is skill points
    charaCreationTempSkillMods = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    def setTempRacialBonuses(raceSkillBonus):
        skillArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for bonus in raceSkillBonus:
            for skill in range(len(playerSheet.skills)+1):
                if skill < 18:
                    if playerSheet.skills[skill][0] == bonus[0]:
                        skillArray[skill] += bonus[1]
                        break
                else:
                    if bonus[0] == "skillPoints":
                        skillArray[skill] += bonus[1]
                        break
        return skillArray
    def setMinSkillLv(skillIndex):
        if skillIndex <= 5:
            return 0
        elif skillIndex <= 17:
            return -20
    def calculateSkillPointValue(skillLv):
        if skillLv <= -10:
            return 2
        elif skillLv <= 10:
            return 1
        elif skillLv <= 20:
            return 2
        elif skillLv <= 30:
            return 3
        else:
            return 5
    
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
            label _("Skills")
            grid 3 6:
                python:
                    skillBonusIndex = 0
                for skill in playerSheet.skills:
                    vbox:
                        text _("[skill[0].capitalize()]")
                        hbox:
                            if skill[1] > setMinSkillLv(skillBonusIndex):
                                textbutton _("-") action [SetVariable("skillPoints", skillPoints+calculateSkillPointValue(skill[1])), SetDict(playerSheet.skills[skillBonusIndex], 1, skill[1]-1)]
                            else:
                                textbutton _("-"):
                                    action SetVariable("bottomText", "Minimum skill level")
                            text _("<[skill[1] + charaCreationTempSkillMods[skillBonusIndex]]>")
                            if skillPoints + charaCreationTempSkillMods[18] >= calculateSkillPointValue(skill[1]):
                                textbutton _("+") action [SetVariable("skillPoints", skillPoints-calculateSkillPointValue(skill[1]+1)), SetDict(playerSheet.skills[skillBonusIndex], 1, skill[1]+1)]
                            else:
                                textbutton _("+"):
                                    action SetVariable("bottomText", "Not enough skill points")
                    python:
                        skillBonusIndex += 1
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