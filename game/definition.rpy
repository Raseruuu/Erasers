
define b = Character("Breeze", image="breezeside",callback=speaker("Breeze"))
define s = Character("Sofi",image="sofiside",callback=speaker("Sofi"))
define f = Character("Flair",callback=speaker("Flair"),)
define a = Character("Azmaveth",image="azside", callback=speaker("Azmaveth"),)
define k = Character("Kizuna",callback=speaker("Kizuna"),)

define ke = Character("Kephirah",callback=speaker("Kephirah"),)

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
# ###############

# MOVED TO characterimage.rpy
image az = im.FactorScale("images/sprite/temp-laughinghand.webp", 1.0)


image cc = im.Flip(im.FactorScale("images/sprite/cc-temp.png", 1.5), horizontal=True)

##sideimage xanchor 0.5 xpos 250 yalign 1.0
# image side sofiside = im.FactorScale(im.Crop(sofi, (400, 265, 1000, 1000)), 0.4)
image side sofiside:
    LiveCrop((220,80, 460,500), "sofi")
    zoom 0.8
image side breezeside:
    LiveCrop((260,60, 460,500), "breeze")
    zoom 0.8
image side azside = "images/sprite/aztemp.png"
# image side breezeside = im.FactorScale(im.Crop(breeze, (500, 150, 1000, 1000)), 0.4)
transform left:
    xpos 0.2 xanchor 0.5
transform right:
    xpos 0.8 xanchor 0.5
transform center:
    xpos 0.5 xanchor 0.5
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
init:
    $ slightleft = Position(xpos=0.3, xanchor='left')
    $ thirdleft = Position(xpos=0.2, xanchor='left')
    $ halfleft = Position(xpos=0.1, xanchor='left')
    $ extremeleft = Position(xpos=-0.2, xanchor='left')
    $ center = Position(xpos=0.5, xanchor='center')
    $ slightright = Position(xpos=0.6, xanchor='right')
    $ thirdright = Position(xpos=0.75, xanchor='right')
    $ halfright = Position(xpos=0.9, xanchor='right')
    $ extremeright = Position(xpos=1.3, xanchor='right')

#################
## Transitions ##
#################
define shatter_in = ImageDissolve("/images/shatter.png", 6.0)
define shatter_out = ImageDissolve("/images/shatter.png", 6.0, reverse=True)
