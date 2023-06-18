image targetsign = im.FactorScale("gui/target.png", 0.3)
image breezecombat = im.FactorScale(im.Crop("images/sprite/breeze.png", (1200, 300, 1700, 2000)), 0.15)
image flairmob = im.FactorScale(im.Crop("images/sprite/flair.png", (800, 200, 3400, 6000)), 0.11)
image ratmob = im.FactorScale("images/sprite/rat.png", 1.0)


label combattest:
    "entering combat"
    # $ combatant = [breeze, sofi, flair]
    $ encounter = "Rattest"
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
        slow = []
        burn = []
        mobhp = []
        for i in mob:
            click.append(0)
            slow.append(0)
            burn.append(0)
            mobhp.append(i.hp)

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
    # show ratmob at combat1
    show breezecombat:
        xpos 450
        yanchor 1.0 ypos 1050
    # show targetsign:
    #     xalign 0.5 yanchor 0.5 ypos 0.4


    label combatloop:
        # $ renpy.block_rollback()
        ## TODO: enemy targeting
        if mobhp[0] < 50 and flairlow == False:
            $ timerpause = True
            $ combattalk = True
            # hide screen nobutton
            f "Oh no"
            b "Haha"
            window hide
            $ flairlow = True
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
        use mob(i)
        use mobicon(i, combat1)
    use actbutton
    use targetting

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

screen mob(i):
    fixed: ##mob hp
        xysize (300, 20)
        xalign 0.5 ypos 30
        bar:
            value mobhp[i]
            range mob[i].hp
            xysize (300, 20)

    fixed: ##mob click
        xysize (300, 30)
        xalign 0.5 ypos 720
        bar:
            value click[i]
            range mob[i].cd
            xysize (300, 30)
        # text "(enemy attack cooldown)" xalign 0.5 yalign 0.5

screen mobicon(i, position):
    button: ##to target
        xysize (425, 750)
        at position
        add mob[i].img xalign 0.5
        action SetVariable("target", i)

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

screen targetting:
    fixed:
        add "targetsign":
            xalign 0.5 yanchor 0.5 ypos 0.4

# screen main message

screen damagecalc(value): ##on target
    fixed:
        xysize (300, 100)
        # pos (100, 200)
        xpos 850 ypos 200
        text str(value) size 100 bold True color "#FF0000"
            # xalign 0.5 yalign 0.5

screen damageincoming(value): ##on breeze
    fixed:
        xysize (300, 100)
        # pos (100, 200)
        xpos 500 ypos 700
        text str(value) size 80 bold True color "#FF0000"

# action Return("damagephase")
 # if _return=="damagephase":
