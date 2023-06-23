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
image sofi = im.FactorScale("images/sprite/sofi.png", 0.26)
image breeze = im.FactorScale("images/sprite/breeze.png", 0.26)

image cc = im.Flip(im.FactorScale("images/sprite/cc-temp.png", 1.5), horizontal=True)

##sideimage xanchor 0.5 xpos 250 yalign 1.0
image side sofiside = im.FactorScale(im.Crop("images/sprite/sofi.png", (850, 530, 1700, 2000)), 0.25)

image bgpark = "images/bg/bgpark.jpg"
image bgcafe = "images/bg/temp_bg_cafe.webp"

image white:
    Solid("#FFF")
image black:
    Solid("#000")
image pitchblack:
    Solid("#000")

image bgcafesepia = im.Sepia("images/bg/temp_bg_cafe.webp")
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

##################################################
## COMBAT RELATED HERE ##
##################################################
transform combat1: ##1enemy placement
    xalign 0.5 yanchor 0.5 ypos 450

transform combat2: ## target placement
    anchor (0.5, 0.5)
    ypos 400

transform mobhurt:
    parallel: #Horizontal shake
        pause 0.1
        ease 0.05 xoffset 10
        ease 0.05 xoffset -10
        ease 0.05 xoffset 8
        ease 0.05 xoffset -8
        ease 0.05 xoffset 5
        ease 0.05 xoffset -5
        ease 0.05 xoffset 0
    parallel:
        linear 0.05 zoom 0.98 yoffset 10
        linear 0.15 zoom 1.02 yoffset -5
        easeout 0.1 zoom 1.0 yoffset 0
transform textpopup:
    alpha 0.5
    linear 0.2 alpha 1.0 yoffset -50


transform atkblade:
    yoffset -50 xoffset 100
    ease 0.2 yoffset +150 xoffset -100
    ease 0.1 alpha 0.0

transform atkshard:
    yoffset -150
    pause 0.1
    ease 0.1 yoffset -200
    pause 0.05
    # 0.25s setup
    ease 0.1 yoffset +0
    pause 0.55
    linear 0.1 alpha 0.0

transform atkinferno:
    xanchor 1.0 xpos 0.0 alpha 0.7
    ease 0.7 xanchor 0.0 xpos 1.0
