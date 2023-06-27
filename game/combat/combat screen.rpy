screen combat:
    ## no outside clicking if not in narrative phase
    if combattalk == False:
        button:
            action NullAction()
    #############################################################################################
    ## Main ticker. This is where all the timing stuff happens. ##
##############################################################
    timer 0.05 action Function(ticking) repeat True
##############################################################
    ## Main ticker. This is where all the timing stuff happens. ##
    #############################################################################################

    if encounter == "Az": #and aztimer > 0:
        fixed:
            xpos 1550
            ypos 20
            text "Time Remaining: " + str(aztimer//20)
    ##display breeze hp and enemys, and the commands
    for i, j in enumerate(mobstat):
        use mob1(i, mobpos[len(mobstat)][i])
    use targetting(mobpos[len(mobstat)][targettemp])

    use breeze ##hp bar
    use actbutton
    if desc != None:
        use description(desc, descpos)

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
            xysize (500, 30)
        if shield >=1:
            text "Shield: "+str(int(shield)) xpos 10 yoffset -2 size 20 color "#000"

# screen mob(i, position):
#     fixed: ##mob hp
#         xysize (300, 20)
#         at combat2 yoffset -300 xpos position ## ymid 100 ybot 110
#         bar:
#             value mobstat[i][1]
#             range mob[i].hp
#             xysize (300, 20)
#         text str(int(mobstat[i][1]))+"/"+str(mob[i].hp) align (0.5, 0.5)
#
#     use mobicon(i, position) ## mob image
#
#     if mobstat[i][4]> 0: ##hides bar during mobaction
#         fixed: ##mob click
#             xysize (300, 30)
#             at combat2 yoffset 250 xpos position
#             bar:
#                 value mobstat[i][4]
#                 range mobstat[i][6]
#                 xysize (300, 30)
#             # text "(enemy attack cooldown)" xalign 0.5 yalign 0.5
#
#     fixed: ## mob debuff icons
#         at combat2 xpos position yoffset -175 xoffset -50
#         xysize (300, 300)
#         if mobstat[i][3]>0:
#             add "fire" xoffset 360 yoffset -10
#         if mobstat[i][2]>0:
#             add "ice"
# screen mobicon(i, position): ## ybuttom 625 ytop 125
#     fixed:
#         xysize (400, 550)
#         at combat2 xpos position
#         add "white" ## for testing use
#         add mob[i].img xalign 0.5 yalign 1.0 yoffset -50
#         button: ##to assign target
#             action SetVariable("target", i)
screen mob1(i, position):
    fixed:
        xanchor 0.5 xpos position
        yanchor 0.5 ypos 290
        ysize 565

        button: ##mob hp
            align (0.5, 1.0)
            xsize 400 ysize 565
            # add "white"
             #If(soficd >= sofi.cost[i] and mobphase == False, true = [
            if mobstat[i][0] != "None":
                action SetVariable("targettemp", i)
                vbox:
                    yalign 0.5
                    xalign 0.5


                    hbox:
                        xalign 0.5
                        fixed:
                            xalign 0.5
                            xysize (300, 50)
                            bar:
                                value mobstat[i][1]
                                range mob[i].hp
                                xysize (300, 50)
                            if encounter != "Az":
                                text str(int(mobstat[i][1]))+"/"+str(mob[i].hp) align (0.5, 0.5)
                    null height 15
                    add mob[i].img xalign 0.5
                    null height 15
                    fixed:
                        xalign 0.5
                        xysize (300, 20)
                        bar:
                            value mobstat[i][4]
                            range mobstat[i][6]
                            xysize (300, 20)
            ## TESTING. Respawn counter
            if encounter == "Rat" and mobstat[i][0] == "None":
                text "Respawn counter: " + str(int(30-(mobstat[i][8]))) xalign 0.5 yalign 0.5

    # fixed: ## mob debuff icons
    #     at combat2 xpos position yoffset -175 xoffset -50
    #     xysize (300, 300)
    #     if mobstat[i][3]>0:
    #         add "fire" xoffset 360 yoffset -10
    #     if mobstat[i][2]>0:
    #         add "ice"

screen targetting(position): ## indicates which one is being targetted. TODO: change symbol used.
    fixed:
        add "targetsign" at combat2 yoffset -100 xpos position
screen mobattacking(position): ##TODO :fix symbol
    fixed:
        add "fire" at combat2 xpos mobpos[len(mobstat)][position] yoffset -250

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
                    hovered [SetVariable("desc", j), SetVariable("descpos", 50+150//2+50+200*i)]
                    unhovered [SetVariable("desc", None)]
                    vbar:
                        value soficd
                        range sofi.cost[i]
                        xysize (150, 175)
                    # add skillcard[j]
                    text j xalign 0.5 ypos 20 color "#000"
                    # text str(int(sofi.cost[i])) xalign 0.5 yoffset 5
                    if soficd <= sofi.cost[i]:
                        text str(int(soficd)) align (0.5, 1.0) yoffset-10
screen breezeact:
    fixed: ##Breeze action buttons
        pos (750, 800)
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
                        hovered [SetVariable("desc", j), SetVariable("descpos", 750+75+200*i)]
                        unhovered [SetVariable("desc", None)]

                        vbar: ## to show cd
                            xysize (150, 175)
                            value breezecd range breeze.cost[i]
                        # add skillcard[j] ## image, to be updated into bars later
                        text j xalign 0.5 ypos 20 color "#000"
                        if breezecd <= breeze.cost[i]: ## show how much cd used TODO: should be reversed if we keep this.
                            text str(int(breezecd)) align (1.0, 1.0) offset (-5, -5) color "#000"
screen flairact:
    fixed: ##Flair action buttons
        pos (1350, 800)
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
                    hovered [SetVariable("desc", j), SetVariable("descpos", 1350+150//2+200*i)]
                    unhovered [SetVariable("desc", None)]
                    vbar:
                        xysize (150, 175)
                        value flaircd range flair.cost[i]
                    # add skillcard[j]
                    text j xalign 0.5 ypos 20 color "#000"
                    # text str(int(flair.cost[i]))
                    if flaircd <= flair.cost[i]:
                        text str(int(flaircd)) align (1.0, 1.0) offset (-10, -10)
screen breezeexact: ## TODO: change to EX lineup
    fixed: ##Breeze action buttons
        pos (750, 800)
        hbox:
            spacing 50
            xysize (150, 175)
            for i, j in enumerate(breezeex.list):

                button:
                    xysize (150, 175)
                    action [If(breezecd >= breezeex.cost[i] and mobphase == False, true = [SetVariable("breezecd", max(breezecd-breezeex.cost[i], 0)),
                                                                SetVariable("timerpause", True),
                                                                SetVariable("act", j), ## for the damagephase to sort out.
                                                                Call("damagephase")])]
                    hovered [SetVariable("desc", j), SetVariable("descpos", 750+75+200*i)]
                    unhovered [SetVariable("desc", None)]
                    vbar: ## to show cd
                        xysize (150, 175)
                        value breezecd range breezeex.cost[i]

                    add skillcard[j]
                    text j xalign 0.5 ypos 20 color "#000"

                    if breezecd <= breezeex.cost[i]: ## show how much cd used TODO: should be reversed if we keep this.
                        text str(int(breezeex.cost[i]-breezecd)):
                            align (0.5, 1.0) yoffset-10

# screen main message ## If I want to get fancy on the narrative part.
screen damageincoming(value): ##on breeze
    fixed:
        xysize (200, 100)
        xanchor 0.5 xpos 570 ypos 700
        # at numpop
        text str(value):
            size 80 bold True color "#FF0000" outlines [(2,"#000",0,0)] xalign 0.5
screen damagecalc(value): ##on target
    fixed:
        xysize (300, 100) xanchor 0.5
        xpos mobpos[len(mobstat)][target]+75 ypos 100
        if value >0:
            text str(value):
                size 80 bold False color "#FF0000" outlines [(2,"#000",0,0)]
                at textpopup

screen atkblade(target):
    fixed:
        add "atkblade":
            anchor (0.5, 0.5) ypos 350 xpos mobpos[len(mobstat)][target] -50
            yzoom 1.5
            rotate 45
            at atkblade
            # with punchwipe
screen atkshard(target):
    fixed:
        add "atkshard":
            anchor (0.5, 0.5) ypos 350 xpos mobpos[len(mobstat)][target]
            at atkshard ##total 1s
screen atkinferno():
    fixed:
        add "atkinferno":
            yalign 1.0
            at atkinferno

screen pausing:
    fixed:
        # xysize (200, 100)
        add "black" alpha 0.5
        text "PAUSING" size 200 bold True align (0.5, 0.5)

screen description(i, descpos):
    fixed:
        xysize (300, 150)
        anchor (0.5, 1.0)
        pos (descpos, 800)  ## 750+75+10+400
        add "black" alpha 0.7
        text i offset (10, 10) bold True size 30 ## Name
        text str(skillvalues[i])+"/"+str(skillcd[i])+"s" xalign 1.0 offset (-10, 10) size 25
        # text "1.5s" align (1.0, 1.0) offset (-5, -5) size 20
        fixed:
            xysize (280, 100)
            pos (10, 45)
            text str(skilldesc[i]) size 20 yalign 0.5
