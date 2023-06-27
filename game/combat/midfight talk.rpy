label midfight:
    $ mobphase = True
    $ timerpause = True
    $ combattalk = True
    $ renpy.call(midtalk)
    $ combattalk = False
    $ timerpause = False
    $ mobphase = False
    return

## Demo fight
label flairtalk:
    $ timerpause = True
    $ combattalk = True

    $ fighttalk = True
    f "Oh no"
    b "Haha"
    window hide

    $ combattalk = False
    $ timerpause = False
    return


################
## RATS FIGHT ##
################
label ratrespawn:
    hide screen combat
    show screen combat
    python:
        if ratkilled == 1:
            midtalk = "ratnew"
            renpy.call("midfight") ## first reappear
        if fighttalk == False and ratkilled == 3:
            midtalk = "rattalk"
            renpy.call("midfight") ## Flair joins in.
        if ratkilled >=9:
            midtalk = "ratlast"
            renpy.call("midfight")
    jump combatloop
label ratnew:
    show screen combat
    "New Vibrant infested Rat appears!"
    b "Tssk"
    window hide
    return

label rattalk:
    show screen combat
    $ fighttalk = True

    s "there's just no end to them!"
    b "gdi what's this bs"
    f "Need a hand?"
    b "Yeah sure what can you do?"

    $ combatant.append(flair)
    $ flaircd = 0
    ## show flair joins party

    hide screen combat
    show screen combat with dissolve
    window hide
    return

label ratlast:
    show screen combat
    b "I think that's almost the last of them"
    f "Right, I just need to clear them all out in one go"
    b "Got it!"
    window hide
    return
####################
## ALV FIGHT ##
####################
label alvstart:
    b "It's okay, I've got this."
    hide screen combat
    hide black
    hide breezecombat
    with dissolve
    play music tanzanite volume 1.0 fadein 1
    show iceblue with Dissolve(1.5):
        alpha 0.5
    $ combatant[0] = breezeex
    show screen combat
    show breezecombat: ## breeze icon
        xpos 450 yanchor 1.0 ypos 1050
    pause 1.0
    return
####################
## Azmaveth FIGHT ##
####################
label aztalk: ## triggered half-time

    $ fighttalk = True
    b "this guy is tough"
    f "hang in there!"
    a "Damn, guess I'm not punching you hard enough."
    "Az flexes, and you can see him assumes a more streamlined stance."
    "Something tells Breeze that this will only get more difficult."
    show screen textoutcome("Azmaveth speeds up")
    a "You ready for this?????"
    hide screen textoutcome
    window hide
    $ mobstat[0][6] = 40
    $ mobstat[0][4] = max(0, mobstat[0][4]-40)
    return

label azwin:
    $ timerpause = True
    $ combattalk = True

    hide screen combat
    hide screen parry
    show azmob at combat2:
        xpos 960
    b "Did we win?"
    hide azmob with dissolve

    jump victory
