define b = Character("Breeze", image="breezeside")
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
define e = Character("Evan@HorizonsNetwork", who_color="#c8ffc8")
define noa = Character("Noa from Twisted Fates")
define un = Character("? ? ? ? ?")

define n = nvl_narrator

################
## SPRITES ##
###############
image sofi = im.FactorScale("images/sprite/sofi2.png", 0.52)
image breeze = im.FactorScale("images/sprite/breeze.png", 0.26)

image cc = im.Flip(im.FactorScale("images/sprite/cc-temp.png", 1.5), horizontal=True)

##sideimage xanchor 0.5 xpos 250 yalign 1.0
image side sofiside = im.FactorScale(im.Crop("images/sprite/sofi2.png", (400, 265, 1000, 1000)), 0.4)
image side breezeside = im.FactorScale(im.Crop("images/sprite/breeze2.png", (500, 150, 1000, 1000)), 0.4)

image bgpark = "images/bg/bgpark.jpg"
image bgcafe = "images/bg/temp_bg_cafe.webp"

image white:
    Solid("#FFF")
image black:
    Solid("#000")
image pitchblack:
    Solid("#000")
image iceblue:
    Solid("#63D3FF")

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

###############
## Screen positions ##
###############
$ slightleft = Position(xpos=0.3, xanchor='left')
$ thirdleft = Position(xpos=0.2, xanchor='left')
$ halfleft = Position(xpos=0.1, xanchor='left')
$ extremeleft = Position(xpos=-0.2, xanchor='left')
$ center = Position(xpos=0.5, xanchor='center')
$ slightright = Position(xpos=0.6, xanchor='right')
$ thirdright = Position(xpos=0.75, xanchor='right')
$ halfright = Position(xpos=0.9, xanchor='right')
$ extremeright = Position(xpos=1.1, xanchor='right')