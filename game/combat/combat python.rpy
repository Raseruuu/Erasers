label combattest:
    "entering combat"
    $ combatroom = True
    menu:
        "Pick encounter"
        "Goons":
            $ encounter = "Goons"
        "Rats":
            $ encounter = "Rats"
        "Corrupted":
            $encounter = "Alv"
        "Az":
            $encounter = "Az"

label precombat:
    $ combatant = combatantlist[encounter]
    call combat

    label endcombat:
        $ _skipping = True
        $ _game_menu_screen = "save_screen"
        $ quick_menu = True
        scene black with dissolve
        # "combat end"
        pause 0.1

    $ renpy.fix_rollback()
    return


label combat:
    window hide
    hide screen skip_indicator
    hide screen quickhover
    $ quick_menu = False

    python:
        _skipping = timerpause = combattalk = False
        nowplaying = "11"
        _game_menu_screen = None ##TODO: uncomment when shipping

        ## Breeze's hp/hpmax/shield
        hpmax = hp = 1000
        shield = shieldtime = 0
        breezeaction = []
        act = ""
        atkdamage = 0
        sofibuff = 1
        breezecd = soficd = flaircd = 0.00

        ## mob's listing and action and phase
        mobcopy = moblist[encounter] ## copying the monsters from encounter tag. (check combat data)
        mobaction = []
        mobphase = False
        mobstat = []
        alvbuff = []
        for i in mobcopy:
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
        notdead = None

        gameover = 0


        if encounter == "Alv":
            alvkill = 0
            targettemp = 1
            for i, j in enumerate(mobstat):
                j.extend([0.25]) ## regen(10)
            mobstat[0][10] = 5

        ## Az
        aztimer = 2400 ##120s in fullgame
        iceshield = 0

    ## Arts
    # scene bgpark
    show black:
        alpha 0.8

    show screen combat ## main screen
    show breezecombat: ## breeze icon
        xpos 490 yanchor 1.0 ypos 1050

    $ timerpause = True
    show screen combatstart
    play sound "sound/sfx/opengameart/swing3.ogg"
    pause 2
    hide screen combatstart
    $ timerpause = False

    if encounter == "Alv":
        $ midtalk = "alvstart"
        call midfight
    elif encounter == "Az":
        play music overtheblood volume 1.0
        $ nowplaying = "Over the Blood - Youfulca"
    else:
        play music battle volume 1.0 fadein 0.5
        $ nowplaying = "Battle"

    if persistent.firsttime == True and encounter == "Goons":
        $ timerpause = True
        show screen tutorial

    ##########################################################################################
    ## the main label where things goes ##
    label combatloop:
        $ renpy.block_rollback() ##stops rollback from here on ##TODO: remove when ship
        python:
            if encounter == "Goons":
                if fighttalk == False and hp < 700:
                    midtalk = "goontute"
                    renpy.call("midfight")

        pause ##gameplay here

    return

####################################################################################
##
####################################################################################

label sofiphase:
    $ timerpause = True

    if act == "Shield":
        show screen atkshield
        play sound shielding
        pause 0.2
        $ shield += skillvalues["Shield"]

    if act == "Heal":
        $ hp = min(hpmax, hp+skillvalues["Heal"])
        play sound healing
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
        elif act == "Tundra":
            # atksound = tundra
            for i in mobstat:
                atksound = None
                breezeaction.append("Tundra")
        else:
            breezeaction = [act]

    if act == "Inferno": ##animation
        show screen atkinferno()
        play sound inferno
    if act == "Tundra":
        show screen atktundra
        play sound tundra

    call breezeaction from _call_breezeaction ## STATS hp/slow/burn
    $ mobphase == False
    ## End Condition Check ##
    python:
        death = []
        for i, j in enumerate(mobstat):
            if mobstat[i][1]<=0 and mobstat[i][0] != "None": ## if there's a 0hp
                death.append(i)
                if encounter == "Alv":
                    alvkill +=1

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
            if act == "Inferno" or act == "Tundra":
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
            call shattering from _call_shattering
            $ mobstat[target][9] = 0
    if act == "Shard":
        if encounter == "Az":
            $ mobstat[target][2] = 50
        elif encounter == "Alv":
            $ mobstat[target][2] = 200
        else:
            $ mobstat[target][2] = 100 ## slowed for 5s, 0.25rate

    if act == "Firebolt":
        $ mobstat[target][3] = 400 ## burn 20s, 20hp
    python:
        if act == "Tundra":
            for i, j in enumerate(mobstat):
                if mobstat[i][2] != 0:
                    mobstat[i][9] = mobstat[i][2]



    $ renpy.pause(0.25)
    ## ANIMATION
    show screen damagecalc(atkdamage)
    $ renpy.pause(0.75)

    hide screen atkblade
    hide screen atkshard
    hide screen atktundra
    hide screen atkfirebolt
    hide screen atkinferno

    $ timerpause = False
    stop sound
    hide screen damagecalc


    ## HP
    $ mobstat[target][1] = max(0, mobstat[target][1] - atkdamage)
    $ mobstat[target][7] = max(0, mobstat[target][7] - (atkdamage//2))

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
        show azparry onlayer screens:
            xalign 0.7 yalign 1.0
            alpha 0.2
            blur 2.5
        play sound swish9 volume 5.0

        call parry from _call_parry
        play sound hitsound
        hide azparry onlayer screens
        hide punchparry onlayer screens
        with Dissolve(0.2)
        hide punchpre onlayer screens
        hide punchpost onlayer screens
        with Dissolve(0.1)
        hide screen parry

    elif encounter == "Alv":
        $ mobdamage = max(50, int(mobstat[mobattacker][5]*(1-((mobstat[mobattacker][2])/200.00)))) ## damage reduced by slow.
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

    if mobdamage-shield>0:
        show screen damageincoming(mobdamage, "#FF0000") ## dmg number
        with vpunch   # show breezecombat at mobhurt ##abandoned
        if encounter != "Az":
            play sound hitsound
    # if iceshield > 0:
    #     play sound iceshatter

    $ renpy.pause(1.0)

    if encounter == "Az":
        hide screen textoutcome
        $ breezecd = min(5, breezecd-1)
        $ tick = 0
        $ parrypause = False

    $ timerpause = False
    $ mobattacker = None
    hide screen damageincoming

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
        ############################################
        if encounter == "Rats":
            if all([mobstat[i][1] == 0 for i, j in enumerate(mobstat)]) and ratkilled >=12: ## when all 3 are dead after killing 9
                renpy.jump("victory")
            else:
                for i in death: ## i is positions
                    mobstat[i][0] = "None"
                    ratkilled += 1
                    ## reset target
                    if targettemp == i:
                        for i, j in enumerate(mobstat):
                            if j[0] != "None":
                                targettemp = i
                                break

        elif encounter == "Alv":
            for i in death: ## i is positions
                mobstat[i][0] = "None"
                alvkill += 1

                ## retargetting ##
                if targettemp == i:
                    if len([item for item in mobstat if item[0] == "None"]) == 2: ## only core remaining:
                        targettemp = 0
                    else:
                        targettemp = abs(i-3)
            if mobstat[1][0] == "None" and mobstat[2][0] == "None" and fighttalk == False:
                midtalk = "alvcore"
                renpy.call("midfight")

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
    show screen combat

    jump combatloop

label victory:
    $ timerpause == True
    stop music fadeout 1.0
    hide screen combat
    with dissolve

    if combatroom == True:
        $ combatroom = False
        return

    if encounter == "Goons":
        jump postgoonfight
    if encounter == "Rats":
        jump chapter6
    if encounter == "Alv":
        jump chapter8
    if encounter == "Az":
        jump chapter9

    # "You win"
    return
label gameover:
    hide screen combat
    stop music fadeout 1.0
    play music gameover volume 0.2 fadein 1.0
    $ gameover +=1
    scene black
    "You LOSE"
    if gameover == 5:
        menu:
            "Skip battle?"
            "Yes":
                stop music fadeout 0.5
                jump victory
            "No":
                pass
    menu:
        "Try Again?"
        "Yes":
            stop music fadeout 1.0
            jump combat
        "Give Up":
            $ combatroom = False
            return

label shattering:
    show screen shattering(mobpos[len(mobstat)][targettemp]) #with shatterwipe
    pause 0.8
    hide screen shattering
    return
screen shattering(position):
    fixed:
        add im.FactorScale("images/shattering.png", 0.5) at combat2 yoffset -80 xpos position
