## Demo fight
label flairtalk:
    $ timerpause = True
    $ combattalk = True

    $ fighttalk = True
    f "Oh no"
    b "Haha"
    window hide

    $ combattalk = False
    $ timerpause = False
    return


################
## RATS FIGHT ##
################
label ratnew:
    show screen combat
    $ timerpause = True
    $ combattalk = True

    "New Vibrant infested Rat appears!"
    b "tssk"
    window hide

    $ combattalk = False
    $ timerpause = False
    return

label rattalk:
    show screen combat
    $ timerpause = True
    $ combattalk = True

    $ fighttalk = True
    s "there's just no end to them!"
    b "gdi what's this bs"
    f "Need a hand?"
    b "Yeah sure what can you do?"
    $ combatant.append(flair)
    ## show flair joins party

    hide screen combat
    show screen combat with dissolve
    window hide
    $ combattalk = False
    $ timerpause = False
    return

label ratlast:
    show screen combat
    $ timerpause = True
    $ combattalk = True
    b "I think that's almost the last of them"
    f "Right, I just need to clear them all out in one go"
    b "Got it!"
    window hide
    $ combattalk = False
    $ timerpause = False
    return
####################
## Azmaveth FIGHT ##
####################
label aztalk: ## triggered half-time
    $ timerpause = True
    $ combattalk = True

    $ fighttalk = True
    b "this guy is tough"
    f "hang in there!"
    a "Huh? I see you're still standing. Guess I can bring it up a notch then."
    "Az flexes, and you can see him assume a more streamlined pose."
    "Something tells Breeze that this will only get more difficult."
    show screen textoutcome("Azmaveth speeds up")
    a "Time pick up the pace!"
    hide screen textoutcome
    window hide
    $ mobstat[0][6] = 40
    $ mobstat[0][4] = max(0, mobstat[i][4]-40)
    $ combattalk = False
    $ timerpause = False
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
