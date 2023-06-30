label combatroom:
    k "Welcome to the training facility. Here you can revisit all the fun times of playing against those enemies."
    k "Now before further ado, here's the mystery door."
    show screen combatroom
    pause
    return

screen combatroom:
    fixed:
        # grid (2, 2):
        #     text "Hi"
        text "yo"

        ## 2x2 grid of the enemies, click to encounter and precombat.
