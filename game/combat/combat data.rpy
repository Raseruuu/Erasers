image breezecombat = im.FactorScale(im.Crop("images/sprite/breeze2.png", (600, 150, 850, 1000)), 0.3)
## Enemies ##
image flairmob = im.FactorScale(im.Crop("images/sprite/flairc.png", (200, 100, 2000, 3000)), 0.16)
image ratmob = im.FactorScale("images/sprite/rat.png", 0.8)
image azmob = im.FactorScale("images/sprite/temp-laughinghand.webp", 0.5)

image targetsign = im.FactorScale("gui/target.png", 0.3)

##debuff signs
image fire = im.FactorScale("gui/fire.png", 0.3)
image ice = im.FactorScale("gui/ice.png", 0.05)

## Battle Music
define battle = "sound/Battle_Theme_ogg.ogg"
define overtheblood = "sound/temp/youfulca-over-the-blood_loop.ogg"
define gameover = "sound/temp/youfulca-Horror-juki_loop.ogg"

################################################################
## ATK VFX
image atkblade = im.FactorScale("blade.png", 0.5)
image atkshard = im.FactorScale("shard.png", 0.5)
# image atkshield
# image atkheal
# image atkfirebolt
image atkinferno = im.FactorScale("inferno.png", 2.5)

## attacking sfx
define blade = "sound/sfx/pigmyon/swordstrike.mp3"
define ice = "sound/sfx/pigmyon/shard.mp3"
##TODO: heal
##TODO: shield
##TODO: Firebolt
define inferno = "sound/sfx/opengameart/foom_0.ogg"
###############################################################

## defending sfx
define hit = "sound/sfx/opengameart/swing2.ogg" ## default hit sound
    ### AZ
define swish9 = "sound/sfx/opengameart/swish-9.ogg" ## az punch
define swordclash = "sound/sfx/freesoundeffects/steelsword.mp3" ## parried
define swordblock = "sound/sfx/pigmyon/swordblock.mp3"
define punch2 = "sound/sfx/freesoundeffects/punch2.mp3" ##az punch land

## AZ FIGHT
image punching = "battle effect 3b.png"
image punchpre = "punchpre.png"
image punchpost = "punchpost.png"
image punchparry = "battle effect 12.png"

##############################################################

init -50 python:
    punchwipe = ImageDissolve("grad.png", 0.3)

    import pygame
    def ticking():
        ## Defining global variables ##
        global timerpause

        global mobattacker ## which incoming attack.
        global mobaction ## for attempting queuing up mob actions.

        global slow
        global burn

        global breezecd
        global soficd
        global flaircd
        global shield

        global encounter
        global aztimer
        global midtalk

        if timerpause == False:
            for i, j in enumerate(mobstat): ## individual timer.
                if mobstat[i][4] < mobstat[i][6]:
                    if mobstat[i][2] > 0:
                        mobstat[i][4]+=0.25 ## 0.25x speed
                    else:
                        mobstat[i][4] += 1
            if mobstat[i][2] > 0: ## slow
                mobstat[i][2] -= 1 ## lasts slow/20 seconds
            if mobstat[i][3] > 0: ## burn
                mobstat[i][3] -= 1 #lasts burn/20 seconds
                mobstat[i][1] -= 0.05 # 1hp/second

            ## Commmand card timers.
            if breezecd < max(breeze.cost):
                breezecd +=0.05
            if soficd <max(sofi.cost):
                soficd +=0.05
            if flaircd <max(flair.cost):
                flaircd +=0.05
            if shield > 0: ## Shield Decay
                shield -=0.05

        ## Assigning mob actions when timer up.
        for i,j in enumerate(mobstat):
            if mobstat[i][4] >= mobstat[i][6]:
                timerpause = True
                for i,j in enumerate(mobstat):
                    if mobstat[i][4] >= mobstat[i][6]:
                        mobaction.append(i)
                        mobstat[i][4] = 0
                renpy.call("mobaction")

        ## az timer
        if encounter == "Az" and timerpause == False:
            aztimer -=1
        if aztimer == 2200 and fighttalk == False:
            midtalk = "aztalk"
            renpy.call("midfight")
        if aztimer <= 0:
            renpy.jump("azwin") ## Main ticker

    ## Functions for testing purposes.
    def burning():
        global mobstat
        mobstat[target][3] +=400
    def icing():
        global mobstat
        mobstat[target][2] +=400

####################################################################
##
###################################################################
    class fighter:
        def __init__(self, name, list, cost):
            self.name = name
            self.list = list
            self.cost = cost

    breeze = fighter("Breeze", ["Attack", "Shard"], [1.5, 3.0])
    sofi = fighter("Sofi", ["Shield", "Heal"], [6.0, 10.0])
    flair = fighter("Flair", ["Firebolt", "Inferno"], [2.0, 20.0]) ##2, 20
    breezeex = fighter("Breeze", ["Attack", "Shard", "Gun"], [1.5, 3.0, 1])

    skillvalues = { ## how much damage/heal for each command. used in damagephase.
                    "Attack": 15, "Shard": 20,
                    "gun": 12,
                    "Shield": 10, "Heal": 100,
                    "Firebolt": 30, "Inferno": 70
                    }
    # actsound = {"Attack": blade, "Shard": ice,
    #             "Shield": blade, "Heal": blade,
    #             "Firebolt": blade, "Inferno": inferno}
    ############################################################################
    class mob:
        def __init__(self,
                    name, hp, cd, dmg, img):
            self.name = name
            self.hp = hp
            self.cd = cd #clickmax = 20*seconds
            self.dmg = dmg ## attacking damage
            self.img = img ## icon image

    flairmob = mob("Flair", 800, 140, 65, "flairmob")
    ratmob = mob("Rat", 50, 100, 20, "ratmob")
    azmob = mob("Az", 80000, 80, 100, "azmob") ##80 cd, 100 attack,
    # goon = mob("Goon", 300, 120, 50, "goonmob")

    ####################################################
    moblist = { ## for mobs in an encounter
                "Flair": [flairmob],
                # "Goons": [goon, goon],
                # "Alv1": [alv11, alv12, alv13],
                # "Alv2": [alv21, alv22, alv23],
                "Az": [azmob],
                "Rat": [ratmob, ratmob, ratmob]}

    ## Mob positioning.
    mobpos = {
            1:[960],
            2: [650, 1270],
            3: [400, 960, 1520]}
