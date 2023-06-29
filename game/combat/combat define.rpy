# image breezecombat = im.FactorScale(im.Crop("images/sprite/breeze2.png", (600, 150, 850, 1000)), 0.3)
image breezecombat = At("side breezeside", resize(0.75))

## Enemies ##
image flairmob = im.FactorScale(im.Crop("images/sprite/flairc.png", (000, 100, 2200, 3000)), 0.16) #200
image g1mob = im.FactorScale(im.Crop("images/sprite/grunt1.png", (100, 250, 1500, 3250)), 0.15)
image g2mob = im.FactorScale(im.Crop("images/sprite/grunt2.png", (100, 250, 1500, 3250)), 0.15)
image ratmob = im.FactorScale("images/sprite/rat.png", 0.6)
#TODO: image alvmob =
image alvmob = im.FactorScale("images/sprite/blame-anime.gif", 0.5)
## TODO: update AZ
image azmob = im.FactorScale(im.Crop("images/sprite/Azmaveth/Azmaveth.png", (0, 0, 2597, 4500)), 0.15)
## placeholder
image greenmob = "images/sprite/green.png"

##debuff signs
image fire = im.FactorScale("gui/fire.png", 0.3)
image ice = im.FactorScale("gui/ice.png", 0.05)
image targetsign = im.FactorScale("gui/target1.png", 0.3)

## command cards ####################
# python:
    # for i in ["cardblade", "cardice", "cardblizzard", "cardshield", "cardheal", "cardfirebolt", "cardinferno"]:
    #     image i = "images/combat/cards/"+i+".png"
image cardblade = "images/combat/cards/cardblade.png"
image cardice = "images/combat/cards/cardice.png"
image cardblizzard = "images/combat/cards/cardblizzard.png"
image cardshield = "images/combat/cards/cardshield.png"
image cardheal = "images/combat/cards/cardheal.png"
image cardfirebolt = "images/combat/cards/cardfirebolt.png"
image cardinferno = "images/combat/cards/cardinferno.png"

image cardblade2 = im.Blur(im.Grayscale("images/combat/cards/cardblade.png"), 1)
image cardice2 = im.Blur(im.Grayscale("images/combat/cards/cardice.png"), 1)
image cardblizzard2 = im.Blur(im.Grayscale("images/combat/cards/cardblizzard.png"), 1)
image cardshield2 = im.Blur(im.Grayscale("images/combat/cards/cardshield.png"), 1)
image cardheal2 = im.Blur(im.Grayscale("images/combat/cards/cardheal.png"), 1)
image cardfirebolt2 = im.Blur(im.Grayscale("images/combat/cards/cardfirebolt.png"), 1)
image cardinferno2 = im.Blur(im.Grayscale("images/combat/cards/cardinferno.png"), 1)

## Battle Music #######################################################
## First 2, pending replacement
define battle = "sound/Battle_Theme_ogg.ogg"
## Alv fight
define tanzanite = "sound/temp/BGM_Theme3_Tanzanite_FSPC2.ogg"
## AZ fight
define overtheblood = "sound/temp/youfulca-over-the-blood_loop.ogg"
## Gameover music
define gameover = "sound/temp/youfulca-Horror-juki_loop.ogg"
################################################################
## ATK VFX ## TODO
image atkblade = im.FactorScale("images/combat/vfx/blade.png", 0.5)
image atkshard = im.FactorScale("images/combat/vfx/shard.png", 0.5)
# image atkshield
# image atkheal
# image atkfirebolt
image atkinferno = im.FactorScale("images/combat/vfx/inferno.png", 2.5)
# image atkblizzard =
# image atkiceblock =

## ATK SFX
define blade = "sound/sfx/pigmyon/swordstrike.mp3"
define ice = "sound/sfx/wowsound/RPG3_IceMagic2_LightImpact01_.mp3" #"sound/sfx/pigmyon/shard.mp3"
define healing = "sound/sfx/wowsound/RPG_Buff_08.mp3"
define shielding = "sound/sfx/wowsound/RPG3_MagicCute_P1_Cast_.mp3"
define firebolt = "sound/sfx/wowsound/RPG3_FireMagicBall_Projectile04_.mp3"
define inferno = "sound/sfx/wowsound/RPG3_FireMagic_Drone01_FireTornado_Loop_.mp3" #"sound/sfx/opengameart/foom_0.ogg"
define blizzard = "sound/sfx/wowsound/RPG3_IceMagic_Cast01_.mp3"
# define iceblock = "sound/sfx/wowsound/RPG3_MagicCute_P1_Cast_.mp3" #???
# define hiticeblock = "RPG3_IceMagic2_LightImpact04Critv2_Longer_" ##when hit when iceblock on
###############################################################

## defending sfx
define hit = "sound/sfx/opengameart/swing2.ogg" ## default hit sound
    ### AZ
define swish9 = "sound/sfx/opengameart/swish-9.ogg" ## az punch
define swordclash = "sound/sfx/freesoundeffects/steelsword.mp3" ## parried
define swordblock = "sound/sfx/pigmyon/swordblock.mp3"
define punch2 = "sound/sfx/freesoundeffects/punch2.mp3" ##az punch land

## AZ FIGHT
image punching = "images/combat/vfx/battle effect 3b.png"
image punchpre = "images/combat/vfx/punchpre.png"
image punchpost = "images/combat/vfx/punchpost.png"
image punchparry = "images/combat/vfx/battle effect 12.png"

##################################################
## TRANSFORMS ##
##################################################
transform combat1: ##1enemy placement
    xalign 0.5 yanchor 0.5 ypos 450

transform combat2: ## target placement
    anchor (0.5, 0.5)
    ypos 400

transform mobhurt: ##not used iirc
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


transform textpopup: ## for damage numbers
    alpha 0.5
    ease 0.1 alpha 1.0 yoffset -30
    ease 0.05 yoffset -20

########################################
## ATK ANIMATIONS ##
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
