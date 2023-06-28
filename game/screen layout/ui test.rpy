screen menutest:
    tag menu
    zorder 5
    button:
        action Hide("menutest", transition=Dissolve(0.2))
    hbox:  ##tab buttons
        xalign 0.5
        spacing 0
        for i in menutablist:
            use menutab(i)
    fixed: ##main bg
        xysize (1500, 850)
        pos (210, 120)
        add Frame("gui/newui/wenrexa/Window04.png")
        if persistent.menupage == "Save":
            text _("Save Gamezzzzzz")
            use file_slots(_("Save"))
        if persistent.menupage == "Load":
            text _("Load Game")
            use file_slots(_("Load"))
        if persistent.menupage == "Preference":
            # text _("Preference")
            use preferences()

screen menutab(i):
    zorder 5
    fixed:
        xysize (280, 100)
        yanchor 1.0 ypos 140
        imagebutton:
        # xysize (375, 100)
            hover Frame("gui/newui/wenrexa/Btn_V16.png")
            idle Frame("gui/newui/wenrexa/Btn_V15.png")
            action SetField(persistent, "menupage", i)
        text i align (0.5, 0.5) color "#FFF"


label testingui:
    scene bgcafesepia
    show g2
    g2 "Hi"
    show g1
    g1 "yo"
    show azmaveth
    a "Hi"
    pause
    pause
    return
