label midfight:
    $ mobphase = True
    $ timerpause = True
    $ combattalk = True

    $ renpy.call(midtalk)

    $ combattalk = False
    $ timerpause = False
    $ mobphase = False
    return

#####################################################################

label goontute:  ## Sofi Join
    b "haha. So what you gotta do, is to slash at your target"

    $ act = "Heal"
    $ hp = min(hpmax, hp+150)
    play sound healing
    show screen damageincoming(150, "#00FF00")

    b "Cheers."
    hide screen damageincoming

    s "Gee couldn't you please take it more seriously?"
    b "You've got my back don't you?"
    s "Good grief..."

    $ combatant.append(sofi)
    $ soficd = 0

    $ fighttalk = True

    return

label goontute2:
    python:
        notdead = abs(death[0]-1)
        goonleftover = []
        for i in mobstat:
            goonleftover.extend(i)
        goonleftover.pop(death[0])

    hide screen combat
    hide breezecombat
    show screen goonleft
    b "ha"
    goonleft "Oh no the other Frank"
    b "Yep."


    $ targettemp = abs(death[0]-1)
    $ mobstat[death[0]][0] = "None"
    $ death.pop(0)
    hide screen goonleft
    show breezecombat: ## breeze icon
        xpos 450 yanchor 1.0 ypos 1050
    show screen combat
    return


################
## RATS FIGHT ##
################
label ratrespawn:
    ## resets rats count
    # hide screen combat
    # show screen combat

    python:
        if ratkilled == 1:
            midtalk = "ratnew"
            renpy.call("midfight") ## first reappear

        if fighttalk == False and ratkilled == 3:
            midtalk = "rattalk"
            renpy.call("midfight") ## Flair joins in.

        if ratkilled >=9 and fighttalk == 1:
            midtalk = "ratlast"
            renpy.call("midfight")
    jump combatloop

label ratnew:
    show screen combat
    "New Vibrant infested Rat appears!"
    b "Tssk"
    window hide
    return

label rattalk:
    show screen combat
    $ fighttalk = 1

    s "there's just no end to them!"
    b "gdi what's this bs"
    f "Can I help now?"
    b "..."
    s "Breeze! Now's not the time for this!"
    f "Seriously!"
    b "Fine! Just becareful about collateral damage."
    f "Of course I'll be careful. She's here with us!"

    $ combatant.append(flair)
    $ flaircd = 0
    ## show flair joins party ##

    hide screen combat
    show screen combat with dissolve
    window hide
    return

label ratlast:
    show screen combat
    s "There's not many left!"
    b "There should be an opening if we can clear them all out in one go. \nFire girl do your thing!"
    f "What did you just call me?"
    b "Counting on ya!"
    f "Don't just ignore me!"
    $ fighttalk = 2
    window hide
    return

####################
## ALV FIGHT ##
####################
label alvstart:
    hide screen combat
    hide breezecombat
    show screen alvintro

    b "Don't worry. I've got this."
    hide screen alvintro
    hide black
    hide breezecombat
    with dissolve

    play music tanzanite volume 0.6 fadein 1
    $ nowplaying = "Tanzanite - bitter sweet entertainment"
    show iceblue with Dissolve(1.5):
        alpha 0.5
    $ combatant[0] = breezeex
    show screen combat
    show breezecombat: ## breeze icon
        xpos 450 yanchor 1.0 ypos 1050
    pause 1.0
    return

label alvcore: ##when first exposed
    hide screen combat
    hide breezecombat
    show screen alvhead
    s "Hey look the core is exposed!"
    f "Alvy!"
    b "Just what I wanted. Hang in there I'm going to get you out!"
    hide screen alvhead
    show screen combat
    show breezecombat: ## breeze icon
        xpos 450 yanchor 1.0 ypos 1050
    $ fighttalk = True
    return


####################
## Azmaveth FIGHT ##
####################
label aztalk: ## triggered half-time

    $ fighttalk = True
    b "This guy is tough"
    f "Hang in there!"
    a "Damn, you really like those girls huh?"
    "He flexes, adopting a more agile stance."
    "Something tells Breeze that this will only get more difficult."
    show screen textoutcome("Azmaveth speeds up")
    a "Time to ramp it up!"
    b "Tssk!"
    hide screen textoutcome
    window hide
    $ mobstat[0][6] = 60
    $ mobstat[0][4] = max(0, mobstat[0][4]-20)
    return

label azwin:
    $ timerpause = True
    $ combattalk = True

    hide screen combat
    hide screen parry
    show azmob at combat2:
        xpos 960
    b "Did we win?"
    hide azmob with dissolve

    jump victory
