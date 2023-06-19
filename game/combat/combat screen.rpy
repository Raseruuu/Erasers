image targetsign = im.FactorScale("gui/target.png", 0.3)
image breezecombat = im.FactorScale(im.Crop("images/sprite/breeze.png", (1200, 300, 1700, 2000)), 0.15)
image flairmob = im.FactorScale(im.Crop("images/sprite/flairc.png", (200, 100, 2000, 3000)), 0.16)
image ratmob = im.FactorScale("images/sprite/rat.png", 0.8)

image fire = im.FactorScale("gui/fire.png", 0.3)
image ice = im.FactorScale("gui/ice.png", 0.05)


label combattest:
    "entering combat"
    # $ combatant = [breeze, sofi, flair]
    $ encounter = "Flair"
    call combat
    "combat end"
    # $ renpy.fix_rollback()
    return

label combat:
    python:
        timerpause = False
        combattalk = False
        ## Breeze's hp/hpmax/shield
        hpmax = 350
        hp = 320
        shield = 0 #10.00

        ## To trigger midcombat narrative
        flairlow = False

        mob = moblist[encounter] ## copying the monsters from encounter tag. (check combat data)
        mobaction = []

        click = [] ## 20clicks/second
        mobhp = []
        mobstat = []
        for i in mob:
            click.append(0)
            mobhp.append(i.hp)
            mobstat.append([i.name, i.hp, 0, 0]) ##slow/burn

        breezecd = soficd = flaircd = 0.00

        ##combat related variables
        mobattacker = 0 #the enemy that's attacking
        target = 0 ## the enemy being attacked
        act = "" ## temp way to tell game which action card picked. ##TODO: streamline it.

    ## Arts
    scene bg_city_destroyed
    show black:
        alpha 0.8
    window hide

    show screen combat ## main screen
    show breezecombat: ## breeze icon
        xpos 450
        yanchor 1.0 ypos 1050


    label combatloop: ##the main label where things goes.
        # $ renpy.block_rollback() ##stops rollback from here on

        ## Midfight Narration trigger
        if encounter == "Flair" and mobhp[0] < 50 and flairlow == False:
            $ timerpause = True
            $ combattalk = True

            $ flairlow = True
            f "Oh no"
            b "Haha"
            window hide

            $ combattalk = False
            $ timerpause = False
        pass
    pause ##gameplay here
    return


screen combat:
    ## no outside clicking if not in narrative phase
    if combattalk == False:
        button:
            action NullAction()

    ## Main ticker. This is where all the timing stuff happens.
    timer 0.05 action Function(tick) repeat True

    ##display breeze hp and enemys, and the commands
    use breeze
    for i, j in enumerate(mob):
        use mob(i,mobpos[len(mob)][i])
    use targetting(mobpos[len(mob)][target])
    use actbutton

    ##test button
    # frame:
    #     xysize (200, 100)
    #     pos (1150, 850)
    #     textbutton "TEST" align (0.5, 0.5):
    #         # action Function(autoattack)
    #         action Jump("mobaction")

screen breeze: ##hp bar
    # fixed: ##Breeze Icon, might bring it back now I use vpunch for being hit.
    #     xpos 450
    #     yanchor 1.0 ypos 1050
    #     xysize (255, 300)
    #     add "breezecombat"

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
            value click[i]
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

screen actbutton:

    # frame: ## Topleftbutton. For testing
    #     xysize (100, 50)
    #     pos(25, 25)
    #     textbutton "DDD":
    #         xalign 0.5 yalign 0.5
    #         action [If(timerpause == False, true = [SetVariable("timerpause", True), Call("damagephase")])]

    fixed: ##Sofi action buttons
        pos (50, 800)
        hbox:
            xysize (150, 175) spacing 50
            for i, j in enumerate(sofi.list):
                button:
                    xysize (150, 175)
                    action [If(soficd >= sofi.cost[i], true = [
                                                        SetVariable("soficd", max(soficd-sofi.cost[i]-3, 0)),
                                                        SetVariable("act", j),
                                                        Call("sofiphase")])]
                    vbar:
                        value soficd
                        range sofi.cost[i]
                        xysize (150, 175)
                    text j xalign 0.5 yalign 0.5
                    text str(int(sofi.cost[i])) xalign 0.5 yoffset 5
                    if soficd <= sofi.cost[i]:
                        text str(int(soficd)) align (1.0, 1.0) offset (-10, -10)

    fixed: ##Breeze action buttons
        pos (750, 800)
        hbox:
            spacing 50
            xysize (150, 175)
            for i, j in enumerate(breeze.list):
                button:
                    xysize (150, 175)
                    action [If(breezecd >= breeze.cost[i], true = [SetVariable("breezecd", 0),
                                                                SetVariable("timerpause", True),
                                                                SetVariable("act", j), ## for the damagephase to sort out.
                                                                Call("damagephase")])]
                    vbar: ## to show cd
                        value breezecd
                        range breeze.cost[i]
                        xysize (150, 175)
                    text j xalign 0.5 yalign 0.5
                    if breezecd <= breeze.cost[i]: ## show how much cd used TODO: should be reversed if we keep this.
                        text str(int(breezecd)) align (1.0, 1.0) offset (-10, -10)

    fixed: ##Flair action buttons
        pos (1500, 800)
        hbox:
            spacing 50
            xysize (150, 175)
            for i, j in enumerate(flair.list):
                button:
                    xysize (150, 175)
                    action [If(flaircd >= flair.cost[i], true = [SetVariable("flaircd", max(flaircd-flair.cost[i]-2, 0)),
                                                                SetVariable("timerpause", True),
                                                                SetVariable("act", j),
                                                                Call("damagephase")])]
                    vbar:
                        value flaircd
                        range flair.cost[i]
                        xysize (150, 175)
                    text j xalign 0.5 yalign 0.5
                    text str(int(flair.cost[i]))
                    if flaircd <= flair.cost[i]:
                        text str(int(flaircd)) align (1.0, 1.0) offset (-10, -10)

# screen main message ## If I want to get fancy on the narrative part.

screen damagecalc(value): ##on target
    fixed:
        xysize (300, 100)
        xpos 850 ypos 200
        text str(value) size 100 bold True color "#FF0000"

screen damageincoming(value): ##on breeze
    fixed:
        xysize (300, 100)
        # pos (100, 200)
        xpos 500 ypos 700
        text str(value) size 80 bold True color "#FF0000"
