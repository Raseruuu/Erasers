## parry: 0.55-0.9 deflect, 0.75-0.8 parry
init python:
    tick = 0
    tickmax = 100
    parrypause = False
    parryoutcome = 0

    def parry():
        global tick
        global tickmax
        global parrypause
        global mobstat
        if parrypause == False and tick<tickmax:
            if mobstat[target][2] > 0:
                tick +=0.5
            else:
                tick +=1

    def parrygo():
        global parrypause
        parrypause = True
        renpy.jump("parryoutcome")

label parry:
    show screen parry
    pause
    return

screen parry:
    timer 0.01 action Function(parry) repeat True
    # frame:
    #     background "black"
    fixed:
        align (0.5, 0.5)
        xysize (600, 200)
        bar:
            xysize (500, 60)
            xpos 50 yalign 0.5
            value tick
            range tickmax
            right_bar "gui/bar/parry.png"
            left_bar "gui/bar/parry.png" ## 500x40 (30 buffer above)
            thumb "gui/bar/thumb.png" ## 80x4
            thumb_offset 2
    fixed:
        button action Function(parrygo) alternate Function(parrygo)
        if tick < tickmax:
            text "Parry" xalign 0.5 yalign 0.7
        else:
            text "Take the Hit" xalign 0.5 yalign 0.7

screen textoutcome(tt):
    frame:
        xalign 0.5 yalign 0.2
        text tt size 100 bold True

label parryoutcome: ##animation.
    if tick>=75 and tick <=80:
        $ mobdamage = 5
        $ hitsound = swordclash
        show screen textoutcome("PARRIED!")
    elif tick>=55 and tick <=90:
        $ mobdamage = 25
        $ hitsound = swordclash
        show screen textoutcome("DEFLECTED!")
    else:
        $ mobdamage = mobstat[mobattacker][5]
        $ hitsound = punch2
        show screen textoutcome("Failed block!")
    return
###############################
