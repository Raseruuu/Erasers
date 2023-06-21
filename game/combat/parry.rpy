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
        global tick
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
    frame:
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
    frame:
        align (0.5, 0.7)
        xysize (300, 100)
        text "Button" xalign 0.5 yalign 0.5
        button action Function(parrygo)
screen textoutcome(tt):
    frame:
        xalign 0.5 yalign 0.2
        text tt size 100 bold True

label parryoutcome: ##animation. ##Infuse with breezehurt later.
    if tick>=75 and tick <=80:
        show screen textoutcome("DEFLECTED")
    elif tick>=55 and tick <=90:
        show screen textoutcome("BLOCKED!")
    else:
        show screen textoutcome("You got it!")
    pause 1
    hide screen parry
    pause
    hide screen textoutcome


    return
###############################
## TODO: enemy attack, call out parry screen, click to input outcome,
