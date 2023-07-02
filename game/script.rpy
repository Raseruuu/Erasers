label start:
    $ combatroom = False
    jump prologue
    # jump combattest

    return

label startend: ## DEMO END
    scene black
    centered "To be continued..."
    stop sound
    stop music fadeout 1.0
    pause 1
    if persistent.combatunlock == None:
        "Combat Room Unlocked"
        $ persistent.combatunlock = True
    return

# ## CREDITS ##
# UI icons: https://kicked-in-teeth.itch.io/
# nameplate: Geometric_Dialogue_Boxes_by_ppppantsu
# textbox: Art_Deco_Fantasy_UI_PNG
# debuff icon: https://opengameart.org/content/95-game-icons sbed
# Combat Effects: Free to use battle cgs by Arimia
# ######
# Boss combat music:
# "Tanzanite" by bitter sweet entertainment
# "Over the Blood" by Youfulca
