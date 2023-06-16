define b = Character("Breeze")
define s = Character("Sofi", image="sofiside")
define f = Character("Flair")
define a = Character("Azmaveth")
define k = Character("Kizuna")

define u = Character("???")
define cc = Character("Cafe Cashier")
define g1 = Character("Goon 1")
define g2 = Character("Goon 2")
define ms = Character("Magic Scientist")
define fi = Character("Intercom")

define n = nvl_narrator

################
## SPRITES ##
###############
image sofi = im.FactorScale("images/sofi.png", 0.26)
image breeze = im.FactorScale("images/breeze.png", 0.26)

image cc = im.Flip(im.FactorScale("images/cc-temp.png", 1.5), horizontal=True)

##sideimage xanchor 0.5 xpos 250 yalign 1.0
image side sofiside = im.FactorScale(im.Crop("images/sofi.png", (850, 530, 1700, 2000)), 0.25)

image bgpark = "images/bg/bgpark.jpg"
image bgcafe = "images/bg/temp_bg_cafe.webp"

image white:
    Solid("#FFF")
image black:
    Solid("#000")

image bgcafesepia = im.Sepia("bg_cafe.webp")
################
## MUSIC ##
################
define flairtheme = "sound/Flairs_Theme_2_ogg.ogg"
define guildtheme = "sound/Guild_Theme_ogg.ogg"
define tomotheme = "sound/Tomos_Theme_ogg.ogg"


define horror = "sound/temp-youfulca/youfulca-Horror-ginen_loop.ogg"
define daily = "sound/temp-youfulca/youfulca-tea-time_loop.ogg"

###############
## Transform ##
###############
transform scenter:
    yanchor 0 ypos 150 xalign 0.5 #zoom 0.65
transform sright:
    yanchor 0 ypos 150 xanchor 0.5 xpos 0.8
transform sleft:
    yanchor 0 ypos 150 xanchor 0.5 xpos 0.2

transform cutejump:
    linear 0.08 yoffset -100
    linear 0.08 yoffset +0
    repeat 1
transform midjump:
    linear 0.10 yoffset -250
    linear 0.10 yoffset +0
    repeat 1
transform wside:
    linear 0.2 xoffset -300
transform test1:
    parallel:
        midjump
    parallel:
        wside
    pause 0.1
    flipflip

transform flipflip:
    linear 0.1 xzoom -1
