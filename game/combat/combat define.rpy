image breezecombat = im.FactorScale(im.Crop("images/sprite/breeze2.png", (600, 150, 850, 1000)), 0.3)
## Enemies ##
image flairmob = im.FactorScale(im.Crop("images/sprite/flairc.png", (000, 100, 2200, 3000)), 0.16) #200
image ratmob = im.FactorScale("images/sprite/rat.png", 0.6)
image azmob = im.FactorScale("images/sprite/temp-laughinghand.webp", 0.5)
image alvmob = im.FactorScale("images/sprite/blame-anime.gif", 0.5)
image greenmob = "images/sprite/green.png"

image targetsign = im.FactorScale("gui/target.png", 0.3)

##debuff signs
image fire = im.FactorScale("gui/fire.png", 0.3)
image ice = im.FactorScale("gui/ice.png", 0.05)

## Battle Music
define battle = "sound/Battle_Theme_ogg.ogg"
define overtheblood = "sound/temp/youfulca-over-the-blood_loop.ogg"
define gameover = "sound/temp/youfulca-Horror-juki_loop.ogg"
define tanzanite = "sound/temp/BGM_Theme3_Tanzanite_FSPC2.ogg"
################################################################
## ATK VFX
image atkblade = im.FactorScale("blade.png", 0.5)
image atkshard = im.FactorScale("shard.png", 0.5)
# image atkshield
# image atkheal
# image atkfirebolt
image atkinferno = im.FactorScale("inferno.png", 2.5)

## attacking sfx
define blade = "sound/sfx/pigmyon/swordstrike.mp3"
define ice = "sound/sfx/pigmyon/shard.mp3"
##TODO: heal
##TODO: shield
##TODO: Firebolt
define inferno = "sound/sfx/opengameart/foom_0.ogg"
###############################################################

## defending sfx
define hit = "sound/sfx/opengameart/swing2.ogg" ## default hit sound
    ### AZ
define swish9 = "sound/sfx/opengameart/swish-9.ogg" ## az punch
define swordclash = "sound/sfx/freesoundeffects/steelsword.mp3" ## parried
define swordblock = "sound/sfx/pigmyon/swordblock.mp3"
define punch2 = "sound/sfx/freesoundeffects/punch2.mp3" ##az punch land

## AZ FIGHT
image punching = "battle effect 3b.png"
image punchpre = "punchpre.png"
image punchpost = "punchpost.png"
image punchparry = "battle effect 12.png"






##################################################
## TRANSFORMS ##
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
