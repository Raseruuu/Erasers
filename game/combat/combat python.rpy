init python:
    import pygame
    import math
    def tick():
        ## Defining global variables ##
        global timerpause

        global click
        global clickmax
        global mobhp
        global mobattacker

        global slow
        global burn

        global breezecd
        global soficd
        global flaircd
        global shield

        if timerpause == False:
            for i, j in enumerate(mob):
                if click[i] < mob[i].cd:
                    # if slow > 0:
                    #     click+=0.5
                    # else:
                    click[i] += 1
            # if slow > 0:
            #     slow -= 1
            # if burn[0] > 0:
            #     burn[0] -= 1
            #     mobhp[0] -= 0.05

            if breezecd < max(breeze.cost):
                breezecd +=0.05
            if soficd <max(sofi.cost):
                soficd +=0.05
            if flaircd <max(flair.cost):
                flaircd +=0.05

            if shield > 0:
                shield -=0.1
        else:
            pass
        for i,j in enumerate(mob):
            if click[i] == mob[i].cd:
                mobattacker = i
                renpy.call("breezehurt")

label sofiphase:
    # $ timerpause = True
    show screen damageincoming(skillvalues[act])

    if act == "Shield":
        $ shield += skillvalues["Shield"]
    if act == "Heal":
        $ hp = min(hpmax, hp+skillvalues["Heal"])

    $renpy.pause(2.0)
    hide screen damageincoming
    # $ timerpause = False
    jump combatloop

label damagephase:
    call flairhurt ##TODO: charge to targeted one.
    show screen damagecalc(skillvalues[act])
    show screen targetting

    $ renpy.pause(1.0)
    $ timerpause = False
    hide screen damagecalc


    ## Condition Check
    if mobhp[0]>0:
        jump combatloop
    else:
        jump victory

####################
## Hurt animation ##
####################
label flairhurt: ##TODO: to targetted
    # if act == "Shard":
    #     $ slow[target] = 100
    # if act == "Firebolt":
    #     $ burn[target] = 400
    $ mobhp[target] -= skillvalues[act]

    ## Cancel due to unable to hide specific one
    # hide screen mobicon
    # show screen mobicon(target, mobhurt) #at mobhurt

    return
label breezehurt:
    $ timerpause = True
    $ click[mobattacker] = 0

    $ hp=int(max(min(hp,hp-mob[mobattacker].dmg+shield), 0)+0.8)
    $ shield = max(shield-mob[mobattacker].dmg, 0)

    show screen damageincoming(mob[mobattacker].dmg)
    
    show breezecombat at mobhurt

    $ renpy.pause(1.0)

    $ timerpause = False
    hide screen damageincoming

    ## gameover check
    if hp ==0:
        jump gameover
    else:
        jump combatloop

####################
## BATTLE OUTCOME ##
####################
label victory:
    hide screen combat
    "You win"
    return
label gameover:
    hide screen combat
    scene black
    "You LOSE"
    return
