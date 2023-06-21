image targetsign = im.FactorScale("gui/target.png", 0.3)
image breezecombat = im.FactorScale(im.Crop("images/sprite/breeze.png", (1200, 300, 1700, 2000)), 0.15)
image flairmob = im.FactorScale(im.Crop("images/sprite/flairc.png", (200, 100, 2000, 3000)), 0.16)
image ratmob = im.FactorScale("images/sprite/rat.png", 0.8)
image azmob = im.FactorScale("images/sprite/temp-laughinghand.webp", 0.5)

image fire = im.FactorScale("gui/fire.png", 0.3)
image ice = im.FactorScale("gui/ice.png", 0.05)

define battle = "sound/Battle_Theme_ogg.ogg"
define overtheblood = "sound//temp/youfulca-over-the-blood_loop.ogg"


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

        ## Midfight talks
        fighttalk = False
        ratkilled = 0

    ## Arts
    scene bg_city_destroyed
    show black:
        alpha 0.8
    window hide

    if encounter == "Az":
        play music overtheblood volume 1.0 fadein 1
        $ aztimer = 2400 ##2400 in fullgame
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
            call flairtalk
        pass
    pause ##gameplay here
    return


screen combat:
    ## no outside clicking if not in narrative phase
    if combattalk == False:
        button:
            action NullAction()

    ## Main ticker. This is where all the timing stuff happens.
    timer 0.05 action Function(ticking) repeat True

    ##display breeze hp and enemys, and the commands
    use breeze
    for i, j in enumerate(mobstat):
        use mob(i,mobpos[len(mobstat)][i])
    use targetting(mobpos[len(mobstat)][target])
    use actbutton

    ##test button
    # if mobphase == False:
    #     frame:
    #         xysize (200, 100)
    #         pos (1150, 850)
    #         textbutton "TEST" align (0.5, 0.5):
    #             action Jump("breezeaction")
                # action Function(autoattack)
                # action Jump("mobaction")
    if aztimer > 0:
        frame:
            # xysize (100, 50)
            text "Time Remaining:" + str(aztimer//20)

screen breeze: ##hp bar

    fixed: ##Hp Bar
        xpos 750 ypos 1000
        xysize (500, 50)
        ## Hp bar
        bar:
            value hp
            range hpmax
            xysize (500, 30)
            yoffset 17
        text "HP: "+str(hp) xpos 10 yalign 1.0
        ## Shield Bar
        bar:
            value shield
            range 10.00
            left_bar "gui/bar/shield.png"
            right_bar "gui/bar/blank.png"
            xysize (500, 20)
        if shield >=1:
            text "Shield: "+str(int(shield)) xpos 10 yoffset -2 size 20 color "#000"

screen mob(i, position): ##TODO: current values are of 1 single enemy
    fixed: ##mob hp
        xysize (300, 20)
        at combat2 yoffset -300 xpos position
        bar:
            value mobstat[i][1]
            range mob[i].hp
            xysize (300, 20)
        text str(int(mobstat[i][1]))+"/"+str(mob[i].hp) align (0.5, 0.5)

    use mobicon(i, position) ## mob image

    fixed: ##mob click
        xysize (300, 30)
        at combat2 yoffset 250 xpos position
        bar:
            value mobstat[i][4]
            range mob[i].cd
            xysize (300, 30)
        # text "(enemy attack cooldown)" xalign 0.5 yalign 0.5

    fixed: ## mob debuff icons
        at combat2 xpos position yoffset -175 xoffset -50
        xysize (300, 300)
        if mobstat[i][3]>0:
            add "fire" xoffset 360 yoffset -10
        if mobstat[i][2]>0:
            add "ice"

screen mobicon(i, position):
    fixed:
        xysize (400, 550)
        at combat2 xpos position
        # add "white" ## for testing use
        add mob[i].img xalign 0.5 yalign 1.0 yoffset -50
        button: ##to assign target
            action SetVariable("target", i)


screen targetting(position): ## indicates which one is being targetted. TODO: change symbol used.
    fixed:
        add "targetsign" at combat2 xpos position
screen mobattacking(position):
    fixed:
        add "fire" at combat2 xpos mobpos[len(mobstat)][position] yoffset -200

screen actbutton:
    if sofi in combatant:
        fixed: ##Sofi action buttons
            pos (50, 800)
            hbox:
                xysize (150, 175) spacing 50
                for i, j in enumerate(sofi.list):
                    button:
                        xysize (150, 175)
                        action [If(soficd >= sofi.cost[i] and mobphase == False, true = [
                                                                                        SetVariable("soficd", max(soficd-sofi.cost[i]-3, 0)),
                                                                                        SetVariable("act", j),
                                                                                        Call("sofiphase")],
                                                                                false = NullAction()
                                                                                        )]
                        vbar:
                            value soficd
                            range sofi.cost[i]
                            xysize (150, 175)
                        text j xalign 0.5 yalign 0.5
                        text str(int(sofi.cost[i])) xalign 0.5 yoffset 5
                        if soficd <= sofi.cost[i]:
                            text str(int(soficd)) align (1.0, 1.0) offset (-10, -10)
    if breeze in combatant:
        fixed: ##Breeze action buttons
            pos (750, 800)
            hbox:
                spacing 50
                xysize (150, 175)
                for i, j in enumerate(breeze.list):
                    button:
                        xysize (150, 175)
                        action [If(breezecd >= breeze.cost[i] and mobphase == False, true = [SetVariable("breezecd", 0),
                                                                    SetVariable("timerpause", True),
                                                                    SetVariable("act", j), ## for the damagephase to sort out.
                                                                    Call("damagephase")])]
                        vbar: ## to show cd
                            xysize (150, 175)
                            value breezecd range breeze.cost[i]
                        text j xalign 0.5 yalign 0.5
                        if breezecd <= breeze.cost[i]: ## show how much cd used TODO: should be reversed if we keep this.
                            text str(int(breezecd)) align (1.0, 1.0) offset (-10, -10)
    if flair in combatant:
        fixed: ##Flair action buttons
            pos (1500, 800)
            hbox:
                spacing 50
                xysize (150, 175)
                for i, j in enumerate(flair.list):
                    button:
                        xysize (150, 175)
                        action [If(flaircd >= flair.cost[i] and mobphase == False, true = [SetVariable("flaircd", max(flaircd-flair.cost[i]-2, 0)),
                                                                    SetVariable("timerpause", True),
                                                                    SetVariable("act", j),
                                                                    Call("damagephase")])]
                        vbar:
                            xysize (150, 175)
                            value flaircd range flair.cost[i]
                        text j xalign 0.5 yalign 0.5
                        text str(int(flair.cost[i]))
                        if flaircd <= flair.cost[i]:
                            text str(int(flaircd)) align (1.0, 1.0) offset (-10, -10)

# screen main message ## If I want to get fancy on the narrative part.

screen damagecalc(value): ##on target
    fixed:
        xysize (300, 100) xanchor 0.5
        xpos mobpos[len(mobstat)][target] ypos 200
        text str(value) size 100 bold True color "#FF0000"

screen damageincoming(value): ##on breeze
    fixed:
        xysize (300, 100)
        # pos (100, 200)
        xpos 500 ypos 700
        text str(value) size 80 bold True color "#FF0000"

screen pausing:
    fixed:
        # xysize (200, 100)
        add "black" alpha 0.5
        text "PAUSING" size 200 bold True align (0.5, 0.5)
