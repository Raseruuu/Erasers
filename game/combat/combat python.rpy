label combattest: ## simulate going into a combat from story.
    "entering combat"

    menu:
        "Pick encounter"
        "Flair":
            $ encounter = "Flair"
            $ combatant = [breeze, sofi]
        "Rats":
            $ encounter = "Rat"
            $ combatant = [breeze, sofi]
        "Az":
            $encounter = "Az"
            $ combatant = [breeze, flair]
        "Parry":
            jump parry

    call combat

    "combat end"
    $ _skipping = True
    $ _game_menu_screen = "save_screen"

    # $ renpy.fix_rollback()
    return

label combat:
    python:
        _skipping = timerpause = combattalk = False
        # _game_menu_screen = None ##TODO: uncomment when shipping

        ## Breeze's hp/hpmax/shield
        hpmax = hp = 350
        shield = 0 #10.00
        breezeaction = []
        act = ""
        breezecd = soficd = flaircd = 0.00
        ## mob's listing and action and phase
        mob = moblist[encounter] ## copying the monsters from encounter tag. (check combat data)
        mobaction = []
        mobphase = False
        mobstat = []
        for i in mob:
            mobstat.append([i.name, i.hp, 0, 0, 0, i.dmg, i.cd]) ##slow/burn/click/dmg/cdmax
        mobdamage = 0 ## each incoming damage

        ##combat related variables
        mobattacker = 0 #the enemy that's attacking
        target = targettemp = 0 ## the enemy being attacked
        hitsound = hit
        atksound = blade

        ## Midfight talks
        fighttalk = False
        ratkilled = 0

        ## Az
        aztimer = 2400 ##2400 in fullgame
        iceshield = 0

    ## Arts
    scene bg_city_destroyed
    show black:
        alpha 0.8
    window hide

    if encounter == "Az":
        play music overtheblood volume 1.0 fadein 1
        pass
    else:
        play music battle volume 1.0 fadein 0.5


    show screen combat ## main screen
    show breezecombat: ## breeze icon
        xpos 450 yanchor 1.0 ypos 1050

    label combatloop: ##the main label where things goes.
        # $ renpy.block_rollback() ##stops rollback from here on

        ## Midfight Narration trigger
        if encounter == "Flair" and mobstat[0][1] < (flairmob.hp)//2 and fighttalk == False:
            # call flairtalk
            $ midtalk = "flairtalk"
            $ renpy.call("midfight")
        pass
    pause ##gameplay here
    return

####################################################################################
##
####################################################################################

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
    if act == "Inferno":
        show screen atkinferno()
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

    if act == "Attack":
        show screen atkblade(target)
        $ atksound = blade
    if act == "Shard":
        show screen atkshard(target)
        $ atksound = ice
    # if act == "Attack":
    #     $ atksound = ice
    # if act == "Shard":
    #     $ atksound == blade
    play sound atksound

    ## TODO: spell/attack animations here
    $ renpy.pause(0.25)
    show screen damagecalc(skillvalues[act]) ## ANIMATION
    $ renpy.pause(0.75)

    hide screen atkblade
    hide screen atkshard
    hide screen atkinferno

    $ timerpause = False
    stop sound
    hide screen damagecalc

    ## HP
    $ mobstat[target][1] = max(0, mobstat[target][1] - skillvalues[act])
    ## debuff no stacking, just reset to max
    if act == "Shard":
        $ mobstat[target][2] = 100 ## slow for 5s, 0.25rate
        if encounter == "Az":
            $ mobstat[target][2] = 50
    if act == "Firebolt":
        $ mobstat[target][3] = 400 ## burn 20s, 20hp

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

    show screen mobattacking(mobattacker) ## attack indicator
    show screen damageincoming(mobdamage) ## dmg number

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
                        midtalk = "ratnew"
                        renpy.call("midfight") ## first reappear
                    if fighttalk == False and ratkilled == 3:
                        midtalk = "rattalk"
                        renpy.call("midfight") ## Flair joins in.
                    if ratkilled >=9:
                        midtalk = "ratlast"
                        renpy.call("midfight")
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
