init -3 python:
    speaking = None
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
    curried_while_speaking = renpy.curry(while_speaking)

    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
    def speaker_callback(name, event, **kwargs):
        global speaking
        if event == "begin" or event == "show":
            speaking = name
        elif (event == "slow_done" or event == "end"):
            speaking = None
    speaker = renpy.curry(speaker_callback)

image Sofi_eyes_blink:
    choice:
        "sprite/Sofi/eyes.png"
        pause 4.0
    choice:
        "sprite/Sofi/eyes_midclose.png"
        pause 0.07
        "sprite/Sofi/eyes_closed.png"
        pause 0.1
        "sprite/Sofi/eyes_midclose.png"
        pause 0.07
        "sprite/Sofi/eyes.png"
        pause 2.0
    choice:
        "sprite/Sofi/eyes_midclose.png"
        pause 0.05
        "sprite/Sofi/eyes_closed.png"
        pause 0.07
        "sprite/Sofi/eyes_midclose.png"
        pause 0.05
        "sprite/Sofi/eyes.png"
        pause 0.1
        "sprite/Sofi/eyes_midclose.png"
        pause 0.05
        "sprite/Sofi/eyes_closed.png"
        pause 0.07
        "sprite/Sofi/eyes_midclose.png"
        pause 0.05
        "sprite/Sofi/eyes.png"
        pause 2.0
    repeat
image Sofi_eyes_crying:
    choice:
        "sprite/Sofi/eyes_crying.png"
        pause 4.0
    choice:
        "sprite/Sofi/eyes_crying_midclose.png"
        pause 0.1
        "sprite/Sofi/eyes_closed.png"
        pause 0.1
        "sprite/Sofi/eyes_crying_midclose.png"
        pause 0.1
        "sprite/Sofi/eyes_crying.png"
        pause 2.0
    choice:
        "sprite/Sofi/eyes_crying_midclose.png"
        pause 0.1
        "sprite/Sofi/eyes_closed.png"
        pause 0.07
        "sprite/Sofi/eyes_crying_midclose.png"
        pause 0.1
        "sprite/Sofi/eyes_crying.png"
        pause 0.1
        "sprite/Sofi/eyes_crying_midclose.png"
        pause 0.1
        "sprite/Sofi/eyes_closed.png"
        pause 0.07
        "sprite/Sofi/eyes_crying_midclose.png"
        pause 0.1
        "sprite/Sofi/eyes_crying.png"
        pause 2.0
    repeat
image Sofi_eyes_midclose:
    choice:
        "sprite/Sofi/eyes_midclose.png"
        pause 4.0
    choice:
        "sprite/Sofi/eyes_midclose.png"
        pause 0.07
        "sprite/Sofi/eyes_closed.png"
        pause 0.2
        "sprite/Sofi/eyes_midclose.png"
        pause 0.07
        "sprite/Sofi/eyes_midclose.png"
        pause 2.0
    choice:
        "sprite/Sofi/eyes_midclose.png"
        pause 0.05
        "sprite/Sofi/eyes_closed.png"
        pause 0.07
        "sprite/Sofi/eyes_midclose.png"
        pause 0.07
        "sprite/Sofi/eyes_closed.png"
        pause 0.07
        "sprite/Sofi/eyes_midclose.png"
        pause 2.05

    repeat
# image Sofi_eyes_lookaway:
#     choice:
#         "sprite/Sofi/eyes_lookaway.png"
#         pause 8.0
#     choice:
#         "sprite/Sofi/eyes_lookaway.png"
#         pause 0.07
#         "sprite/Sofi/eyes_closed.png"
#         pause 0.1
#         "sprite/Sofi/eyes_lookaway.png"
#         pause 3.0

#     choice:
#         "sprite/Sofi/eyes_lookaway.png"
#         pause 0.05
#         "sprite/Sofi/eyes_closed.png"
#         pause 0.07
#         "sprite/Sofi/eyes_lookaway.png"
#         pause 0.07
#         "sprite/Sofi/eyes_closed.png"
#         pause 0.07
#         "sprite/Sofi/eyes_lookaway.png"
#         pause 3.0

#     repeat
image Sofi_mouth_frown_speaking:
    "sprite/Sofi/mouth_openfrown.png"
    pause 0.08
    "sprite/Sofi/mouth_open.png"
    pause 0.1
    "sprite/Sofi/mouth_openfrown.png"
    pause 0.08
    "sprite/Sofi/mouth_frown.png"
    pause 0.08
    repeat
image Sofi_mouth_smile_speaking:
    "sprite/Sofi/mouth_opensmile2.png"
    pause 0.08
    "sprite/Sofi/mouth_opensmile.png"
    pause 0.1
    "sprite/Sofi/mouth_opensmile2.png"
    pause 0.08
    "sprite/Sofi/mouth_smile.png"
    pause 0.1
    repeat
define sofi_body="normal"
# $ sofi_body="battle"
layeredimage sofi:

    always:
        "sprite/Sofi/base_[sofi_body].png"
    group eyes:
        attribute open default:
            "Sofi_eyes_blink"
        # attribute oneclose:
        #     "sprite/Sofi/Sofi_eyes2.png"
        attribute midclose:
            "Sofi_eyes_midclose"
        attribute closed:
            "sprite/Sofi/eyes_closed.png"
        # attribute lookaway:
        #     "Sofi_eyes_lookaway"
        # attribute crying:
        #     "Sofi_eyes_crying"
    group eyebrows:
        attribute normal default:
            "sprite/Sofi/eyebrows_normal.png"
        attribute worried:
            "sprite/Sofi/eyebrows_up.png"
        attribute down:
            "sprite/Sofi/eyebrows_down.png"
        # attribute default:
        #     "sprite/Sofi/eyebrows_normal.png"
    group mouth:
        attribute frown:
            WhileSpeaking("Sofi","Sofi_mouth_frown_speaking","sprite/Sofi/mouth_frown.png")
        attribute squiggly:
            WhileSpeaking("Sofi","Sofi_mouth_frown_speaking","sprite/Sofi/mouth_squiggly.png")
        attribute smile default:
            WhileSpeaking("Sofi","Sofi_mouth_smile_speaking","sprite/Sofi/mouth_smile.png")
        attribute openmouth:
            WhileSpeaking("Sofi","Sofi_mouth_frown_speaking","sprite/Sofi/mouth_open.png")
        attribute opensmile:
            WhileSpeaking("Sofi","Sofi_mouth_smile_speaking","sprite/Sofi/mouth_opensmile.png")
        attribute smug:
            WhileSpeaking("Sofi","Sofi_mouth_smile_speaking","sprite/Sofi/mouth_smug.png")
    group blush:
        attribute noblush default:
            Null()
        attribute blush:
            "sprite/Sofi/Sofi_blush.png"
            alpha 0.7
    zoom 0.5 yanchor 0.5 ypos 1.0


layeredimage azmaveth:
    always:
        "sprite/Azmaveth/Azmaveth.png"
    zoom 0.45 yanchor 0.5 ypos 1.0
####################################################################################

image Breeze_eyes_blink:
    choice:
        "sprite/Breeze/eyes.png"
        pause 4.0
    choice:
        "sprite/Breeze/eyes_midclose.png"
        pause 0.07
        "sprite/Breeze/eyes_closed.png"
        pause 0.1
        "sprite/Breeze/eyes_midclose.png"
        pause 0.07
        "sprite/Breeze/eyes.png"
        pause 2.0
    choice:
        "sprite/Breeze/eyes_midclose.png"
        pause 0.05
        "sprite/Breeze/eyes_closed.png"
        pause 0.07
        "sprite/Breeze/eyes_midclose.png"
        pause 0.05
        "sprite/Breeze/eyes.png"
        pause 0.1
        "sprite/Breeze/eyes_midclose.png"
        pause 0.05
        "sprite/Breeze/eyes_closed.png"
        pause 0.07
        "sprite/Breeze/eyes_midclose.png"
        pause 0.05
        "sprite/Breeze/eyes.png"
        pause 2.0
    repeat
image Breeze_eyes_midclose:
    choice:
        "sprite/Breeze/eyes_midclose.png"
        pause 4.0
    choice:
        "sprite/Breeze/eyes_midclose.png"
        pause 0.07
        "sprite/Breeze/eyes_closed.png"
        pause 0.2
        "sprite/Breeze/eyes_midclose.png"
        pause 0.07
        "sprite/Breeze/eyes_midclose.png"
        pause 2.0
    choice:
        "sprite/Breeze/eyes_midclose.png"
        pause 0.05
        "sprite/Breeze/eyes_closed.png"
        pause 0.07
        "sprite/Breeze/eyes_midclose.png"
        pause 0.07
        "sprite/Breeze/eyes_closed.png"
        pause 0.07
        "sprite/Breeze/eyes_midclose.png"
        pause 2.05

    repeat
# image Breeze_eyes_lookaway:
#     choice:
#         "sprite/Breeze/eyes_lookaway.png"
#         pause 8.0
#     choice:
#         "sprite/Breeze/eyes_lookaway.png"
#         pause 0.07
#         "sprite/Breeze/eyes_closed.png"
#         pause 0.1
#         "sprite/Breeze/eyes_lookaway.png"
#         pause 3.0

#     choice:
#         "sprite/Breeze/eyes_lookaway.png"
#         pause 0.05
#         "sprite/Breeze/eyes_closed.png"
#         pause 0.07
#         "sprite/Breeze/eyes_lookaway.png"
#         pause 0.07
#         "sprite/Breeze/eyes_closed.png"
#         pause 0.07
#         "sprite/Breeze/eyes_lookaway.png"
#         pause 3.0

#     repeat
image Breeze_mouth_frown_speaking:
    "sprite/Breeze/mouth_open2.png"
    pause 0.08
    "sprite/Breeze/mouth_open.png"
    pause 0.1
    "sprite/Breeze/mouth_open2.png"
    pause 0.08
    "sprite/Breeze/mouth_frown.png"
    pause 0.08
    "sprite/Breeze/mouth_open2.png"
    pause 0.08
    "sprite/Breeze/mouth_open3.png"
    pause 0.08
    "sprite/Breeze/mouth_open2.png"
    pause 0.08
    "sprite/Breeze/mouth_frown.png"
    pause 0.08
    repeat
image Breeze_mouth_smile_speaking:
    "sprite/Breeze/mouth_opensmile2.png"
    pause 0.08
    "sprite/Breeze/mouth_opensmile.png"
    pause 0.1
    "sprite/Breeze/mouth_opensmile2.png"
    pause 0.08
    "sprite/Breeze/mouth_smile.png"
    pause 0.1
    "sprite/Breeze/mouth_open2.png"
    pause 0.08
    "sprite/Breeze/mouth_open.png"
    pause 0.1
    "sprite/Breeze/mouth_open2.png"
    pause 0.08
    "sprite/Breeze/mouth_smile.png"
    pause 0.08
    repeat
define Breeze_body="normal"

# define Breeze_body="battle"
layeredimage breeze:

    always:
        "sprite/Breeze/base_[Breeze_body].png"
    group eyes:
        attribute open default:
            "Breeze_eyes_blink"
        # attribute oneclose:
        #     "sprite/Breeze/Breeze_eyes2.png"
        attribute midclose:
            "Breeze_eyes_midclose"
        attribute closed:
            "sprite/Breeze/eyes_closed.png"
        # attribute lookaway:
        #     "Breeze_eyes_lookaway"
        # attribute crying:
        #     "Breeze_eyes_crying"
    group eyebrows:
        attribute down default:
            "sprite/Breeze/eyebrows_mad.png"
        attribute straight:
            "sprite/Breeze/eyebrows_straight.png"
        attribute down2:
            "sprite/Breeze/eyebrows_mad2.png"
        attribute up:
            "sprite/Breeze/eyebrows_up.png"
    group mouth:
        attribute frown default:
            WhileSpeaking("Breeze","Breeze_mouth_frown_speaking","sprite/Breeze/mouth_frown.png")
        attribute squiggly:
            WhileSpeaking("Breeze","Breeze_mouth_frown_speaking","sprite/Breeze/mouth_squiggly.png")
        attribute smile:
            WhileSpeaking("Breeze","Breeze_mouth_smile_speaking","sprite/Breeze/mouth_smile.png")
        attribute openmouth:
            WhileSpeaking("Breeze","Breeze_mouth_frown_speaking","sprite/Breeze/mouth_open.png")
        attribute opensmile:
            WhileSpeaking("Breeze","Breeze_mouth_smile_speaking","sprite/Breeze/mouth_opensmile.png")
        attribute smug:
            WhileSpeaking("Breeze","Breeze_mouth_smile_speaking","sprite/Breeze/mouth_smug.png")
    group blush:
        attribute noblush default:
            Null()
        attribute blush:
            "sprite/Breeze/Breeze_blush.png"
            alpha 0.7
    zoom 0.5 yanchor 0.5 ypos 1.0

#####################################################################################

image Flair_eyes_blink:
    choice:
        "sprite/Flair/eyes.png"
        pause 4.0
    choice:
        "sprite/Flair/eyes_midclose.png"
        pause 0.07
        "sprite/Flair/eyes_closed.png"
        pause 0.1
        "sprite/Flair/eyes_midclose.png"
        pause 0.07
        "sprite/Flair/eyes.png"
        pause 2.0
    choice:
        "sprite/Flair/eyes_midclose.png"
        pause 0.05
        "sprite/Flair/eyes_closed.png"
        pause 0.07
        "sprite/Flair/eyes_midclose.png"
        pause 0.05
        "sprite/Flair/eyes.png"
        pause 0.1
        "sprite/Flair/eyes_midclose.png"
        pause 0.05
        "sprite/Flair/eyes_closed.png"
        pause 0.07
        "sprite/Flair/eyes_midclose.png"
        pause 0.05
        "sprite/Flair/eyes.png"
        pause 2.0
    repeat
image Flair_eyes_midclose:
    choice:
        "sprite/Flair/eyes_midclose.png"
        pause 4.0
    choice:
        "sprite/Flair/eyes_midclose.png"
        pause 0.07
        "sprite/Flair/eyes_closed.png"
        pause 0.2
        "sprite/Flair/eyes_midclose.png"
        pause 0.07
        "sprite/Flair/eyes_midclose.png"
        pause 2.0
    choice:
        "sprite/Flair/eyes_midclose.png"
        pause 0.05
        "sprite/Flair/eyes_closed.png"
        pause 0.07
        "sprite/Flair/eyes_midclose.png"
        pause 0.07
        "sprite/Flair/eyes_closed.png"
        pause 0.07
        "sprite/Flair/eyes_midclose.png"
        pause 2.05

    repeat
# image Flair_eyes_lookaway:
#     choice:
#         "sprite/Flair/eyes_lookaway.png"
#         pause 8.0
#     choice:
#         "sprite/Flair/eyes_lookaway.png"
#         pause 0.07
#         "sprite/Flair/eyes_closed.png"
#         pause 0.1
#         "sprite/Flair/eyes_lookaway.png"
#         pause 3.0

#     choice:
#         "sprite/Flair/eyes_lookaway.png"
#         pause 0.05
#         "sprite/Flair/eyes_closed.png"
#         pause 0.07
#         "sprite/Flair/eyes_lookaway.png"
#         pause 0.07
#         "sprite/Flair/eyes_closed.png"
#         pause 0.07
#         "sprite/Flair/eyes_lookaway.png"
#         pause 3.0

#     repeat
image Flair_mouth_frown_speaking:
    "sprite/Flair/mouth_open2.png"
    pause 0.08
    "sprite/Flair/mouth_open.png"
    pause 0.1
    "sprite/Flair/mouth_open2.png"
    pause 0.08
    "sprite/Flair/mouth_frown.png"
    pause 0.08
    "sprite/Flair/mouth_open.png"
    pause 0.1
    "sprite/Flair/mouth_openfrown2.png"
    pause 0.08
    "sprite/Flair/mouth_openfrown.png"
    pause 0.08
    "sprite/Flair/mouth_openfrown2.png"
    pause 0.08
    "sprite/Flair/mouth_frown.png"
    pause 0.08
    repeat
image Flair_mouth_smile_speaking:
    "sprite/Flair/mouth_opensmile2.png"
    pause 0.08
    "sprite/Flair/mouth_opensmile.png"
    pause 0.1
    "sprite/Flair/mouth_opensmile2.png"
    pause 0.08
    "sprite/Flair/mouth_smile.png"
    pause 0.1
    "sprite/Flair/mouth_open2.png"
    pause 0.08
    "sprite/Flair/mouth_open.png"
    pause 0.1
    "sprite/Flair/mouth_open2.png"
    pause 0.08
    "sprite/Flair/mouth_smile.png"
    pause 0.08
    repeat

image Flair_fire:
    "sprite/Flair/fire_1.png"
    pause .2
    "sprite/Flair/fire_2.png"
    pause .2
    "sprite/Flair/fire_3.png"
    pause .2
    "sprite/Flair/fire_4.png"
    pause .2
    repeat
define Flair_body="withcoat"

# define Flair_body="battle"
layeredimage flair:

    always:
        "sprite/Flair/base_[Flair_body].png"
    group eyes:
        attribute open default:
            "Flair_eyes_blink"
        # attribute oneclose:
        #     "sprite/Flair/Flair_eyes2.png"
        attribute midclose:
            "Flair_eyes_midclose"
        attribute closed:
            "sprite/Flair/eyes_closed.png"
        # attribute lookaway:
        #     "Flair_eyes_lookaway"
        # attribute crying:
        #     "Flair_eyes_crying"
    group eyebrows:
        attribute up default:
            "sprite/Flair/eyebrows_up.png"
        attribute oneup:
            "sprite/Flair/eyebrows_1up.png"
        attribute down:
            "sprite/Flair/eyebrows_down.png"
        attribute worried:
            "sprite/Flair/eyebrows_worried.png"
    group mouth:
        attribute frown default:
            WhileSpeaking("Flair","Flair_mouth_frown_speaking","sprite/Flair/mouth_frown.png")
        attribute squiggly:
            WhileSpeaking("Flair","Flair_mouth_frown_speaking","sprite/Flair/mouth_squiggly.png")
        attribute smile:
            WhileSpeaking("Flair","Flair_mouth_smile_speaking","sprite/Flair/mouth_smile.png")
        attribute openmouth:
            WhileSpeaking("Flair","Flair_mouth_frown_speaking","sprite/Flair/mouth_open.png")
        attribute opensmile:
            WhileSpeaking("Flair","Flair_mouth_smile_speaking","sprite/Flair/mouth_opensmile.png")
        attribute smug:
            WhileSpeaking("Flair","Flair_mouth_smile_speaking","sprite/Flair/mouth_smug.png")
    group blush:
        attribute nofire :
            Null()
        attribute fire default:
            "Flair_fire"
    # group blush:
    #     attribute noblush default:
    #         Null()
    #     attribute blush:
    #         "sprite/Flair/Flair_blush.png"
    #         alpha 0.7
    zoom 0.5 yanchor 0.5 ypos 1.0

image Alverna_eyes_blink:
    choice:
        "sprite/Alverna/eyes.png"
        pause 4.0
    choice:
        "sprite/Alverna/eyes_midclose.png"
        pause 0.07
        "sprite/Alverna/eyes_closed.png"
        pause 0.1
        "sprite/Alverna/eyes_midclose.png"
        pause 0.07
        "sprite/Alverna/eyes.png"
        pause 2.0
    choice:
        "sprite/Alverna/eyes_midclose.png"
        pause 0.05
        "sprite/Alverna/eyes_closed.png"
        pause 0.07
        "sprite/Alverna/eyes_midclose.png"
        pause 0.05
        "sprite/Alverna/eyes.png"
        pause 0.1
        "sprite/Alverna/eyes_midclose.png"
        pause 0.05
        "sprite/Alverna/eyes_closed.png"
        pause 0.07
        "sprite/Alverna/eyes_midclose.png"
        pause 0.05
        "sprite/Alverna/eyes.png"
        pause 2.0
    repeat
image Alverna_eyes_crying:
    choice:
        "sprite/Alverna/eyes_crying.png"
        pause 4.0
    choice:
        "sprite/Alverna/eyes_crying_midclose.png"
        pause 0.1
        "sprite/Alverna/eyes_closed.png"
        pause 0.1
        "sprite/Alverna/eyes_crying_midclose.png"
        pause 0.1
        "sprite/Alverna/eyes_crying.png"
        pause 2.0
    choice:
        "sprite/Alverna/eyes_crying_midclose.png"
        pause 0.1
        "sprite/Alverna/eyes_closed.png"
        pause 0.07
        "sprite/Alverna/eyes_crying_midclose.png"
        pause 0.1
        "sprite/Alverna/eyes_crying.png"
        pause 0.1
        "sprite/Alverna/eyes_crying_midclose.png"
        pause 0.1
        "sprite/Alverna/eyes_closed.png"
        pause 0.07
        "sprite/Alverna/eyes_crying_midclose.png"
        pause 0.1
        "sprite/Alverna/eyes_crying.png"
        pause 2.0
    repeat
image Alverna_eyes_midclose:
    choice:
        "sprite/Alverna/eyes_midclose.png"
        pause 4.0
    choice:
        "sprite/Alverna/eyes_midclose.png"
        pause 0.07
        "sprite/Alverna/eyes_closed.png"
        pause 0.2
        "sprite/Alverna/eyes_midclose.png"
        pause 0.07
        "sprite/Alverna/eyes_midclose.png"
        pause 2.0
    choice:
        "sprite/Alverna/eyes_midclose.png"
        pause 0.05
        "sprite/Alverna/eyes_closed.png"
        pause 0.07
        "sprite/Alverna/eyes_midclose.png"
        pause 0.07
        "sprite/Alverna/eyes_closed.png"
        pause 0.07
        "sprite/Alverna/eyes_midclose.png"
        pause 2.05

    repeat
image Alverna_mouth_frown_speaking:
    "sprite/Alverna/mouth_openfrown.png"
    pause 0.08
    "sprite/Alverna/mouth_open.png"
    pause 0.1
    "sprite/Alverna/mouth_openfrown.png"
    pause 0.08
    "sprite/Alverna/mouth_frown.png"
    pause 0.08
    repeat
image Alverna_mouth_smile_speaking:
    "sprite/Alverna/mouth_opensmile2.png"
    pause 0.08
    "sprite/Alverna/mouth_opensmile.png"
    pause 0.1
    "sprite/Alverna/mouth_opensmile2.png"
    pause 0.08
    "sprite/Alverna/mouth_smile.png"
    pause 0.1
    repeat
define Alverna_body="normal"
# $ Alverna_body="battle"
layeredimage Alverna:

    always:
        "sprite/Alverna/Alverna.png"
    # group eyes:
    #     # attribute open :
    #     #     "Alverna_eyes_blink"
    #     attribute up default:
    #         "Alverna_eyes_up"
    #     attribute closed:
    #         "sprite/Alverna/eyes_closed.png"
    #     # attribute lookaway:
    #     #     "Alverna_eyes_lookaway"
    #     # attribute crying:
    #     #     "Alverna_eyes_crying"
    # group eyebrows:
    #     attribute normal default:
    #         "sprite/Alverna/eyebrows_normal.png"
    #     attribute worried:
    #         "sprite/Alverna/eyebrows_up.png"
    #     attribute down:
    #         "sprite/Alverna/eyebrows_down.png"
    #     # attribute default:
    #     #     "sprite/Alverna/eyebrows_normal.png"
    # group mouth:
    #     attribute frown default:
    #         WhileSpeaking("Alverna","Alverna_mouth_frown_speaking","sprite/Alverna/mouth_frown.png")
    #     attribute openmouth:
    #         WhileSpeaking("Alverna","Alverna_mouth_frown_speaking","sprite/Alverna/mouth_open.png")
    #     attribute opensmile:
    #         WhileSpeaking("Alverna","Alverna_mouth_smile_speaking","sprite/Alverna/mouth_opensmile.png")
    #     attribute noblush default:
    #         Null()
    #     attribute blush:
    #         "sprite/Alverna/Alverna_blush.png"
    #         alpha 0.7
    zoom 0.5 yanchor 0.5 ypos 1.0
