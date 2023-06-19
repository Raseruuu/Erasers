init python:
    import pygame
    import math ## This one is probably not used. TODO: consider removal.
    def tick():
        ## Defining global variables ##
        global timerpause

        global click ## individual monster's timer TODO:standardise into mobstat
        global mobattacker ## which incoming attack. TODO: streamline/remove here.
        global mobaction ## for attempting queuing up mob actions.

        global slow
        global burn

        global breezecd
        global soficd
        global flaircd
        global shield

        if timerpause == False:
            for i, j in enumerate(mob): ## individual timer.
                if click[i] < mob[i].cd:
                    if mobstat[i][2] > 0:
                        click+=0.25
                    else:
                        click[i] += 1
            # if mobstat[i][2] > 0: ## slow
            #     mobstat[i][2] -= 1
            # if mobstat[i][3] > 0: ## burn
            #     mobstat[i][3] -= 1
            #     mobstat[i][1] -= 0.05

            ## Commmand card timers.
            if breezecd < max(breeze.cost):
                breezecd +=0.05
            if soficd <max(sofi.cost):
                soficd +=0.05
            if flaircd <max(flair.cost):
                flaircd +=0.05
            if shield > 0: ## Shield Decay
                shield -=0.05
        else:
            pass

        for i,j in enumerate(mob): ## Assigning mob actions when timer up.
            if click[i] == mob[i].cd:

                timerpause = True
                for i,j in enumerate(mob):
                    if click[i] == mob[i].cd:
                        mobaction.append(i)
                renpy.call("mobaction")

                ##### OLD CODE for this section
                # mobattacker = i
                # renpy.call("breezehurt")

    ## Functions for testing purposes.
    def autoattack():
        global mobstat
        mobstat[target][1] -= 700
    def burning():
        global mobstat
        mobstat[target][3] +=400
    def icing():
        global mobstat
        mobstat[target][2] +=400

label sofiphase:
    # $ timerpause = True
    show screen damageincoming(skillvalues[act]) ##TODO change to green textcolor.

    if act == "Shield":
        $ shield += skillvalues["Shield"]
    if act == "Heal":
        $ hp = min(hpmax, hp+skillvalues["Heal"])

    $renpy.pause(2.0)
    hide screen damageincoming
    # $ timerpause = False
    jump combatloop

label damagephase:
    call mobhurt
    show screen damagecalc(skillvalues[act]) ##damage numbers

    $ renpy.pause(1.0)
    $ timerpause = False
    hide screen damagecalc

    ## Condition Check
    if mobstat[target][1]>0:
        jump combatloop
    else:
        jump victory

####################
## Hurt animation ##
####################
label mobhurt: ##TODO: to targetted
    ## HP
    $ mobstat[target][1] = max(0, mobstat[target][1] - skillvalues[act])
    ## Currently no debuff stacking
    # if act == "Shard":
    #     $ slow[target] = 100
    # if act == "Firebolt":
    #     $ burn[target] = 400

    ## Defunct due to unable to hide specific one.
    ## TODO: find a way to show mob hurt shaking animation.
    # hide screen mobicon
    # show screen mobicon(target, mobhurt) #at mobhurt
    return

label mobaction:
    python:
        for i, j in enumerate(mobaction):
            mobattacker = i
            renpy.call("breezehurt")
            renpy.pause(1.0)
        mobaction = []
    jump combatloop

label breezehurt: ##Each mob action
    $ timerpause = True
    $ click[mobattacker] = 0 ##reset the cd of the attacking mob.
    ## hp and shield value adjustment. & damage number.
    $ hp=int(max(min(hp,hp-mob[mobattacker].dmg+shield), 0)+0.8)
    $ shield = max(shield-mob[mobattacker].dmg, 0)
    show screen damageincoming(mob[mobattacker].dmg)

    with vpunch
    # show breezecombat at mobhurt

    $ renpy.pause(1.0)
    $ timerpause = False
    hide screen damageincoming

    ## gameover check
    if hp ==0:
        jump gameover
    return

####################
## BATTLE OUTCOME ##
####################
label mobdeath: ## if multiple enemies.
    # if len(mobstat)>0:
    $ mobstat.pop(target)
    if len(mobstat) == 0:
        hide screen targetting
    hide screen combat
    show screen combat
    # if len(mobstat)>0:
    #     jump combatloop
    # else:
    jump victory
label victory:
    hide screen combat
    "You win"
    return
label gameover:
    hide screen combat
    scene black
    "You LOSE"
    return
