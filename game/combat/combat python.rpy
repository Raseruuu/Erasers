init python:
    import pygame
    import math ## This one is probably not used. TODO: consider removal.
    def tick():
        ## Defining global variables ##
        global timerpause

        global mobattacker ## which incoming attack.
        global mobaction ## for attempting queuing up mob actions.

        global slow
        global burn

        global breezecd
        global soficd
        global flaircd
        global shield

        if timerpause == False:
            for i, j in enumerate(mobstat): ## individual timer.
                if mobstat[i][4] < mobstat[i][6]:
                    if mobstat[i][2] > 0:
                        mobstat[i][4]+=0.25
                    else:
                        mobstat[i][4] += 1
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

        for i,j in enumerate(mobstat): ## Assigning mob actions when timer up.
            if mobstat[i][4] == mobstat[i][6]:
                timerpause = True

                for i,j in enumerate(mobstat):
                    if mobstat[i][4] == mobstat[i][6]:
                        mobaction.append(i)
                        mobstat[i][4] = 0
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

label damagephase: ## damaging enemies
    python:
        targettemp = target

        breezeaction = []
        if act == "Inferno":
            # for i in mobstat:
            #     breezeaction.append("Inferno")
            breezeaction = [act]

        else:
            breezeaction = [act]



    call breezeaction ## STATS hp/slow/burn

    $ target = targettemp


    ## Condition Check ##
    if mobstat[target][1]==0:
        if len(mobstat)== 1:
            jump victory
        elif len(mobstat) >1:
            jump mobdeath
    else:
        jump combatloop

###################
## Hurt SEQUENCE ##
###################
label breezeaction:
    ## call animation in here
    python:
        if act == "Inferno":

            # renpy.call("mobhurt")
            # target = 1
            # renpy.call("mobhurt")
            # target = 2
            # renpy.call("mobhurt")

            # for i, j in enumerate(breezeaction):  ## breezeaction = ["Inferno", "Inferno", "Inferno"]
            #     target = i
                # renpy.call("mobhurt")
            for i in range(len(mobstat)):
                target = i
                renpy.call("mobhurt")

        else:
            # breezeaction.pop(0)
            renpy.call("mobhurt")
    return


label mobhurt: ## INDIVIDUAL mob being hit + animation
    $ timerpause = True
    ## HP
    $ mobstat[target][1] = max(0, mobstat[target][1] - skillvalues[act])
    ## Currently no debuff stacking
    # if act == "Shard":
    #     $ slow[target] = 100
    # if act == "Firebolt":
    #     $ burn[target] = 400

    ## TODO: find a way to show mob hurt shaking animation.

    show screen damagecalc(skillvalues[act]) ## ANIMATION
    $ renpy.pause(1.0)
    $ timerpause = False
    hide screen damagecalc
    return
#####
label mobaction:
    $ mobphase = True
    python:
        if len(mobaction) != 0: ##if there's still atk incoming
            mobattacker = mobaction[0]
            mobaction.pop(0)
            renpy.call("breezehurt")
    $ mobphase = False
    jump combatloop

label breezehurt: ## ANIMATION
    $ timerpause = True

    $ mobstat[mobattacker][4] = 0 ##reset the cd of the attacking mob.
    ## hp and shield value adjustment. & damage number.
    $ hp=int(max(min(hp,hp-mobstat[mobattacker][5]+shield), 0)+0.8)
    $ shield = max(shield-mobstat[mobattacker][5], 0)

    show screen mobattacking(mobattacker) ## attack indicator
    show screen damageincoming(mobstat[mobattacker][5]) ## dmg number
    with vpunch
    # show breezecombat at mobhurt

    $ renpy.pause(1.0)
    $ timerpause = False
    hide screen damageincoming
    hide screen mobattacking

    ## gameover check
    if hp ==0:
        jump gameover
    else:
        jump mobaction ##loops back and check python again.

####################
## BATTLE OUTCOME ##
####################
label mobdeath: ## remove dead enemy
    hide screen combat
    if encounter == "Rat": ##TODO: Tweak function so that it knows when all 3 are dead.
        # for i, j in mobstat:
        #     if mobstat[i][1] ==0:
        #         pass
        # else:
        $ mobstat[target] = [mob[target].name, (mob[target].hp)//2, 0, 0, 0, mob[target].dmg, mob[target].cd]
    else:
        $ mobstat.pop(target)
        $ target = 0
    show screen combat

    jump combatloop

label victory:
    hide screen combat
    "You win"
    stop music fadeout 1.0
    return
label gameover:
    hide screen combat
    scene black
    "You LOSE"
    return
