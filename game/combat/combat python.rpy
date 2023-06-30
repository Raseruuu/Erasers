label combattest: ## simulate going into a combat from story.
    "entering combat"
    $ encounter = "Goons"
    call precombat
    return
    # menu:
    #     # "Pick encounter"
    #     "Goons":
    #         $ encounter = "Goons"
    #     "Rats":
    #         $ encounter = "Rats"
    #     "Corrupted":
    #         $encounter = "Alv"
    #     "Az":
    #         $encounter = "Az"

label precombat:
    $ combatant = combatantlist[encounter]
    $ tutorial = 1 ##remove later
    call combat

    label endcombat:
        $ _skipping = True
        $ _game_menu_screen = "save_screen"
        $ quick_menu = True

        scene black with dissolve
        "combat end"
    # $ renpy.fix_rollback()
    return


label combat:
    window hide
    hide screen skip_indicator
    hide screen quickhover
    $ quick_menu = False

    python:
        _skipping = timerpause = combattalk = False
        # _game_menu_screen = None ##TODO: uncomment when shipping

        ## Breeze's hp/hpmax/shield
        hpmax = hp = 1000
        shield = shieldtime = 0
        breezeaction = []
        act = ""
        atkdamage = 0
        sofibuff = 1
        breezecd = soficd = flaircd = 0.00
        ## mob's listing and action and phase
        mob = moblist[encounter] ## copying the monsters from encounter tag. (check combat data)
        mobaction = []
        mobphase = False
        mobstat = []
        alvbuff = []
        for i in mob:
            mobstat.append([i.name, i.hp, 0, 0, 0, i.dmg, i.cd, i.hp, 0, 0]) ##slow/burn/click/dmg/cdmax/hpmax / respawn(8) / freeze(9) /
        mobdamage = 0 ## each incoming damage
        mobregen = 0




        ##combat related variables
        mobattacker = None #the enemy that's attacking
        target = targettemp = 0 ## the enemy being attacked
        hitsound = hit
        atksound = blade
        desc = None
        descpos = 750

        ## Midfight talks
        fighttalk = False
        ratkilled = 0

        if encounter == "Alv":
            mobregen = 0.1 ##2hp/sec regen
            alvkill = 0
            alvheads = [0, 2, 2, 0]
            alvnone = 0
            targettemp = 1
            for i, j in enumerate(mobstat):
                j[1] = j[1]#-100 (starting hp, buffer before zeal)
                j.extend([0, 0]) ## alvbuff/regen (10, 11)
            mobstat[0][11] = 2
        ## Az
        aztimer = 2400 ##2400 in fullgame
        iceshield = 0


    ## Arts
    # scene bg_city_destroyed
    show black:
        alpha 0.8

    show screen combat ## main screen
    show breezecombat: ## breeze icon
        xpos 490 yanchor 1.0 ypos 1050

    if encounter == "Az":
        play music overtheblood volume 1.0 fadein 1
    elif encounter == "Alv":
        $ midtalk = "alvstart"
        call midfight
    else:
        play music battle volume 1.0 fadein 0.5

    if persistent.firsttime == True and encounter == "Goons":
        $ timerpause = True
        show screen tutorial
    ##########################################################################################
    ## the main label where things goes ##
    label combatloop:
        # $ renpy.block_rollback() ##stops rollback from here on

        ## Midfight Narration trigger
        # if encounter == "Flair" and mobstat[0][1] < (flairmob.hp)//2 and fighttalk == False:
        #     # call flairtalk
        #     $ midtalk = "flairtalk"
        #     $ renpy.call("midfight")
            # pass
        pause ##gameplay here

    return

####################################################################################
##
####################################################################################

label sofiphase:
    $ timerpause = True
     ##TODO change to green textcolor.
    if act == "Shield":
        show screen atkshield
        pause 0.2
        $ shield += skillvalues["Shield"]

    if act == "Heal":
        $ hp = min(hpmax, hp+skillvalues["Heal"])
        # show screen atkheal
        show screen damageincoming(skillvalues[act], "#00FF00")
    $renpy.pause(1.0)
    hide screen damageincoming
    hide screen atkshield
    $ timerpause = False
    jump combatloop

label damagephase: ## damaging enemies
    python:
        # targettemp = target
        target == targettemp

        breezeaction = []
        if act == "Inferno":
            atksound = None
            for i in mobstat:
                breezeaction.append("Inferno")
        elif act == "Blizzard":
            # atksound = blizzard
            for i in mobstat:
                atksound = None
                breezeaction.append("Blizzard")
        else:
            breezeaction = [act]

    if act == "Inferno": ##animation
        show screen atkinferno()
        play sound inferno
    if act == "Blizzard":
        show screen atkblizzard
        play sound blizzard

    call breezeaction ## STATS hp/slow/burn
    $ mobphase == False
    ## End Condition Check ##
    python:
        death = []
        for i, j in enumerate(mobstat):
            if mobstat[i][1]<=0 and mobstat[i][0] != "None": ## if there's a 0hp
                death.append(i)
                if encounter == "Alv":
                    alvkill +=1
                if encounter == "Goon":
                    midtalk = "goontute2"
                    renpy.call("midfight")

    if len(death) >=1: ##if there's death
        if len(mobstat) - len([item for item in mobstat if item[0] == "None"]) == 1: ## single enemy remaining
            jump victory
        elif len(mobstat) - len([item for item in mobstat if item[0] == "None"]) >1: ## multiple remaining
            jump mobdeath
    else:
        jump combatloop

###################
## Hurt SEQUENCE ##
###################
label breezeaction:
    $ mobphase = True
    ## call animation in here
    python:
        if len(breezeaction) != 0:
            if act == "Inferno" or act == "Blizzard":
                if mobstat[(len(mobstat)-len(breezeaction))][0] == "None": ## skip none
                    breezeaction.pop(0)
                    renpy.jump("breezeaction")
                else:
                    target = len(mobstat)-len(breezeaction)
                    breezeaction.pop(0)
                    renpy.call("mobhurt")
            else:
                breezeaction.pop(0)
                target = targettemp
                renpy.call("mobhurt")
    $ mobphase = False
    return

label mobhurt: ## INDIVIDUAL mob being hit + animation
    $ timerpause = True
    hide screen targetting

    if act == "Attack":
        show screen atkblade(target)
        if mobstat[targettemp][9] > 0:
            $ atksound = shattering
        else:
            $ atksound = blade
    if act == "Shard":
        show screen atkshard(target)
        $ atksound = ice
    if act == "Firebolt":
        show screen atkfirebolt(target)
        $ atksound = firebolt

    ###################
    play sound atksound
    ###################

    $ atkdamage = skillvalues[act]*sofibuff
    ## debuff no stacking, just reset to max
    if act == "Attack":
        $ atkdamage += mobstat[target][9]*5 ## adjust the modifier later
        if mobstat[target][9]> 0:
            call shattering
            $ mobstat[target][9] = 0
    if act == "Shard":
        if encounter == "Az":
            $ mobstat[target][2] = 50
        elif encounter == "Alv":
            $ mobstat[target][2] = 200
        else:
            $ mobstat[target][2] = 100 ## slow for 5s, 0.25rate

    if act == "Firebolt":
        $ mobstat[target][3] = 400 ## burn 20s, 20hp
    python:
        if act == "Blizzard":
            for i, j in enumerate(mobstat):
                if mobstat[i][2] != 0:
                    mobstat[i][9] = mobstat[i][2]



    ## TODO: spell/attack animations here
    $ renpy.pause(0.25)
    ## ANIMATION
    show screen damagecalc(atkdamage)
    $ renpy.pause(0.75)

    hide screen atkblade
    hide screen atkshard
    hide screen atkblizzard
    hide screen atkfirebolt
    hide screen atkinferno

    $ timerpause = False
    stop sound
    hide screen damagecalc


    ## HP
    $ mobstat[target][1] = max(0, mobstat[target][1] - atkdamage)
    $ mobstat[target][7] = max(0, mobstat[target][7] - (atkdamage//2))


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
        show punchpre onlayer screens
        play sound swish9 volume 5.0

        call parry
        play sound hitsound
        hide punchparry onlayer screens with Dissolve(0.2)
        hide punchpre onlayer screens with Dissolve(0.1)
        hide punchpost onlayer screens with Dissolve(0.1)
        hide screen parry

    elif encounter == "Alv":
        # $ mobdamage = mobstat[mobattacker][5] + int(mobstat[mobattacker][10]) ## buffs
        # $ mobdamage = mobstat[mobattacker][5]*(mobstat[mobattacker][1]//500)+100
        $ mobdamage = int(mobstat[mobattacker][5]*(1-((mobstat[mobattacker][2])/200.00)))
        # $ mobdamage = mobstat[mobattacker][5]
    else:
        $ mobdamage = mobstat[mobattacker][5]




    if encounter == "Az" and iceshield >0:
        $ mobdamage = mobdamage//2
        $ hp=int(max(min(hp,hp-mobdamage), 0)+0.8)
        $ iceshield = 0
    else:
    ## hp and shield value adjustment. & damage number.
        $ hp=int(max(min(hp,hp-mobdamage+shield), 0)+0.8)
        $ shield = max(shield-mobdamage, 0)

    # show mob(mobattacker, mobpos[3][i], textpopup)
    # show screen mobattacking(mobattacker) ## attack indicator
    show screen damageincoming(mobdamage, "#FF0000") ## dmg number

    with vpunch   # show breezecombat at mobhurt ##abandoned
    if encounter != "Az":
        play sound hitsound
    # if iceshield > 0:
    #     play sound iceshatter

    $ renpy.pause(1.0)
    if encounter == "Az":
        hide screen textoutcome
        $ breezecd = max(0, breezecd-1)
        $ tick = 0
        $ parrypause = False

    $ timerpause = False
    $ mobattacker = None
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
    hide screen targetting
    python:
        if encounter == "Goons":
            for i in death:
                goonleft = [g1, g2][abs(i-1)]
                midtalk = "goontute2"
                renpy.call("midfight")

            # target = 0

        if encounter == "Rat":
            if all([mobstat[i][1] == 0 for i, j in enumerate(mobstat)]) and ratkilled >=9 : ## when all 3 are dead after killing 9
                renpy.jump("victory")
            else:
                for i in death: ## i is positions
                    mobstat[i][0] = "None"
                    ratkilled += 1
                    if targettemp == i:
                        for i, j in enumerate(mobstat):
                            if j[0] != "None":
                                targettemp = i
                                break
        ## old alv system
        # elif encounter == "Alv":
        #     mobstat[death[0]][0] = "None"
        #     head = []
        #     for i, j in enumerate(mobstat):
        #         if mobstat[i][0] == "None":
        #             head.append(i)
        #     while len(head) > 0:
        #         headrespawn = renpy.random.choice(head)
        #         if alvheads[headrespawn] !=0:
        #             mobstat[headrespawn] = [mob[0].name, mob[0].hp, 0, 0, 0, mob[0].dmg, mob[0].cd, 0, 0, 0]
        #             alvheads[headrespawn] = alvheads[headrespawn]-1
        #             break
        #         else:
        #             head.remove(headrespawn)
        #     if alvkill == 3+(2+0+1+2):
        #         mobstat[1] = [mob[i].name, (mob[i].hp), 0, 0, 0, mob[i].dmg, mob[i].cd, 0, 0]
        #
        #     if targettemp == death[0]:
        #         for i, j in enumerate(mobstat):
        #             if j[0] != "None":
        #                 targettemp = i
        #                 break
        #     head = []
        elif encounter == "Alv":
            for i in death: ## i is positions
                mobstat[i][0] = "None"
                alvkill += 1

                ## retargetting ##
                if targettemp == i:
                    if len(mobstat) - len([item for item in mobstat if item[0] == "None"]) == 1: ## only alv remaining:
                        targettemp = 0
                    else:
                        targettemp = abs(i-3)
                        # for i, j in enumerate(mobstat):
                        #     if j[0] != "None" and j[0]!= "Alv":
                        #         targettemp = i
                        #         break



        else:
            while len(death)>0:
                mobstat[death[0]][0] = "None"
                death.pop(0)
            target = 0

        ## Retargetting
        if mobstat[targettemp][0] == "None":
            for i, j in enumerate(mobstat):
                if mobstat[i][0] != "None" and mobstat[i][6] != 69420:
                    targettemp = i
                    break

    ## TODO: goon death narration here
    ## TODO:s Alv 1st death narration here
    show screen combat

    jump combatloop

label victory:
    $ timerpause == True
    hide screen combat with dissolve
    stop music fadeout 1.0

    ## TODO: have encounter specific victory
    "You win"

    # jump endcombat
    return
label gameover:
    hide screen combat
    stop music fadeout 1.0
    play music gameover volume 0.2 fadein 1.0
    scene black
    "You LOSE"
    menu:
        "Retry?"
        "Yes":
            stop music fadeout 1.0
            jump combat
        "No":
            return

label shattering:
    show screen shattering(mobpos[len(mobstat)][targettemp]) #with shatterwipe
    pause 0.8
    hide screen shattering
    return
screen shattering(position):
    fixed:
        add im.FactorScale("images/shattering.png", 0.5) at combat2 yoffset -80 xpos position
