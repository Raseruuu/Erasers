label credits:
    # scene white
    scene black with dissolve
    hide screen main_menu
    pause 1.0
    centered "{size=+30}{cps=30}Raseruuu{/cps}{/size} {cps=20}{size=+10}\n\nSprite Artist \n\nCharacters \n\nStory Concept{/cps}{/size}{p=3.0}{nw}" with dissolve
    centered "{size=+30}{cps=30}Dusk{/cps}{/size} {cps=20}{size=+10}\n\nWriter \n\nSequence of Events Director \n\nStory Revisions \n\nActual Monster{/cps}{/size}{p=3.0}{nw}" with dissolve
    centered "{size=+30}{cps=30}Kamataya{/cps}{/size} {cps=20}{size=+10}\n\nScript Writer \n\nDialogue/Monologue{/cps}{/size}{p=3.0}{nw}" with dissolve
    centered "{size=+30}{cps=30}Jeroz{/cps}{/size} {cps=20}{size=+10}\n\nStory Concept\n\nScene UI design \n\nTime-Attack Action Time Battle \n\nGameplay Programming{/cps}{/size}{p=3.0}{nw}" with dissolve
    centered "{size=+30}{cps=30}Khanondrum{/cps}{/size} {cps=20}{size=+10}\n\nRen'py programmer \n\nAssets programming{/cps}{/size}{p=3.0}{nw}" with dissolve
    centered "{size=+30}{cps=30}James Blackwell{/cps}{/size} {cps=20}{size=+10}\n\nOriginal Music{/cps}{/size}{p=3.0}{nw}" with dissolve
    centered "{size=+30}{cps=30}Pleinar{/cps}{/size} {cps=20}{size=+10}\n\nBackground Art{/cps}{/size}{p=3.0}{nw}" with dissolve
    show side breezeside with dissolve
    centered "{size=+30}{cps=30}Gale Rivera{/cps}{/size} {cps=20}{size=+10}\n\nBreeze{/cps}{/size}{p=3.0}{nw}" with dissolve
    # hide side breezeside
    show side sofiside with dissolve
    centered "{size=+30}{cps=30}Lauren Kong{/cps}{/size} {cps=20}{size=+10}\n\nSofi{/cps}{/size}{p=3.0}{nw}" with dissolve
    hide side sofiside
    show side kizunaside with dissolve
    centered "{size=+30}{cps=30}Shakyra Dunn{/cps}{/size} {cps=20}{size=+10}\n\nKizuna{/cps}{/size}{p=3.0}{nw}" with dissolve
    hide side kizunaside
    show side flairside with dissolve
    centered "{size=+30}{cps=30}Sayaka Mashiro{/cps}{/size} {cps=20}{size=+10}\n\nFlair{/cps}{/size}{p=3.0}{nw}" with dissolve
    hide side flairside
    show side alvernaside with dissolve
    centered "{size=+30}{cps=30}RedVelvetVA{/cps}{/size} {cps=20}{size=+10}\n\nAlverna{/cps}{/size}{p=3.0}{nw}" with dissolve
    hide side alvernaside
    centered "{size=+30}{cps=30}Thanks For Playing{/cps}{/size} {cps=20}{size=+10}\n\nUpdate Coming Soon{/cps}{/size}{p=3.0}{nw} {cps=20}{size=+5}\n\...Probably{p=1.0}" with dissolve
    pause 2
    show screen main_menu
    return

screen credits:
    button:
        action NullAction()
    frame:
        align (0.5, 0.5)
        xysize (300, 100)
        textbutton _("Main Menu") action MainMenu()
