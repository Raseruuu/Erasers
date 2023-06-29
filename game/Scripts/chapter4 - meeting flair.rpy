label meetingflair:
    # Open with a black screen and an alarm sound
    scene black with fade
    play sound "audio/alarm.mp3" volume 0.3
    fl "CONTAINMENT BREACH IN SECTORS 6 - 13!"
    fl "EMERGENCY LOCKDOWN PROTOCOLS ARE NOW IN EFFECT!"

    #Hold on the black screen
    # scene hallway with fade
    # Open with a hallway bg, I think we have an extra somewhere that was in the original sketch work
    # Have Breeze and Azma walking down the hall, I don’t know if we’re still using the goon sprite to represent Breeze though

    az "I don’t care about protocols, I need this lockdown lifted now so I can go to the relevant sectors to deal with these fires."
    az "Do you want this situation taken care of or not? The facility is under attack by hostile forces and we have test subjects wreaking havoc. This situation is very close to being unfixable, and you can’t override this door because of protocol?"
    az "Oh, you’re worried about your job? Okay, okay, that’s understandable." 
    az "Counter offer."
    az "You’re gonna sack up, override the door controls, and you’re gonna do it in the next 5 minutes. And if your supervisor tells you otherwise; tell him that I, as head of security, am overruling him because right now... he’s being a problem." 
    az "And my job is to handle problems, do you get what I mean."
    az "...Stop and listen to what I’m saying. If I have to break down this door, I’m gonna swing by Operations, and give you, your supervisor, and anyone else who so much as looks at me funny the good news. Cause you see, you won’t have to worry about your job anymore if I have to come down there." 
    az "You won’t have to worry about ANY job ever again."
    az "Are we clear now?"
    az "Good. You now have 4 minutes to get this done. And stop crying already, you’re an adult for god’s sake."

    play sound "audio/beep.mp3"

    # Azma annoyed groan
    az "The things I have to put up with..."

    s "...he hasn’t changed."
    s "This man... after all these times, he’s still the bastard he’s always been."
    s "I promised the rookie that I wouldn’t blow my cover but... seeing him here, his guard down... could I take him out now?"
    play sound "audio/icesword.mp3" volume 0.5
    # ice sword forming noise, but softer, quieter
    s "We’re in the middle of an attack, he doesn’t know it’s me, maybe in that brief moment I can strike him down. Create a dagger of ice that can be easily hidden. Then a quick strike to a vital organ, it’d be done and over with in 5 seconds. They’d probably find his body and assume that either the intruders or a vibrant got him."
    s "....."
    s "No. He’d be able to survive that. This man has survived far worse than a stab wound. I’d only have one shot, and right now it’s too much of a risk."
    play sound "audio/icesword.mp3" volume 0.5
    # Sound of ice sword deforming, I guess it’s like a defrosting sound or just the same sound as the forming
    s "She was right; now’s not the time for this. My chance will appear, but it’s not now."
    az "Did you hear me, guard?"
    b "Huh? Sorry, I was just a bit nervous about the intruders."
    az "What for? It’s just another fight. Just kill them before they kill you."
    b "....."
    az "It’s not a difficult concept to grasp, guard."
    b "Most people are usually apprehensive about being in a situation where they can die."
    az "...."
    az "Have you never killed anyone before?"
    az "They say that after your first kill, it gets easier. But there must be something wrong with me, because I’ve never felt anything from it. Not once. Perhaps I’ve just rationalized it as something that can’t be helped. I mean, I don’t wanna die, so... only option is to kill them before they kill me, right?"
    az "You hit me first, so I’ll kill you before you kill me."
    az "You failed your job and forced me to have to clean up after you, so I’ll kill you before you kill me."
    az "I don’t like the way you look at me, so I’ll kill you before you kill me."

    # Azma shrug noise

    b "And how many people have you killed, sir?"
    az "......"

    # Azma thinking, then evil smile

    az "...Enough."
    s "...I’m going to kill him. I swear it."
    az "Speaking of which, that’s five."

    #Azma sigh
    az "Make me have to do everything myself. Guess they’re tired of living, soooo..."

    # Azma preparing to punch, I don’t know how to display that, maybe show him with glowing eyes or something
    b "Wait, maybe they just can’t override the door lock?"
    az "Oh? Explain, guard."
    b "Well, from what I could gather, these intruders did some damage to the facility. That’s what the containment breaches are about right? "
    b "So, with that in mind, maybe the systems to control the door are also affected?"
    az "Hmmmmm, perhaps. Well, maybe I should break it anyways."
    b "I could also run down to Operations, see what the deal is. It’s not like I can do much here anyways."

    s "A quick lie, laced with elements of the truth. He’s an evil bastard, but he’s not an idiot. So this should work to at least get me away from him so I can regroup with the rookie."
    b "I mean, let’s be honest, I don’t stand a chance if we run into a problem. Worst case scenario, I just get in your way. So, running down to Ops to get a situation report is the least I can do."
    az "...."
    az "What was your name again, guard?"
    b "Uhhh... Herbert, sir."
    az "Ah, yes, Herbert. Right."
    az "Your plan is acceptable, you may go."
    b "Thank you... sir."

    # Turn Breeze’s sprite and begin sliding off-screen, don’t slide all the way though, keep the pace slow

    az "....."
    az "Oh and Herbert, what should I tell your wife? if you don’t make it, that."

    # Stop Breeze’s sprite, think about it... play breeze thinking sfx

    b "Tell her: I’m sorry, but I’ll have to take a rain check on date night."
    az "Right.. oh, Herbert. One more thing..."
    play sound "audio/punch.mp3"
    play sound "audio/icesword.mp3"
    # play Azma strike SFX + Breeze Ice SFX, the intention here is that Breeze blocked a ranged attack from Azma with an ice-wall

    # Hold on the scene
    with Pause (3.0)
    az "I see you managed to survive... Breeze."

    # Breeze undoes the goon disguise since he’s been made / TN: "To be made is spy talk for cover being blown, being discovered, essentially"
    hide grunt1 with fade 
    show breeze with fade

    b "What gave it away?"

    # Hold......

    # Then Azma shrugs

    b "...Y-you didn’t know for sure? What would’ve happened if you were wrong?"
    az "What do you think? He would’ve been a red smear on the wall."

    # tilt Breeze sprite, like the response was so callous that he takes physical pain from it

    b "...still the same violent psycho as ever, I see."
    az "Well, what can I say?"
    az "It’s just my nature."

    # Hold on the scene as the two sprites step further apart

    s "I should’ve escaped soon or struck first, this setup was not in my favor at all;. It’s too cramped, he’s fully alert, and reinforcements could come at any minute."
    s "I don’t have a snowball’s chance in hell of beating him in these conditions, I just need to survive then find an opening to make a break for it."
    s "Speaking of hell, was it getting hotter in here?"
    s "Taking a moment to realize that the room really was getting hotter, I notice in the corner of my eye, the wall glowing when suddenly-"
    play sound "audio/explosion.mp3"
    # play breeze ice sfx
    queue sound "audio/icesword.mp3"
    # Hold on the scene, then play footsteps
    queue sound "audio/footsteps.mp3"
    s "That was too close."
    s "If I hadn’t noticed the rising heat, then I might’ve been burned to a crisp."
    s "Next to where I’d been standing was now a hole burn straight through the wall. A fire-haired woman stepped through the hole, carrying with her an air of confidence and power."
    show flair at halfright
    un "Pardon the intrusion, but you didn’t have a doorbell."
    s "Ah, this person was likely the intruder that’s been causing trouble. A fire mage huh, not a good match up against me and-"
    play sound "audio/ding.mp3"
    # turn Flair sprite towards Breeze if it isn’t already
    # Play a ringing sound, probably the same sound used during the tunnel investigation

    s "This girl..." 
    s "Why did I feel like this wasn’t the first time we’ve met?"
    s "Something from my past? No. No, I've never seen this girl in my life but... I know her, from somewhere?"
    s "Flair... Her name is Flair. Why did I know that?"

    # Turn Flair to Azma

    f "Hey, you, big guy. You the boss here? I have some questions that need answers."
    az "Who the hell are you?"
    f "You’re holding someone captive, I’m here to get them out."

    # Hold on the scene, tilt Azma sprite slightly to symbolize his disbelief at the reasoning

    az ".....are you messing with me?"
    az "You just... strolled into a facility, burned through several layers of defenses... to pick up one person?"
    az "Heh...ha...hahahahahaha. Okay then, I’ll humor you. Who, exactly, are you looking for?"

    # f "[Tomo’s full name here or a nickname, something familiar]"

    az "... I have no idea who you’re-"
    az "Wait..."
    az "Dr Tomo? You’re here for that Tomo?"
    az "Oh, you stupid girl..."
    s "Azma can’t help but laugh as he turns on his heel, as if he and he alone were aware of some massive joke. However, it didn’t look like he was gonna share with the rest of us."
    f "Hey, I’m not done with you!"
    s "Like a beast of flame seeking its prey, a torrent of fire shot out from Flare, threatening to burn Azma to a crisp. And, had it been anyone else, it might’ve worked."
    s "However..."
    s "All he did was backhand the fire with barely any effort, and as if it had hit some kinda invisible barrier, it sputtered out until it was nothing but a whiff of hot air."
    az "...Pathetic."

    # Sealed door opening sound... this might be difficult to find though, so as a substitute, the beeping sound that some vehicles make when backing up can be used
    play sound "audio/doorbeep.mp3"
    az "Oh, now it’s open. Just when things were getting interesting."

    "Suddenly, Azma pointed directly at me."

    az "Kill her for me, will you? I’ve got something else to take care of."

    # Azma walking off screen
    show azmaveth with move:
        xpos 1.5
    b "What, hey, I’m not-"

    # Show Breeze sprite beginning to follow but is stopped by a wall of fire, which he immediately backs up from, then turn sprite to Flair

    b "Are we really gonna do this now?"
    f "Well your boss just told you to get rid of me, so I decided to take the initiative."
    b "Initati- I’m not working for him!"
    f "Oh yeah, sure, you just happen to be a totally unrelated person in the middle of a secret underground facility- do you think I’m stupid?"
    b "....I’m not gonna answer that."
    b "I will say though, I’m not your enemy, but..."

    play sound "audio/icesword.mp3"
    b "I’m not about to lay down and die either. So, if you won’t listen to reason, then you’re not giving me much of a choice."

    # Flair fire sfx
    f "Better men than you have tried."

    # Show the two sprites rushing at each other as it fades to black
    scene black with Dissolve(1.5)
    jump chapter5
    return