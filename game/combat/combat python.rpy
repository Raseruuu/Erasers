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

        if timerpause == False:
            for i, j in enumerate(mobstat): ## individual timer.
                if mobstat[i][4] < mobstat[i][6]:
                    if mobstat[i][2] > 0:
                        mobstat[i][4]+=0.25
                    else:
                        mobstat[i][4] += 1
            if mobstat[i][2] > 0: ## slow
                mobstat[i][2] -= 1 ## lasts slow/20 seconds
            # if mobstat[i][3] > 0: ## burn
            #     mobstat[i][3] -= 1 #lasts burn/20 seconds
            #     mobstat[i][1] -= 0.05 #

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

    ## Functions for testing purposes.
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
            for i in mobstat:
                breezeaction.append("Inferno")

        else:
            breezeaction = [act]

    call breezeaction ## STATS hp/slow/burn

    $ target = targettemp


    ## Condition Check ##
    python:
        death = []
        for i, j in enumerate(mobstat):
            if mobstat[i][1]<=0:
                death.append(i)
    if len(death) >=1:
    # if mobstat[target][1]==0:
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
    ## HP
    $ mobstat[target][1] = max(0, mobstat[target][1] - skillvalues[act])
    ## Currently no debuff stacking
    if act == "Shard":
        $ mobstat[target][2] = 100 ##reset to max
    if act == "Firebolt":
        $ mobstat[target][3] = 400

    ## TODO: find a way to show mob hurt shaking animation.

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
label mobdeath: ## dead replace/removal in group
    hide screen combat
    python:
        if encounter == "Rat":
            if all([mobstat[i][1] == 0 for i, j in enumerate(mobstat)]): ## when all 3 are dead
                renpy.jump("victory")
            else:
                for i in death: ## i is positions
                    mobstat[i] = [mob[i].name, (mob[i].hp), 0, 0, 0, mob[i].dmg, mob[i].cd] ## Rat replacement
                    ratkilled += 1
                    if ratkilled == 1:
                        renpy.call("ratnew") ## first reappear
                    if fighttalk == False and ratkilled == 3:
                        renpy.call("rattalk") ## Flair joins in.
        else:
            mobstat.pop(death)
            target = 0
    show screen combat

    jump combatloop

label victory: ## TODO: have encounter specific victory
    hide screen combat
    stop music fadeout 1.0
    "You win"
    return
label gameover:
    hide screen combat
    scene black
    "You LOSE"
    return

###################
## MIDFIGHT talk ##
###################
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

label ratnew:
    show screen combat
    $ timerpause = True
    $ combattalk = True

    "New Vibrant infested Rat appears!"
    b "tssk"
    window hide

    $ combattalk = False
    $ timerpause = False
    return

label rattalk:
    show screen combat
    $ timerpause = True
    $ combattalk = True

    $ fighttalk = True
    s "there's just no end to them!"
    b "gdi what's this bs"
    f "Need a hand?"
    b "Yeah sure what can you do?"
    $ combatant.append(flair)
    window hide
    ## show flair joins party

    $ combattalk = False
    $ timerpause = False
    return
