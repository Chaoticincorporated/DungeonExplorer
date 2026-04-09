init python:
    bottomText = ""
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
        
        text _("Skill Points: [skillPoints]")
        textbutton _("General") action ShowMenu("general_details")
        textbutton _("Appearance") action ShowMenu("defining_character_appearance")
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
                        textbutton _("Human") action [SetVariable("playerSheet.race", "human"), SetVariable("bottomText", raceDesc("human"))]
                        textbutton _("Elf") action [SetVariable("playerSheet.race", "elf"), SetVariable("bottomText", raceDesc("elf"))]
                        textbutton _("Dwarf") action [SetVariable("playerSheet.race", "dwarf"), SetVariable("bottomText", raceDesc("dwarf"))]
                        textbutton _("Orc") action [SetVariable("playerSheet.race", "orc"), SetVariable("bottomText", raceDesc("orc"))]
                        textbutton _("Halfling") action [SetVariable("playerSheet.race", "halfling"), SetVariable("bottomText", raceDesc("halfling"))]
                        textbutton _("Arenae") action [SetVariable("playerSheet.race", "arenae"), SetVariable("bottomText", raceDesc("arenae"))]
                        textbutton _("Harpy") action [SetVariable("playerSheet.race", "harpy"), SetVariable("bottomText", raceDesc("harpy"))]
                        textbutton _("Oviur") action [SetVariable("playerSheet.race", "oviur"), SetVariable("bottomText", raceDesc("oviur"))]
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
            label _("Core Skills(1 point each)")
            hbox:
                #style "skill_rows"
                hbox:
                    style "skill_col_one"
                    text _("Strength: ")
                    vbox:
                        if skillPoints >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.strength", playerSheet.strength+1)]
                        else:
                            textbutton _("+"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.strength]")
                        if playerSheet.strength > 1:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.strength", playerSheet.strength-1)]
                        else:
                            textbutton _("-"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Minimum skill level")
                hbox:
                    style "skill_col_two"
                    text _("Dexterity: ")
                    vbox:
                        if skillPoints >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.dexterity", playerSheet.dexterity+1)]
                        else:
                            textbutton _("+"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.dexterity]")
                        if playerSheet.dexterity > 1:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.dexterity", playerSheet.dexterity-1)]
                        else:
                            textbutton _("-"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Minimum skill level")
                hbox:
                    style "skill_col_three"
                    text _("Constitution: ")
                    vbox:
                        if skillPoints >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.constitution", playerSheet.constitution+1)]
                        else:
                            textbutton _("+"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.constitution]")
                        if playerSheet.constitution > 1:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.constitution", playerSheet.constitution-1)]
                        else:
                            textbutton _("-"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Minimum skill level")
            hbox:
                #style "skill_rows"
                hbox:
                    style "skill_col_one"
                    text _("Intellect: ")
                    vbox:
                        if skillPoints >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.intellect", playerSheet.intellect+1)]
                        else:
                            textbutton _("+"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.intellect]")
                        if playerSheet.intellect > 1:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.intellect", playerSheet.intellect-1)]
                        else:
                            textbutton _("-"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Minimum skill level")
                hbox:
                    style "skill_col_two"
                    text _("Charm: ")
                    vbox:
                        if skillPoints >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.charm", playerSheet.charm+1)]
                        else:
                            textbutton _("+"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.charm]")
                        if playerSheet.charm > 1:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.charm", playerSheet.charm-1)]
                        else:
                            textbutton _("-"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Minimum skill level")
                hbox:
                    style "skill_col_three"
                    text _("Willpower: ")
                    vbox:
                        if skillPoints >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.willPower", playerSheet.willPower+1)]
                        else:
                            textbutton _("+"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.willPower]")
                        if playerSheet.willPower > 1:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.willPower", playerSheet.willPower-1)]
                        else:
                            textbutton _("-"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Minimum skill level")
            label _("Secondary Skills(1 point each)")
            hbox:
                #style "skill_rows"
                hbox:
                    style "skill_col_one"
                    text _("Insight: ")
                    vbox:
                        if skillPoints >= 1:
                            textbutton _("+") action [SetVariable("skillPoints", skillPoints-1), SetVariable("playerSheet.insight", playerSheet.insight+1)]
                        else:
                            textbutton _("+"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Not enough skill points")
                        text _("[playerSheet.insight]")
                        if playerSheet.insight > 0:
                            textbutton _("-") action [SetVariable("skillPoints", skillPoints+1), SetVariable("playerSheet.insight", playerSheet.insight-1)]
                        else:
                            textbutton _("-"):
                                action NullAction()
                                hovered SetVariable("bottomText", "Minimum skill level")
            text _("")

style skill_col_one is hbox
style skill_col_two is hbox
style skill_col_three is hbox

style skill_col_one:
    xalign 1
style skill_col_two:
    xalign 0.5
style skill_col_three:
    xalign 0.75

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
    use character_creation_menu(_("defining_character_appearance"), scroll="viewport"):
        hbox:
            style_prefix "appearance_selection"
            label _("Character Appearance [playerSheet.gender]")

style appearance_selection_label is gui_label
style appearance_selection_label_text is gui_label_text