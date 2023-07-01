screen combat:
    ## no outside clicking if not in narrative phase
    if combattalk == False:
        button:
            action NullAction()
    #############################################################################################
    ## Main ticker. This is where all the timing stuff happens. ##
##############################################################
    if timerpause == False:
        timer 0.05 action Function(ticking) repeat True
##############################################################
    ## Main ticker. This is where all the timing stuff happens. ##
    #############################################################################################

    if encounter == "Az" and aztimer > 0:
        fixed:
            xysize(1920, 20)
            yalign 1.0

            bar:
                value aztimer
                range 2400
                xysize(1920, 20)
                yalign 1.0
            text "Until Escape: " + str(aztimer//20) xalign 0.5 yalign 0.5 outlines [(1,"#000",0,0)] size 20

    for i, j in enumerate(mobstat):
        use mobenemy(i, mobpos[len(mobstat)][i], None)
    use targetting(mobpos[len(mobstat)][targettemp])

    use breeze ##hp bar
    use actbutton

    if desc != None:
        use description(desc, descpos)
    if nowplaying != "11":
        use nowplaying

screen breeze: ##hp bar
    fixed:
        xpos 780 ypos 1100
        xysize (520, 50)
        add "black"

    fixed:
        xpos 790 ypos 1000
        xysize (500, 50)
    ## Hp bar
        bar:
            value hp
            range hpmax
            left_bar "gui/bar/lefthp.png"
            right_bar "gui/bar/righthp.png"
            xysize (500, 30)
            yoffset 20
        text "HP: "+str(hp)+"/1000" xpos 10 yalign 1.0 yoffset 6 outlines [(2,"#000",0,0)]
    ## Shield Bar
        bar:
            value shield
            range 500.00
            left_bar "gui/bar/shield.png"
            right_bar "gui/bar/blank.png"
            xysize (500, 20)
            yoffset -2
        if shield >=1:
            text "Shield: "+str(int(shield)) xalign 0.5 yoffset -4 size 20 color "#000"

screen mobenemy(i, position, animation): ## each enemy
    fixed:
        xanchor 0.5 xpos position
        yanchor 0.5 ypos 350
        ysize 565

        button:
            align (0.5, 1.0)
            xsize 400 ysize 565
            if mobstat[i][0] != "None":
                action [If(mobstat[i][6]!=69420 or len(mobstat) - len([item for item in mobstat if item[0] == "None"]) == 1, true = SetVariable("targettemp", i))]

                vbox:
                    yalign 0.5
                    xalign 0.5

                    hbox: ##hp bar
                        xalign 0.5
                        fixed:
                            xalign 0.0 #xpos 50
                            xysize (300, 45)
                            bar:
                                value mobstat[i][1] range mobstat[i][7]
                                left_bar "gui/bar/lefthp.png" right_bar "gui/bar/righthp.png"
                                xysize (300, 30)
                                yalign 1.0
                            # if encounter != "Az":
                            #     # text str(int(mobstat[i][1]))+"/"+str(mobstat[i][7]) align (0.5, 1.0) yoffset 5 ## hp
                            #     text str(mobstat[i][2])+"+"+str(mobstat[i][9]) align (0.5, 0.5)  ##slow and freeze
                            if mobstat[i][3]>0:
                                add "fire" yalign 1.0 xalign 0.0

                    null height 15

                    if encounter == "Alv" and mobstat[1][0] != "None" and mobstat[2][0] !=0 and i == 0:
                        add mobcopy[i].img at corefade

                    elif mobstat[i][9] > 0: ## if frozen
                        add mobcopy[i].img+"frozen" xalign 0.5
                    elif i == mobattacker: ## attacking animation.
                        add mobcopy[i].img at mobattacking xalign 0.5
                    else:
                        add mobcopy[i].img xalign 0.5

                    null height 5
                    hbox:
                        xalign 0.5
                        fixed:
                            xysize (300, 45)
                            bar:
                                value mobstat[i][4]
                                range mobstat[i][6]
                                xysize (300, 20)
                                yalign 0.5
                                xalign 0.0

                            if mobstat[i][2]>0:
                                add "ice" yalign 1.0 xalign 0.0
                                fixed:
                                    yalign 10 xpos 15
                                    text str(int(mobstat[i][2]/20)) color "#fff" outlines [(2,"#000",0,0)]
                    text mobstat[i][0] style "cardtext" xalign 0.5
                if mobstat[i][9]>0:
                    vbar:
                        xalign 0.5 yalign 0.5
                        xysize (20, 250)
                        value mobstat[i][9]
                        range 200
                    add "iceblue" alpha 0.7 ysize 600

            ## TESTING. Respawn counter
            # if mobstat[i][0] == "None":
            #     text "Respawn counter: " + str(int(mobstat[i][8])) xalign 0.5 yalign 0.5

screen targetting(position): ## indicates which one is being targetted.
    fixed:
        add "targetsign" at combat2 yoffset -80 xpos position

transform resize(size):
    zoom size
transform transparent():
    alpha 0.5

screen actbutton:
    if sofi in combatant:
        use sofiact
    if breeze in combatant:
        use breezeact
    if flair in combatant:
        use flairact
    if breezeex in combatant:
        use breezeexact
screen sofiact:
    # add "side sofiside down frown" at resize(0.75):
    #     yoffset -200
    #     xoffset -20
    #     xpos 0
    fixed: ##Sofi action buttons
        pos (80, 875)
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
                    if mobphase == False:
                        hovered [SetVariable("desc", j), SetVariable("descpos", 50+150//2+50+200*i)]
                    unhovered [SetVariable("desc", None)]
                    vbar:
                        value soficd
                        range sofi.cost[i]
                        bottom_bar skillcard[j]
                        top_bar skillcard[j]+"2"
                        xysize (150, 175)
                    text j xalign 0.5 ypos 7 xoffset 5 style "cardtext"
                    if soficd <= sofi.cost[i]:
                        text str(int(sofi.cost[i]-soficd)) align (0.5, 1.0) offset (5, -5) style "cardtext"
                    if mobphase == True:
                        add skillcard[j]+"2" alpha 0.6
screen breezeact:
    fixed: ##Breeze action buttons
        pos (780, 780)
        hbox:
            spacing 50
            xysize (150, 175)
            for i, j in enumerate(breeze.list):
                fixed:

                    button:
                        xysize (150, 175)
                        action [If(breezecd >= breeze.cost[i] and mobphase == False, true = [SetVariable("breezecd", 0),
                                                                    SetVariable("timerpause", True),
                                                                    SetVariable("act", j), ## for the damagephase to sort out.
                                                                    Call("damagephase")])]

                        if mobphase == False:
                            hovered [SetVariable("desc", j), SetVariable("descpos", 750+75+200*i)]
                        unhovered [SetVariable("desc", None)]

                        vbar: ## to show cd
                            xysize (150, 175)
                            bottom_bar skillcard[j]
                            top_bar skillcard[j]+"2"
                            value breezecd range breeze.cost[i]
                        text j xalign 0.5 ypos 7 xoffset 5 style "cardtext"
                        if breezecd <= breeze.cost[i]:
                            text str(int(breeze.cost[i]-breezecd)) style "cardtext":
                                align (0.5, 1.0) offset (5, -25)
                        if mobphase == True:
                            add skillcard[j]+"2" alpha 0.6
screen flairact:
    # add "side flairside down frown" at resize(0.75):
    #         yoffset -200
    #         xalign 0.77
    fixed: ##Flair action buttons
        pos (1520, 875)
        hbox:
            # at transparent
            spacing 50
            xysize (150, 175)
            for i, j in enumerate(flair.list):
                button:
                    xysize (150, 175)
                    action [If(flaircd >= flair.cost[i] and mobphase == False, true = [SetVariable("flaircd", max(flaircd-flair.cost[i]-2, 0)),
                                                                SetVariable("timerpause", True),
                                                                SetVariable("act", j),
                                                                Call("damagephase")])]
                    if mobphase == False:
                        hovered [SetVariable("desc", j), SetVariable("descpos", 1350+150//2+200*i)]
                    unhovered [SetVariable("desc", None)]
                    vbar:
                        xysize (150, 175)
                        bottom_bar skillcard[j]
                        top_bar skillcard[j]+"2"
                        value flaircd range flair.cost[i]
                    text j xalign 0.5 ypos 7 xoffset 5 style "cardtext"
                    if flaircd <= flair.cost[i]:
                        text str(int(flair.cost[i]-flaircd)) align (1.0, 1.0) offset (-10, -10) style "cardtext"
                    if mobphase == True:
                        add skillcard[j]+"2" alpha 0.6
screen breezeexact:
    fixed: ##Breeze action buttons
        pos (780, 780)
        hbox:
            spacing 50
            xysize (150, 175)
            for i, j in enumerate(breezeex.list):

                # fixed:
                button:
                    # xoffset -15 yoffset -15
                    xysize (150, 175)
                    action [If(breezecd >= breezeex.cost[i] and mobphase == False, true = [SetVariable("breezecd", max(breezecd-breezeex.cost[i], 0)),
                                                                SetVariable("timerpause", True),
                                                                SetVariable("act", j), ## for the damagephase to sort out.
                                                                Call("damagephase")])]
                    if mobphase == False:
                        hovered [SetVariable("desc", j), SetVariable("descpos", 750+75+200*i)]
                    unhovered [SetVariable("desc", None)]
                    vbar: ## to show cd
                        xysize (150, 175)
                        bottom_bar skillcard[j]
                        top_bar skillcard[j]+"2"
                        value breezecd range breezeex.cost[i]
                    text j xalign 0.5 ypos 7 xoffset 5 style "cardtext"
                    if breezecd <= breezeex.cost[i]:
                        text str(int(breezeex.cost[i]-breezecd)) style "cardtext":
                            align (0.5, 1.0) yoffset-10
                    if mobphase == True:
                        add skillcard[j]+"2" alpha 0.6
style cardtext:
    color "#FFF" bold True outlines [(3,"#000",0,0)] #font "mangat.ttf"

# screen main message ## If I want to get fancy on the narrative part.

screen damageincoming(value, color): ##on breeze
    fixed:
        xysize (200, 100)
        xanchor 0.5 xpos 640 ypos 700
        at textpopup
        text str(value):
            size 80 bold True color color outlines [(2,"#000",1,1)] xalign 0.5
screen damagecalc(value): ##on target
    fixed:
        xysize (300, 100) xanchor 0.5
        xpos mobpos[len(mobstat)][target]+75 ypos 100
        if value >0:
            text str(value):
                size 80 bold False color "#FF0000" outlines [(2,"#000",0,0)]
                at textpopup

### VFX #######################################################################
screen atkblade(target):
    fixed:
        add "atkblade":
            anchor (0.5, 0.5) ypos 350 xpos mobpos[len(mobstat)][target] -50
            yzoom 1.5
            rotate 45
            at atkblade
screen atkshard(target):
    fixed:
        add "atkshard":
            anchor (0.5, 0.5) ypos 350 xpos mobpos[len(mobstat)][target]
            at atkshard ##total 1s
screen atktundra():
    fixed:
        add "iceblue":
            at atktundra
screen atkshield:
    fixed:
        add "shieldgreen":
            xanchor 0.5 yanchor 1.0
            xpos 1040 ypos 1018
            xysize (500, 20)
            at atkshield
screen atkfirebolt(target):
    fixed:
        add "atkfirebolt":
            anchor (0.5, 0.5) ypos 350 xpos mobpos[len(mobstat)][target]
            at atkfirebolt
screen atkinferno():
    fixed:
        add "atkinferno":
            yalign 1.0
            at atkinferno

screen pausing:
    fixed:
        add "black" alpha 0.5
        text "PAUSING" size 200 bold True align (0.5, 0.5)

screen description(i, descpos):
    fixed:
        xysize (300, 150)
        anchor (0.5, 1.0)
        pos (80+180, 850)
        add "black" alpha 0.8
        text i offset (15, 10) bold True size 30 ## Name
        text str(skillcd[i])+"s" xalign 1.0 offset (-10, 10) size 25
        fixed:
            xysize (280, 100)
            pos (10, 45)
            text str(skilldesc[i]) size 20 yalign 0.5

screen combatstart:
    frame:
        align (0.5, 0.5)
        padding (50, 30, 50, 30)
        # add "gui/textbox.png" alpha 0.5
        text "Combat Start" size 160 bold True align (0.5, 0.5) font "mangat.ttf"

screen combatwin:
    fixed:
        add "gui/textbox.png" alpha 0.5
        text "Victory!" size 160 bold True align (0.5, 0.5)

##########################################################################
screen goonleft:
    for i, j in enumerate([goonleftover]):
        use mobenemy(i, [650, 1270][notdead], None)

screen alvintro:
    for i, j in enumerate(mobstat):
        use mobenemy(i, mobpos[len(mobstat)][i], None)
screen alvhead:
    for i, j in enumerate([alvheadmob]):
        use mobenemy(i, 960, None)

screen tutorial:
    fixed:
        xysize (1920, 1080)
        add "combat/tutorial.png"
        button action [SetVariable("timerpause", False), Hide("tutorial")]

screen nowplaying:
    fixed:
        pos (10, 10)
        text "♫ Now Playing: "+ nowplaying + " ♫" color "#D7D7D7" size 25 outlines [(2,"#000",1,1)]
