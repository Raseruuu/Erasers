init -50 python:
    breezelist = ["Attack", "Shard"]
    breezecost = [1.5, 3.0]
    breezevalue = [15, 20]

    sofilist = ["Shield", "Heal"]
    soficost = [6.0, 10.0]
    sofivalue = [10, 10]

    flairlist = ["Firebolt", "Inferno"]
    flaircost = [2.0, 10.0]
    flairvalue = [30, 70]



    class fighter:
        def __init__(self, name, list, cost, amount):
            self.name = name
            self.list = list
            self.cost = cost
            self.amount = amount

    breeze = fighter("Breeze", ["Attack", "Shard"], [1.5, 3.0], [15, 20])
    sofi = fighter("Sofi", ["Shield", "Heal"], [6.0, 10.0], [10, 100])
    flair = fighter("Flair", ["Firebolt", "Inferno"], [2.0, 10.0], [30, 70])

    skillvalues = {"Attack": 1500, "Shard": 20,
                    "Shield": 10, "Heal": 100,
                    "Firebolt": 30, "Inferno": 70
                    }

    class mob:
        def __init__(self, name, hp, cd, dmg, img):
            self.name = name
            self.hp = hp
            self.cd = cd #clickmax = 20*seconds
            self.dmg = dmg
            self.img = img

    flairmob = mob("Flair", 800, 140, 65, "flairmob")
    ratmob = mob("Rat", 300, 100, 20, "ratmob")
    ratmob2 = mob("Rat2", 300, 101, 20, "ratmob")

    moblist = {"Flair": [flairmob],
                # "Goons": [goon, goon],
                # "Alv1": [alv11, alv12, alv13],
                # "Alv2": [alv21, alv22, alv23],
                # "Az": [Az],
                "Rattest": [ratmob],
                "Rat": [ratmob, ratmob2]}

    mobpos = {1:[960], 2: [650, 1270], 3: [400, 960, 1520]}