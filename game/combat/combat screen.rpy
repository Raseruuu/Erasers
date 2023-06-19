image targetsign = im.FactorScale("gui/target.png", 0.3)
image breezecombat = im.FactorScale(im.Crop("images/sprite/breeze.png", (1200, 300, 1700, 2000)), 0.15)
image flairmob = im.FactorScale(im.Crop("images/sprite/flair.png", (500, 200, 3500, 6000)), 0.08)
image ratmob = im.FactorScale("images/sprite/rat.png", 0.8)

image fire = im.FactorScale("gui/fire.png", 0.3)
image ice = im.FactorScale("gui/ice.png", 0.05)


label combattest:
    "entering combat"
    # $ combatant = [breeze, sofi, flair]
    $ encounter = "Rat"
    call combat
    "combat end"
    # $ renpy.fix_rollback()
    return

label combat:
    python:
        timerpause = False
        combattalk = False
        hpmax = 350
        hp = 320
        shield = 10.00

        fhpmax = 800
        fhp = 751
        flairlow = False
        mobdmg = 70

        clickmax = 140 ## 20clicks/second

        mob = moblist[encounter]

        click = []
        # slow = []
        # burn = []
        mobhp = []
        mobstat = []
        for i in mob:
            click.append(0)
            # slow.append(0)
            # burn.append(0)
            mobhp.append(i.hp)
            mobstat.append([i.name, i.hp, 0, 0]) ##slow/burn

        breezecd = soficd = flaircd = 0.00

        damage = 0
        skillvalue = 0
        act = ""
        mobattacker = 0
        target = 0


    ## Arts
    scene bg_city_destroyed
    show black:
        alpha 0.8
    window hide

    show screen combat
    show breezecombat:
        xpos 450
        yanchor 1.0 ypos 1050
    # show targetsign:
    #     xalign 0.5 yanchor 0.5 ypos 0.4


    label combatloop:
        # $ renpy.block_rollback()

        ## Midfight Narration
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
    if combattalk == False:
        button:
            action NullAction()

    timer 0.05 action Function(tick) repeat True
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
    #         action Function(autoattack)

screen breeze: ##hp bar
    # fixed: ##Icon
    #     xpos 450
    #     yanchor 1.0 ypos 1050
    #     xysize (255, 300)
    #     add "breezecombat"

    fixed: ##Hp Bar
        xpos 750 ypos 1000
        xysize (500, 50)
        bar:
            value hp
            range hpmax
            xysize (500, 30)
            yoffset 17
        bar:
            value shield
            range 10.00
            left_bar "gui/bar/shield.png"
            right_bar "gui/bar/blank.png"
            xysize (500, 20)
        text "HP: "+str(hp) xpos 10 yalign 1.0
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

    use mobicon(i, position)

    fixed: ##mob click
        xysize (300, 30)
        at combat2 yoffset 250 xpos position
        bar:
            value click[i]
            range mob[i].cd
            xysize (300, 30)
        # text "(enemy attack cooldown)" xalign 0.5 yalign 0.5

    fixed:
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
        # add "white"
        add mob[i].img xalign 0.5 yalign 1.0 yoffset -50
        button: ##to target
            action SetVariable("target", i)


screen targetting(position):
    fixed:
        add "targetsign" at combat2 xpos position

screen actbutton:

    # frame: ## Topleftbutton
    #     xysize (100, 50)
    #     pos(25, 25)
    #     textbutton "DDD":
    #         xalign 0.5 yalign 0.5
    #         action [If(timerpause == False, true = [SetVariable("timerpause", True), Call("damagephase")])]

    fixed: ##Sofi action buttons
        pos (50, 800)
        hbox:
            xysize (150, 175) spacing 50
            for i, j in enumerate(sofilist):
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
            for i, j in enumerate(breezelist):
                button:
                    xysize (150, 175)
                    action [If(breezecd >= breezecost[i], true = [SetVariable("breezecd", 0),
                                                                SetVariable("timerpause", True),
                                                                SetVariable("act", j),
                                                                Call("damagephase")])]
                    vbar:
                        value breezecd
                        range breezecost[i]
                        xysize (150, 175)
                    text j xalign 0.5 yalign 0.5
                    if breezecd <= breezecost[i]:
                        text str(int(breezecd)) align (1.0, 1.0) offset (-10, -10)

    fixed: ##Flair action buttons
        pos (1500, 800)
        hbox:
            spacing 50
            xysize (150, 175)
            for i, j in enumerate(flairlist):
                button:
                    xysize (150, 175)
                    action [If(flaircd >= flaircost[i], true = [SetVariable("flaircd", max(flaircd-flair.cost[i]-2, 0)),
                                                                SetVariable("timerpause", True),
                                                                SetVariable("act", j),
                                                                Call("damagephase")])]
                    vbar:
                        value flaircd
                        range flaircost[i]
                        xysize (150, 175)
                    text j xalign 0.5 yalign 0.5
                    text str(int(flaircost[i]))
                    if flaircd <= flaircost[i]:
                        text str(int(flaircd)) align (1.0, 1.0) offset (-10, -10)
    # timer 0.05 action Function(tick) repeat True


# screen main message

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

# action Return("damagephase")
 # if _return=="damagephase":
