image breezecombat = im.FactorScale(im.Crop("images/breeze.png", (1200, 300, 1700, 2000)), 0.15)
image flairmob = im.FactorScale(im.Crop("images/flair.png", (800, 200, 3400, 6000)), 0.125)

label combat:
    python:
        hpmax = 50
        hp = 35

        fhpmax = 100
        fhp = 69

        click = 50
        clickmax = 100

    scene bg_city_destroyed
    show black:
        alpha 0.8
    "Combat test"

    window hide
    show screen combat

    pause
    return

screen combat:
    button:
        action NullAction()
    use breeze
    use mob
    use testbutton
    # use damage

    # timer 0.05 action Function(tick) repeat True

screen breeze:
    fixed: ##Icon
        xpos 200
        yanchor 1.0 ypos 1000
        xysize (255, 300)
        add "breezecombat"

    fixed: ##Hp Bar
        xysize (350, 20)
        xpos 500
        ypos 970
        bar:
            value hp
            range hpmax
            xysize (350, 20)

screen mob:
    fixed: ##mob hp
        xysize (1000, 20)
        xalign 0.5 ypos 30
        bar:
            value fhp
            range fhpmax
            xysize (1000, 20)
    fixed: ##mob icon
        xalign 0.5 ypos 100
        xysize (425, 750)
        add "flairmob"
    fixed: ##mob click
        xysize (500, 50)
        xpos 50 ypos 100
        bar:
            value click
            range clickmax
            xysize (500, 50)


screen testbutton:
    button:
        xysize (100, 50)
        pos(25, 25)
        text "DDD":
            xalign 0.5 yalign 0.5
        action Call("damage")

screen damagecalc:
    frame:
        xysize (300, 100)
        pos (100, 200)
        text "5 Damage":
            xalign 0.5 yalign 0.5

label damage:
    show screen damagecalc
    ##damage calculation
    $ renpy.pause(2.0)
    $ click = 0
    hide screen damagecalc
    window hide
    return
