##############################################################
init -50 python:
    punchwipe = ImageDissolve("images/combat/vfx/grad.png", 0.3)
    shatterwipe = ImageDissolve("images/shattergrad.png", 1.0)

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
        global shieldtime
        global targettemp

        global encounter
        global aztimer
        global midtalk

        if timerpause == False:
            for i, j in enumerate(mobstat): ## individual timer.
                if mobstat[i][6]!=69420:
                    if mobstat[i][4] < mobstat[i][6]:
                        if mobstat[i][2] > 0: ## if slow
                            mobstat[i][4]+=0.25 ## 0.25x speed
                        else:
                            mobstat[i][4] += 1
                if mobstat[i][2] > 0: ## slow
                    if mobstat[i][9] > 0:
                        mobstat[i][2] -= 0.5
                    else:
                        mobstat[i][2] -= 1 ## lasts slow/20 seconds
                if mobstat[i][3] > 0: ## burn
                    mobstat[i][3] -= 1 #lasts burn/20 seconds
                    mobstat[i][1] = max(1, mobstat[i][1]- 0.25) # 5hp/second
                if mobstat[i][9] > 0: ## FREEZE
                    mobstat[i][9] -= 0.5 ## 10s = 200

            ## Commmand card timers.
            if breezecd < max(breezeex.cost):
                breezecd +=0.05
            if soficd <max(sofi.cost):
                soficd +=0.05
            if flaircd <max(flair.cost):
                flaircd +=0.05

            ## Shield Decay
            if shield > 0:
                if shieldtime <80:
                    shieldtime += 1
                else:
                    shield -= (shield//10)
            if shield == 0:
                shieldtime = 0

            ## Rat respawn ##
            if encounter == "Rat":
                for i, j in enumerate(mobstat):
                    if mobstat[i][0] == "None" and i != 3: ## if rat is dead
                        if mobstat[i][8] < 35:
                            mobstat[i][8] += 1
                        else:
                            mobstat[i] = [mob[i].name, (mob[i].hp), 0, 0, 0, mob[i].dmg, mob[i].cd, (mob[i].hp), 0, 0, 0] ## Rat replacement
                            renpy.call("ratrespawn")
            ## Alv respawn ##
            if encounter == "Alv":
                for i, j in enumerate(mobstat):
                    if mobstat[i][0] == "None": ## if hand  is dead
                        if mobstat[i][8] < (80+40*alvkill):
                            mobstat[i][8] += 1
                        else: ## hand respawn
                            mobstat[i] = [mob[i].name, (mob[i].hp), 0, 0, 0, mob[i].dmg, mob[i].cd, (mob[i].hp), 0, 0, 0, 0] ## hand replacement
                            if mobstat[abs(i-3)][0] == "None":
                                targettemp = i

            ## Alv regen ##
            if encounter == "Alv" :
                for i,j in enumerate(mobstat):
                    if mobstat[i][0] != None:
                        if mobstat[i][1] < mobstat[i][7] and mobstat[i][9] == 0 :
                            mobstat[i][10] = 0
                            mobstat[i][1] = min(mobstat[i][7], mobstat[i][1]+ mobstat[i][11])
                        elif mobstat[i][1] == mobstat[i][7]:
                            mobstat[i][10] += 0.05


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

    breeze = fighter("Breeze", ["Attack", "Shard"], [2.5, 2.0]) #2.5, 5
    sofi = fighter("Sofi", ["Shield", "Heal"], [5.0, 2.5])
    flair = fighter("Flair", ["Firebolt", "Inferno"], [3.0, 8.0]) ##3, 8
    breezeex = fighter("Breeze", ["Attack", "Shard", "Blizzard"], [1.2, 2.0, 6.0])

    skillcard = { "Attack": "cardblade",
                    "Shard": "cardice",
                    "Blizzard": "cardblizzard",
                    "Shield": "cardshield",
                    "Heal": "cardheal",
                    "Firebolt": "cardfirebolt",
                    "Inferno": "cardinferno"}
    skillvalues = { ## how much damage/heal for each command. used in damagephase.
                    "Attack": 12500, "Shard": 200,
                    "Blizzard": 0,
                    "Shield": 500, "Heal": 150,
                    "Firebolt": 150, "Inferno": 3000
                    }
    skillcd = {"Attack": 2.5, "Shard": 2,
                "Blizzard": 10,
                "Shield": 5, "Heal": 2.5,
                "Firebolt": 3, "Inferno": 8
                }
    skilldesc = {
                "Attack": "Strike it like it's hot.",
                "Shard": "ice ice baby",
                "Blizzard": "Freezes all chilled enemies, halting their actions. Frozen enemies can be shattered upon impact.",
                "Shield": "Decaying magic shield that can block incoming damage.",
                "Heal": "Replenishes health points",
                "Firebolt": "Magic missile! Magic missile!",
                "Inferno": "You see me burning, you hating."
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

    # goon = mob("Goon", 300, 120, 50, "goonmob")
    flairmob = mob("Flair", 1200, 100, 220, "flairmob") ## dps 65/7 = 8 ## transit into goons later
    g1mob = mob("Goon 1", 1000, 110, 180, "g1mob")
    g2mob = mob("Goon 2", 1200, 110, 180, "g2mob")

    ratmob = mob("Rat", 350, 70, 40, "ratmob") ## dps 20/5 = 4

    alvheadmob = mob("Vibrant Core", 10000, 69420, 0, "alvheadmob")
    alvrightmob = mob("Right Hand", 3000, 1800, 150, "alvrightmob")
    alvleftmob = mob("Left Hand", 3000, 1800, 150, "alvleftmob")

    azmob = mob("Azmaveth", 80000, 80, 300, "azmob") ## 4 unblocked hits

    nonemob = mob("None", 800, 20, 65, "alvmob")

    ####################################################
    moblist = { ## for mobs in an encounter
                "Flair": [flairmob, flairmob],
                "Goons": [g1mob, g2mob],
                "Alv": [alvheadmob, alvrightmob, alvleftmob],
                "Az": [azmob],
                "Rat": [ratmob, ratmob, ratmob, nonemob]}

    ## Mob positioning.
    mobpos = {
            1:[960],
            2: [650, 1270],
            3: [960, 450, 1470],
            4: [450, 960, 1470, 1680],
            }
