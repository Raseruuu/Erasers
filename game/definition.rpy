
define b = Character("Breeze", image="breezeside",callback=speaker("Breeze"), who_font="mangat.ttf",)
define s = Character("Sofi",image="sofiside",callback=speaker("Sofi"), who_font="mangat.ttf")
define f = Character("Flair",image="flairside",callback=speaker("Flair"), who_font="mangat.ttf",)
define a = Character("Azmaveth",image="azmavethside", callback=speaker("Azmaveth"), who_font="mangat.ttf")
define k = Character("Kizuna",image="kizunaside",callback=speaker("Kizuna"), who_font="mangat.ttf",)
define tm = Character("Alverna",image="alvernaside",callback=speaker("Alverna"), who_font="mangat.ttf",)
# define az = Character("Azmaveth",callback=speaker("Azmaveth"),)
define ke = Character("Kephirah",callback=speaker("Kephirah"), who_font="mangat.ttf",)

define u = Character("???")
define cc = Character("Cafe Cashier")
define g1 = Character("Goon 1", image="g1side")
define g2 = Character("Goon 2", image="g2side")
define ms = Character("Mag. Scientist")
define fl = Character("Intercom")
define fi = Character("Intercom") ## it's written as FL and FI in the script. duplicate is to save time from having to fix all occurrences.
define e = Character("Evan", who_color="#c8ffc8")
define noa = Character("Noa")
define un = Character("? ? ? ? ?")

define n = nvl_narrator

init -100 python:
    persistent.firsttime = True
################
## SPRITES ##
# ###############

# MOVED TO characterimage.rpy
# image az = im.FactorScale("images/sprite/Azmaveth/Azmaveth.png", 0.25)
image g1:
    "images/sprite/grunt1.png"
    zoom 0.5 yanchor 0.5 ypos 1.0
image g2:
    "images/sprite/grunt2.png"
    zoom 0.5 yanchor 0.5 ypos 1.0
image ms:
    "images/sprite/ms.png"
    zoom 0.5 yanchor 0.5 ypos 1.0
image cc = im.Flip(im.FactorScale("images/sprite/cc-temp.png", 1.5), horizontal=True)

##sideimage xanchor 0.5 xpos 250 yalign 1.0
# image side sofiside = im.FactorScale(im.Crop(sofi, (400, 265, 1000, 1000)), 0.4)
# image side sofiside:
#     LiveCrop((220,80, 460,500), LayeredImageProxy("sofi"))
#     zoom 0.8

image side sofiside = LayeredImageProxy("sofi", Transform(crop=(220, 120, 460, 500), zoom=0.8))
image side breezeside =  LayeredImageProxy("breeze", Transform(crop=(260, 80, 460, 500), zoom=0.8))
image side flairside =  LayeredImageProxy("flair", Transform(crop=(260, 80, 460, 500), zoom=0.8))
image side alvernaside =  LayeredImageProxy("Alverna", Transform(crop=(260, 140, 460, 500), zoom=0.8))
image side kizunaside =  LayeredImageProxy("Kizuna", Transform(crop=(200, 80, 460, 500), zoom=0.8))
image side azmavethside =  LayeredImageProxy("azmaveth", Transform(crop=(280, 0, 460, 500), zoom=0.8))

# s down openmouth ""


image side azside:
    LiveCrop((260,60, 460,500), "images/sprite/Azmaveth/Azmaveth.png")
    zoom 0.4
# image side breezeside = im.FactorScale(im.Crop(breeze, (500, 150, 1000, 1000)), 0.4)
image side g1side:
    LiveCrop((200,120, 460,500), "g1")
    zoom 0.8
image side g2side:
    LiveCrop((200,120, 460,500), "g2")
    zoom 0.8


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
image shieldgreen:
    Solid("#00FF66")

image bgcafesepia = im.Sepia("images/bg/temp_bg_cafe.webp")

## UI buttons
image quickauto = im.Crop("gui/buttons.png",(0, 0, 16, 16))
$ quickhover = ["History", "Auto"]
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
