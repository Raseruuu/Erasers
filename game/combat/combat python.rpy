init python:
    import pygame
    def ticking():
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

        global encounter
        global aztimer

        if timerpause == False:
            for i, j in enumerate(mobstat): ## individual timer.
                if mobstat[i][4] < mobstat[i][6]:
                    if mobstat[i][2] > 0:
                        mobstat[i][4]+=0.25 ## 0.25x speed
                    else:
                        mobstat[i][4] += 1
            if mobstat[i][2] > 0: ## slow
                mobstat[i][2] -= 1 ## lasts slow/20 seconds
            if mobstat[i][3] > 0: ## burn
                mobstat[i][3] -= 1 #lasts burn/20 seconds
                mobstat[i][1] -= 0.05 # 1hp/second

            ## Commmand card timers.
            if breezecd < max(breeze.cost):
                breezecd +=0.05
            if soficd <max(sofi.cost):
                soficd +=0.05
            if flaircd <max(flair.cost):
                flaircd +=0.05
            if shield > 0: ## Shield Decay
                shield -=0.05

        ## Assigning mob actions when timer up.
        for i,j in enumerate(mobstat):
            if mobstat[i][4] >= mobstat[i][6]:
                timerpause = True
                for i,j in enumerate(mobstat):
                    if mobstat[i][4] >= mobstat[i][6]:
                        mobaction.append(i)
                        mobstat[i][4] = 0
                renpy.call("mobaction")

        ## az timer
        if encounter == "Az" and timerpause == False:
            aztimer -=1
        if aztimer == 2200 and fighttalk == False:
            renpy.call("aztalk")
        if aztimer <= 0:
            renpy.jump("azwin")


    ## Functions for testing purposes.
    def burning():
        global mobstat
        mobstat[target][3] +=400
    def icing():
        global mobstat
        mobstat[target][2] +=400
    def nothing():
        pass

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
            atksound = inferno
            for i in mobstat:
                breezeaction.append("Inferno")
        else:
            breezeaction = [act]

    call breezeaction ## STATS hp/slow/burn

    $ target = targettemp

    ## End Condition Check ##
    python:
        death = []
        for i, j in enumerate(mobstat):
            if mobstat[i][1]<=0:
                death.append(i)
    if len(death) >=1:
        if len(mobstat)== 1: ## single enemy
            jump victory
        elif len(mobstat) >1: ## Group fight
            jump mobdeath
    else:
        jump combatloop

###################
## Hurt SEQUENCE ##
###################
label breezeaction:
    ## call animation in here
    python:
        if len(breezeaction) != 0:
            if act == "Inferno":
                target = len(mobstat)-len(breezeaction)
                breezeaction.pop(0)
                renpy.call("mobhurt")
            else:
                breezeaction.pop(0)
                target = targettemp
                renpy.call("mobhurt")
    return

label mobhurt: ## INDIVIDUAL mob being hit + animation
    $ timerpause = True
    hide screen targetting
    play sound atksound

    ## HP
    $ mobstat[target][1] = max(0, mobstat[target][1] - skillvalues[act])
    ## debuff no stacking, just reset to max
    if act == "Shard":
        $ mobstat[target][2] = 100 ## slow for 5s, 0.25rate
        if encounter == "Az":
            $ mobstat[target][2] = 50
    if act == "Firebolt":
        $ mobstat[target][3] = 400 ## burn 20s, 20hp

    ## TODO: spell/attack animations here

    show screen damagecalc(skillvalues[act]) ## ANIMATION
    $ renpy.pause(1.0)
    $ timerpause = False
    hide screen damagecalc
    # show screen targetting(mobpos[len(mobstat)][target])
    jump breezeaction

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

    if encounter == "Az":
        play sound swish9 volume 5.0
        call parry
    else:
        $ mobdamage = mobstat[mobattacker][5]

    with vpunch   # show breezecombat at mobhurt ##abandoned
    play sound hitsound
    # if iceshield > 0:
    #     play sound iceshatter

    if encounter == "Az" and iceshield >0:
        $ mobdamage = mobdamage//2
        $ hp=int(max(min(hp,hp-mobdamage), 0)+0.8)
        $ iceshield = 0
    else:
    ## hp and shield value adjustment. & damage number.
        $ hp=int(max(min(hp,hp-mobdamage+shield), 0)+0.8)
        $ shield = max(shield-mobdamage, 0)

    show screen mobattacking(mobattacker) ## attack indicator
    show screen damageincoming(mobdamage) ## dmg number



    $ renpy.pause(1.0)
    if encounter == "Az":
        hide screen parry
        hide screen textoutcome
        $ breezecd -=1
        $ tick = 0
        $ parrypause = False
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
label mobdeath: ## dead replace/removal in group
    hide screen combat
    python:
        if encounter == "Rat":
            if all([mobstat[i][1] == 0 for i, j in enumerate(mobstat)]) and ratkilled >=9 : ## when all 3 are dead after killing 9
                renpy.jump("victory")
            else:
                for i in death: ## i is positions
                    mobstat[i] = [mob[i].name, (mob[i].hp), 0, 0, 0, mob[i].dmg, mob[i].cd] ## Rat replacement

                    ratkilled += 1
                    if ratkilled == 1:
                        renpy.call("ratnew") ## first reappear
                    if fighttalk == False and ratkilled == 3:
                        renpy.call("rattalk") ## Flair joins in.
                    if ratkilled >=9:
                        renpy.call("ratlast")
        else:
            mobstat.pop(death)
            target = 0
    show screen combat

    jump combatloop

label victory: ## TODO: have encounter specific victory
    hide screen combat with dissolve
    stop music fadeout 1.0
    "You win"
    return
label gameover:
    hide screen combat
    scene black
    "You LOSE"
    menu:
        "Retry?"
        "Yes":
            jump combat
        "No":
            return
