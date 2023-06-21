init -50 python:
    class fighter:
        def __init__(self, name, list, cost):
            self.name = name
            self.list = list
            self.cost = cost

    breeze = fighter("Breeze", ["Attack", "Shard"], [1.5, 3.0])
    sofi = fighter("Sofi", ["Shield", "Heal"], [6.0, 10.0])
    flair = fighter("Flair", ["Firebolt", "Inferno"], [2.0, 20.0])

    skillvalues = { ## how much damage/heal for each command. used in damagephase.
                    "Attack": 15, "Shard": 20,
                    "Shield": 10, "Heal": 100,
                    "Firebolt": 30, "Inferno": 70
                    }

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
    azmob = mob("Az", 80000, 80, 100, "azmob") ##200 attack, 80 cd

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
