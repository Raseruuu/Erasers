##############################################################
init -50 python:
    punchwipe = ImageDissolve("grad.png", 0.3)

    import pygame
    def ticking():
        ## Defining global variables ##
        global timerpause

        global mobattacker ## which incoming attack.
        global mobaction ## for attempting queuing up mob actions.

        global mobregen

        global breezecd
        global soficd
        global flaircd
        global shield

        global encounter
        global aztimer
        global midtalk

        if timerpause == False:
            for i, j in enumerate(mobstat): ## individual timer.
                if mobstat[i][4] < mobstat[i][6] and mobstat[i][8] == 0:
                    if mobstat[i][2] > 0: ## if slow
                        mobstat[i][4]+=0.25 ## 0.25x speed
                    else:
                        mobstat[i][4] += 1
            if mobstat[i][2] > 0: ## slow
                mobstat[i][2] -= 1 ## lasts slow/20 seconds
            if mobstat[i][3] > 0: ## burn
                mobstat[i][3] -= 1 #lasts burn/20 seconds
                mobstat[i][1] -= 0.05 # 1hp/second
            if mobstat[i][8] > 0: ## FREEZE
                mobstat[i][8] -= 1 ## 10s = 200

            ## Commmand card timers.
            if breezecd < max(breeze.cost):
                breezecd +=0.05
            if soficd <max(sofi.cost):
                soficd +=0.05
            if flaircd <max(flair.cost):
                flaircd +=0.05
            if shield > 0: ## Shield Decay
                shield -=0.05

            ## Rat respawn ##
            if encounter == "Rat":
                for i, j in enumerate(mobstat):
                    if mobstat[i][0] == "None":
                        if mobstat[i][8] == 30:
                            mobstat[i] = [mob[i].name, (mob[i].hp), 0, 0, 0, mob[i].dmg, mob[i].cd, 0, 0] ## Rat replacement
                            renpy.call("ratrespawn")
                          ## Narration
                        elif mobstat[i][8] < 30:
                            mobstat[i][8] += 1

            ## Alv regen ##
            if encounter == "Alv" :
                for i,j in enumerate(mobstat):
                    if mobstat[i][0] != None:
                        if mobstat[i][1] < mobstat[i][7] and mobstat[i][8] == 0 :
                            mobstat[i][9] = 0
                            mobstat[i][1] = min(mobstat[i][7], mobstat[i][1]+ mobregen)
                        elif mobstat[i][1] == mobstat[i][7]:
                            mobstat[i][9] += 0.05


        ## Assigning mob actions when timer up.
        for i,j in enumerate(mobstat):
            if mobstat[i][4] >= mobstat[i][6] and mobstat[i][0] != "None":
                timerpause = True
                for i,j in enumerate(mobstat):
                    if mobstat[i][4] >= mobstat[i][6] and mobstat[i][0] != "None":
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
    flair = fighter("Flair", ["Firebolt", "Inferno"], [2.0, 2.0]) ##2, 20
    breezeex = fighter("Breeze", ["Attack", "Shard", "Blizzard"], [1.5, 1.5, 3.0])

    skillvalues = { ## how much damage/heal for each command. used in damagephase.
                    "Attack": 1500, "Shard": 20,
                    "Blizzard": 0,
                    "Shield": 50, "Heal": 100,
                    "Firebolt": 30, "Inferno": 700
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

    flairmob = mob("Flair", 800, 140, 65, "flairmob") ## dps 65/7 = 8
    ratmob = mob("Rat", 50, 100, 20, "ratmob") ## dps 20/5 = 4
    azmob = mob("Az", 80000, 80, 100, "azmob") ## dps 100/4 = 25
    # goon = mob("Goon", 300, 120, 50, "goonmob")
    alvmob = mob("Alv", 500, 16000, 80, "alvmob") ## dps 80/8 = 10
    nonemob = mob("None", 800, 20, 65, "alvmob")

    ####################################################
    moblist = { ## for mobs in an encounter
                "Flair": [flairmob, flairmob],
                # "Goons": [goon, goon],
                "Alv": [alvmob, alvmob, nonemob, alvmob],
                # "Alv1": [alv11, alv12, alv13],
                # "Alv2": [alv21, alv22, alv23],
                "Az": [azmob],
                "Rat": [ratmob, ratmob, ratmob, ratmob]}

    ## Mob positioning.
    mobpos = {
            1:[960],
            2: [650, 1270],
            3: [450, 960, 1470],
            4: [240, 730, 1200, 1680]
            }
