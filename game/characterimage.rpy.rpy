init python:
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
    "sprite/Sofi/mouth_open2.png"
    pause 0.08
    "sprite/Sofi/mouth_open.png"
    pause 0.1
    "sprite/Sofi/mouth_open2.png"
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
    "sprite/Sofi/mouth_open2.png"
    pause 0.08
    "sprite/Sofi/mouth_open.png"
    pause 0.1
    "sprite/Sofi/mouth_open2.png"
    pause 0.08
    "sprite/Sofi/mouth_smile.png"
    pause 0.08
    repeat
define sofi_body="normal"

define sofi_body="battle"
layeredimage Sofi2:

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
        attribute up default:
            "sprite/Sofi/eyebrows_up.png"
        attribute concerned:
            "sprite/Sofi/eyebrows_concerned.png"
        attribute down:
            "sprite/Sofi/eyebrows_angry.png"
        attribute horizontal:
            "sprite/Sofi/eyebrows_horizontal.png"
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