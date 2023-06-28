label facility:
    scene magicfacility with Dissolve(2.0)
    show ms at left:
        yrotate 180
    show grunt1:
        xpos 1.5
    show grunt2:
        xpos 1.5
    # Have the goon sprites "walking" across the screen, maybe lookin’ kinda shady
    # have another goon sprite just suddenly pop up from the ground, since all the goon sprites look alike, we don’t need to make a new one. Btw just to mention it, the two goons are Sofi and Breeze in disguise
    show grunt1 at center with move
    show grunt2 at right with move
    ms "Where the hell have you two idiots been?!"

    # Straighten up the goon sprites, basically just put a shake effect on them briefly
    ms "Your shift starts in two minutes, do I need to remind you about proper time management again?"
    g1 "Uhhhh, no sir, sorry sir, we were just… ummm… uhhh…"
    g2 "A sensor was tripped topside, so we went to confirm that we don’t have another intruder."
    ms "Oh."
    ms "I see."
    with Pause (2.0)
    # Beat, as if he doesn’t believe them, there’s some tense music that should start playing
    # hold on the scene
    play sound "audio/ding.mp3"
    ms "Finally taking initiative I see, well done."
    ms "I’ll overlook your tardiness this time, just don’t let it happen again."

    # Maybe we should have a one-time define line that’s just both of them talking, unless there’s a way to have both their lines play at the same time
    g1 "Yes sir! Sorry sir!"
    g2 "Yes sir."
    ms "Good, now get to your posts."
    ms "Seriously. Go. Now."

    show ms at offscreenright with move

    # Hold on the goons 1 and 2 sprites, have one turn to look at the other
    # If possible, spin the sprites and then replace with the breeze and sofi sprites. If not possible, just do a fade in or something
    hide grunt1 with fade
    show breeze at left
    hide grunt2 with fade
    show sofi at center
    b "Wow, I can’t believe that worked."
    s "Yeah, on the way here, I familiarized myself with the stored spells loaded onto our devices. Check it out."

    # replace Sofi’s sprite with the goon, it doesn’t matter who, but it’s g2 as the default
    hide sofi with fade
    show grunt2 at center with fade
    g2 "Ooh look at me, I’m goon-2! I’m a total brown noser, nyeh!"
    b "...He doesn’t say, nyeh."
    g2 "I do now, nyeh!"

    # Breeze, cringe groan
    # breeze sigh

    b "They didn’t have this stuff when I started, so... I guess it makes things easier?"
    # put Sofi sprite back
    hide grunt2 with fade
    show sofi at thirdright with fade
    s "Yeah, it’s cool! It’s kinda like what vtubers used back in the day, but in real space. It just needed to scan his form, keep the device on my person, and it’ll compensate for the rest to overlay a model of him over me." 
    s "I just gotta not do any sudden explosive movements and no one should be able to tell the difference."
    b "We’ll thank the crafters when we get back, anyways... take a look at this."

    # I don’t know if we have a bg for the facility. We might be able to recycle a previous or cut bg, otherwise we’ll just use theater of the mind or something, make use of sound effects of like… a busy construction site or something
    b "Guess they were telling the truth after all."
    s "Yeah they definitely seem to be in a big hurry to pack things up."
    s "I'll grab a picture for HQ!"
    # show Sofi phone as a cut-in, basically a small tab that slides in from the side with the phone asset in the tab
    play sound "camera.mp3"
    s "Huh, looks like they’re using old world tech? What for?"
    b "Maybe it helps cloak their activities in some way. It’s probably not efficient but they might be sacrificing the convenience of newer tech if it helps keep them hidden."
    b "The MRF is very paranoid after all, that’s why they have dozens upon dozens of shell corporations to interact with local government agencies and groups of interest. It’s all about controlling things from in the shadows."
    s "Why are they doing this? What are they trying to accomplish?"
    b "In contrast to the Erasers goal to prevent a second apocalypse by protecting magic from those who would abuse it, the MRF goes the opposite direction."
    b "They want magic to be more integrated with society and have it surround us."
    b "Officially, their various mouthpieces say that progress cannot be stopped, and we must change with the times. But that’s a lie."
    b "They only want magic to proliferate so they can control people."
    b "They want to be involved in every magical decision, they want to make people beholden to them for their expertise, and most of all… they believe that they alone have the right to rule."
    b "Why take over a country through military might when you can hold the pursestrings of its leaders?"
    s "But why though? What do they gain out of it? Money? Power?"
    b "...."
    b "That, rookie, is the million dollar question. Look there."

    show rat2 at right with fade
    s "Oh… crap. It doesn’t look exactly like the one in the video, but that’s definitely a new strain."
    play sound "camera.mp3"
    hide rat2 with fade
    b "..they called it Project Siren, what could that mean?"
    s "In the old world’s mythologies, sirens were said to lure sailors to their doom with a bewitching song. In order to keep them from steering their ships into jagged rocks, sailors would stuff their ears so they can’t hear anything."
    s "Maybe i t has something to do with that?"
    b "Hmmm…"
    s "In anycase, I think we have more than enough evidence. We know the MRF are here, they have a secret facility, they’re trying to leave, and they’re likely experimenting with vibrants here. We even have a photo of that."
    s "Protocol dictates that we should fall back immediately to a safe location."
    s "Then we have to send this data back to HQ, and wait for further instructions."
    b "Alright. Sounds good to me."
    "The moment I heard those words, I knew something was off..."
    s "This is the first time you actually agreed to a written protocol…"
    s "... You’re going to add a \"but\" to that statement, aren’t you?"
    b "No…"
    b "..."
    b "Buuuutt…"
    s "There it is."
    b "This is a serious suggestion, though. Remember what Goon 2 said earlier?"
    s "That they were moving their stuff, right?"
    b "Exactly, which means that they won't be around here muchlonger."
    b "By the time reinforcements arrive, they will probably realize they've been compromised and destroy this place to wipe their tracks."
    s "That’s… a good point actually. "
    b "So, I say we take care of this now, rather than later!"
    s "But this is supposed to be a reconnaissance mission! The boss told us not to be reckless, remember?"
    b "That's what she says in all my missions.he hasn't kicked me out yet."
    b "So are you in or out? It's your call, rookie."
    s "... Fine, but if this goes south I blame you!"
    b "Fine by me!"
    s "But first we need to come up with an actual strategy. "
    s "These disguises aren't perfect and if someone here is smart enough to see through our shoddy facades, we're dead!"
    s "And with so many people still running around here, I say it's next to impossible to sneak around."
    s "Maybe if we had a distraction of some kind, it would be a different story but I don’t see how-"
    play sound "audio/explosion.mp3"
    "BOOM!!!"
    with hpunch
    with vpunch 
    "Out of nowhere, an explosion seemingly went off as the alarms in the facility started blaring."
    play sound "audio/alarm.mp3" volume 0.5
    "The floor rumbled, causing me to lose my footing, I would’ve met the ground had Breeze’s quick reflexes not caught me in time."

    # We should have a VA actually say this line
    fl "ALERT. SECURITY BREACH IN SECTOR 3."
    fl "REPEAT. SECURITY BREACH IN SECTOR 3."
    fl "NON-COMBATANTS ARE TO EVACUATE TO THE NEAREST SHELTER AS SOON AS POSSIBLE TO AWAIT FURTHER INSTRUCTIONS."
    fl "ALL COMBATANTS ARE TO CONTAIN THE BREACH IMMEDIATELY. "
    b "Cast your disguise spell, quick!"
    hide breeze with fade
    show grunt1:
        xpos -0.05 yrotate 180
    hide sofi with fade
    show grunt2 at center:
        xpos 0.25 yrotate 180
    s "As soon as we heard the alert come on over the intercom, we're-engaged our disguises. Looks like we wouldn’t be be able to just casually walk around anymore."
    s "Did they find us out? I wasn’t sure until I saw a couple of guards literally run past us."
    b "Might be another Vibrant breakout?"
    b "Talk about a lucky break."
    s "Weird coincidence, but this is definitely a golden opportunity."
    s "Let’s move!"
    "Seizing this fortunate chance, we immediately began to bolt to the opposite direction the guards were going to shut down their operation."
    "But the thing about luck is that it’s a fickle mistress."
    "Just as we thought we were home-free, we get flagged down by someone I could only describe as… a wall of rippling muscle."

    show azmaveth at right
    un "Hey, you! Where are you two going!?"
    "Seeing as we were caught red-handed, I quickly tried to come up with an excuse to tell him."
    s "Sorry sir, we just got back from our patrol! We were just-!"
    un "Okay look, I don’t actually care. Whatever you were doing, drop it, I need you to-."
    show azmaveth:
        yrotate 180

    un "...Where the-"
    # pained sigh from Azma
    show azmaveth:
        yrotate 0
    un "Wait here."

    show azmaveth with move:
        yrotate 180 xpos 1.5
    "We should probably get out of here before he gets back, that’s what I was thinking. After all, there’s no reason for us to play guards, and whatever that breach was about, I don’t wanna be around to meet the cause."
    s "Hey, I think we should-"

    # Show Sofi shake
    "Breeze looked off. That look in his eyes, his body language, it triggered as soon as that man came into view. Did these two have some history?"
    "It was almost frightening to see the level-headed weirdo get so worked up all of a sudden."
    s "Breeeeeeeeze?"
    s "You okay there?"

    "...I get it. No, really I do."
    "He’s angry about something, that’s plain to see. I was in that state myself in the past, it’s kinda what lead me here."
    "Under any other circumstances, I’d probably be more comforting. However… this was an ideal location to let anger guide our actions."
    s "Breeze…"
    s "I don’t know what your story is with this guy, but I can tell it’s bothering you. Maybe even enough to get you to act in a… less than ideal manner."
    s "I get that. I really do."
    s "But, we can’t afford to blow our cover right now. We’re deep in enemy territory, cut off from our allies, and we have vital intel."
    s "If we get into a fight here, there’s a good chance at least one of us won’t make it out. And that violates the first rule, doesn’t it?"
    s "So… please, I need you to go back to your normal self; the calm, rational guy who ignores the manual, who does his own thing, but doesn’t put his partner in unnecessary danger. Okay?"
    b "...."

    # Breeze inhale then exhale
    b "...Fine.."
    s "Thank you. Remember, keep your cool, and we’ll get through this. Right? That’s what you told me, right?"
    b "...Not in those exact words."
    s "Well, I got most of it at least. How’s my pep talk?"
    b "...6 out of 10."
    s "You jerk."
    show azmaveth:
        yrotate 0
    show tomo at offscreenright
    play sound "audio/footsteps.mp3"
    show azmaveth at extremeright with move
    un "Why do you keep trying to go off on your own, and make my life harder, Dr Tomo?"
    show tomo at right with move
    # Show Tomo sprite coming after that line
    tm "Mr Azma, I swear, I wasn’t trying to-"
    az "Shhh."
    az "No more talking. I don’t have time to babysit you, so here’s what’s gonna happen."
    az "This guy here, he’s gonna escort you to one of the safe rooms. You’re gonna follow him. You’re not gonna make any detours. Straight. To. The. Safe. Room. It’s right down this hall, then take a left, and just keep following the blinking lights."
    az "Are we clear?"
    tm "....yes… sir."
    az "Good. Now be a good girl, and get out of my sight, and don’t cause me anymore problems today, or I’m going to very upset. Got it."
    tm "...Y-yes."
    az "Good."

    # Turn to Breeze and Sofi
    az "You get all that?"
    s "Yes sir, got it all. We’ll just be on our way-"
    az "Not both of you."
    az "You. You’re with me, we’re gonna go contain this breach."
    b "...."
    az "...Got a problem with that, soldier?"
    b "...No, sir. There are no such problems."
    az "......"

    # There seems to be building tension, then play a communicator beeping sound
    pause 3
    play sound "audio/beep.mp3" volume 1.5
    # Turn Azma’s sprite around
    show azmaveth:
        yrotate 180
    az "Boss is calling. Let’s go, we’ll head to the rendezvous while I take this call."
    show azmaveth with move:
        xpos 1.5
    # Az walking off screen
    az "What is it, Kephirah?"
    # begin to move Breeze’s sprite, but then have him turn to Sofi’s sprite
    # tilt his sprite slightly as if nodding, then turn back and slide him out of frame
    # bring Tomo’s sprite to Sofi’s
    s "So… your name was Dr Tomo?"
    tm "..."
    s "...."
    tm "...."
    s "...."
    "Okay, this was just getting awkward."
    s "Soooo, should we get moving now or-"

    # Show Tomo moving off-screen
    show tomo with move:
        yrotate 180
    s "Wait, where are you going? I don’t think that’s the way to the safe zone."
    tm "We’re not going there."
    s "But, the big g- Azma, said-"
    tm "I know what he said."
    tm "But I have something I need to do so… if your job is to protect me then you can do that by following me. Or don’t. Either way, I’m going."

    # slightly tilt Sofi’s sprite like she "can’t fuckin’ believe this bitch’s attitude"
    "And just like that, Tomo began to walk away leaving me to stand around flabbergasted at her attitude."

    # Show Sofi shake
    "Recovering from my stupor, I promptly went after her. Couldn’t exactly just let her get eaten by a Vibrant."

    jump meetingflair
    return
