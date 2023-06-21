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
        if parrypause == False and tick<tickmax:
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
    button:
        align (0.5, 0.7)
        xysize (300, 100)
        action Function(parrygo)
        background "black"
        if tick < tickmax:
            text "Parry" xalign 0.5 yalign 0.5
        else:
            text "Take the Hit" xalign 0.5 yalign 0.5


screen textoutcome(tt):
    frame:
        xalign 0.5 yalign 0.2
        text tt size 100 bold True

label parryoutcome: ##animation. ##Infuse with breezehurt later.
    ## value altered for ease of testing
    if tick>=75 and tick <=80:
        $ mobdamage = 5
    elif tick>=55 and tick <=90:
        $ mobdamage = 20
    else:
        $ mobdamage = mobstat[mobattacker][5]

    if tick>=75 and tick <=80:
        show screen textoutcome("DEFLECTED")
    elif tick>=55 and tick <=90:
        show screen textoutcome("BLOCKED!")
    else:
        show screen textoutcome("Failed block!")
    pause 1
    hide screen parry
    # pause
    hide screen textoutcome
    $ tick = 0
    $ parrypause = False

    return
###############################
