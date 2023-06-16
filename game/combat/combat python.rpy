init python:
    import pygame
    def tick():
        ## Defining global variables ##
        global click
        global clickmax
        if click < clickmax:
            click += 2
        if click == clickmax:
            renpy.call("damage")
