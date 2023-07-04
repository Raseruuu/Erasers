label chapter5:
    scene ElevatorOutside
    play music complextheme fadein 1.0
    fl "CONTAINMENT BREACH IN SECTOR 16 through 27!"
    fl "EXODUS PROTOCOL IS IN EFFECT!"

    # Show Alverna’s sprite lower than Sofi’s to give the impression that she is crouching down, Sofi’s sprite is probably still using the goon sprite
    ## show alverna at center
    show g2 at left
    s "What’s Exodus Protocol?"
    tm "Shouldn’t you know that? Aren’t you a guard?"

    # Shake sofi sprite
    s "Yyyyyeah, buuuuut it’s my first day?"
    tm "...Riiiight. Anyways… Exodus Protocol. It means they’re beginning evacuation procedures. They’ll likely take the research done here and move it to a sister location while this space will probably be purged."
    s "O-Oh… I see."
    s "Th-Then maybe we should get to the evacuation zone?"
    tm "Not an option yet. There’s something important I need to retrieve in the lab."
    s "But, it’s dangerous here, so maybe we should-"
    tm "Look. Your job is to protect me, right?"
    s "I… guess?"
    tm "Well there’s something I need to take care of in the lower levels, so if you’re going to protect me then you need to-"
    play sound "audio/heart.mp3"
    # Heart beat sound and Alverna shake, tilt her sprite so it’s at a 45 degree angle, kinda like she’s doubled over in pain

    s "Dr Alverna, are you alright?"
    # Pained Alverna noises
    # Alverna shake
    tm "Just… shut up, I just need…."
    play sound "audio/heart.mp3"
    # Play sound of something dropping if one can be found or made, otherwise we don’t have to have this
    # Show image of the injection device, probably sliding in from the side or just uh… what’s that thing called when an object zooms out from nothing on the screen? I can also likely make the asset
    # Alverna pained voice
    "She procures a long syringe from inside her coat pocket and fumbles with it's safety lock."
    tm "No dammit, just… not now…."

    # Show Sofi conflicted
    "...the manual dictates that I shouldn’t break character, shouldn’t help an adversary without purpose, I know that. I read that manual back and forth a hundred times, I can quote sections from memory. I know that."
    "But..."

    #Sofi sigh noise
    # Slide Sofi closer to Alverna sprite, have the "sofi" sprite pan down under the screen while tilted as if she’s crouching down. We should still be able to see a good portion of her upper body, at most up to her shoulders

    s "This is an Icarus Industries auto-injection device, yeah?"
    tm "...Yes, how… do you know?"
    s "....."
    s "I’m familiar with them."
    s "Let me see your arm?"

    # Show Alverna sprite shake + turn away (the turn away might look awkward given the angle she’s at so it can be skipped if it looks weird)
    tm "No!"
    "As soon as my hands were close to hers, she wrenched them away as if I was something to be feared, like just the act of physical contact was painful."
    s "Listen, I have some medical training, and I know how to use this thing."
    s "I’m guessing your grip strength is probably weak right now, let me help you, please."
    tm "...."
    s "I promise I won’t tell anyone that you’re sick, okay? I’m just trying to help. But I need you to meet me halfway, okay?"
    tm "....."

    # show Alverna sprite turning back to Sofi, tilt the sprite

    s "Thank you. I’m going to lift your sleeve so I can administer the medicine, okay?"
    tm "...."

    # Show Alverna tilt slightly as if nodding
    # Show asset of Alverna’s arm in a cut-in, I’ll draw that, I’m not a character artist, but I can draw a simple goddamn forearm

    s "Okay, I’m going to…"

    # Hold on the scene
    play sound "audio/alert.mp3"
    # play the "ace attorney clue" sound that was used in some prior scenes
    # There should be some mark on Alverna’s arm but I don’t know if I should draw attention to it, probably not and hope people remember from the founding myth

    tm "...?"
    tm "Something wrong, guard?"
    s "Uhhh, no, sorry, just… um… was trying to find a good spot to inject."

    # Injection noise here, if someone has a can of compressed air, using the sound that makes when it’s engaged should suffice
    # Show "sofi" sprite standing at full height

    s "There, that should do it. Lemme help you up."

    # Alverna standing to proper height

    tm "....."
    tm "...Th-thanks.."
    s "It… was nothing."
    "...I’m sure I must be mistaken, that mark… it couldn’t be. Right?"
    tm "Where does a guard learn to use an autoinjector? That’s not part of your training, is it?"
    s "Well… the thing is-"

    # play fuse sound, kinda like someone lit one of those old timey bombs
    s "Get down!"

    # Show barrier image and Alverna sprite being moved slightly behind Sofi
    play sound "audio/explosion.mp3"
    with hpunch
    with vpunch
    # play explosion sound from Alverna’s fire
    # show Breeze sprite sliding out from the side
    # show breeze dodging at least two shots of fire, then shoot back some ice
    stop music fadeout 0.5
    play music breezeintro fadein 1.0
    queue music breezeloop
    s "What the-"
    s "Breeze?!"
    s "What happened to your cover!"
    b "Now is not a good time!"

    # Show Flair sprite and a swinging sfx, Breeze sprites moves past her, her sprite should be tracking Breeze’s sprite until she notices Alverna

    tm "Wh-What is it? Is it an enemy or- wait…."

    # Show Alverna sprite peeking out from behind "sofi"
    # Turn flair to Sofi and Alverna
    f "Alverna!"
    # Show enraged Flair
    f "Get your hands off her!"

    # Play charging up sfx if it exists, then rush forward

    s "Wait wait wait wait this isn’t what it looks li-"
    b "Sofi, barrier!"

    # Sofi undoes the disguise, Flair tries to stop her attack, engage Sofi barrier
    # bright flash and ringing
    # fade in, Sofi tilting towards the ground, bring her sprite back upright. Alverna turned away. Breeze right behind Flair with an ice sword, Flair standing still
    ". . . .  . . "
    s "Okay… everyone… just calm down, look… I’m gonna put my weapon down. Alright? Breeze, can you do the same."
    b "...."
    s "Breeze, please?"
    b "..."

    # disengage ice
    f "......"
    "Despite my attempts to defuse the situation, the woman still seemed uneasy. Much like a landmine, any amount of pressure seemed likely to set her off."
    "What did the manual say about negotiations? Analyze the situation. She came at me when she saw Alverna, they know each other? Could I use that?"
    s "D-Do you two… know each other?"
    f "......"
    tm "...Y-yeah, I know her. This is Flair, we grew up in the same household."
    tm "Although, I have no idea what she’s doing here."
    b "Apparently, she and her friends are the cause of-"
    # interrupt Breeze’s line or have this play at the same time
    fl "CONTAINMENT BREACH IN SECTIONS 34-39!"
    b "That, basically."
    f "What friends?"
    b "Didn’t… you come in here with an army or something?"
    f "Nnnnnnnnooooo? Is that alert not about not her?"
    s "Definitely not."
    f "Wait, don’t you work for that big guy?"
    b "I’d sooner take orders from the rookie."
    s "Okay, rude."
    f "But… he said…"
    b "He was obviously lying, you unhinged pyromaniac!"
    f "Bite me, you walking snow cone"
    # fire and ice sfx
    play sound "audio/icesword.mp3"
    ## queue sound "audio/flames.mp3"
    s "Okay, stop stop stop, before you get into another fight! Look, can both of you just calm down and listen for a moment?"
    "......"

    # fire and ice dispelled, turn breeze and flair sprites away from each other
    s "Okay, so… there’s clearly some misunderstandings here, so why don’t we-"
    "But before any more words could be said, the tension was abruptly interrupted by a blood-curdling sound"
    "ROOOOAAAAARRRRR!!!"
    with vpunch
    play music vibranttheme
    "We all turn to the direction of the noise, and at the end of the hall was something truly horrendous."

    # switch to the other corridor BG and slide in the vibrants
    # playing sniffing sound
    play sound "audio/sniff.mp3"
    "I’d seen them before, in photos, videos, and from a distance but this time there was no screen to keep us apart, these things weren’t photos in an article, nor was there a barrier between them and I. At the end of the hall, a swarm of vibrants started to crawl in, some practically tripping over each other as they sniffed the air."
    "As if… they were looking for something."

    # Stop sniffing noise
    # scene ElevatorOutside
    # swap back to the elevator bg, have Alverna behind Sofi’s sprite again
    # I don’t know if they have a ranged attack, if so, have a vibrant fire one at Sofi, only to be blocked by Flair

    b "Rookie, focus!"

    play sound "audio/icesword.mp3"

    f "How long will that last?"
    b "Not long enough, we need a way out."

    # turn breeze to flair

    b "Truce?"
    f "...."
    b "Are… are you seriously THINKING about it? In THIS situation?"
    f "Okay, okay, okay fine! Temporary truce."
    b "Great."

    # Show Breeze sprite turning in place, as if looking around, then stop, and turn to Sofi

    b "Rookie, I need you to get this elevator open. Right now, it’s our only way out."
    s "I… I…"
    b "Hey, What’s the first rule of the guild?"
    s "Huh?"
    b "First rule, I told you it before, what is it?"
    s "Ummmm… e-everyone comes back alive?"
    b "You got it. And you got this. You’ve done well on your first assignment, so I’ll put my trust in you."
    # turn breeze to face the fibrants with flair
    s "...got it… okay… I can do this."
    "I’m scared. Of course I am, who wouldn’t be in this situation."
    "Even those two, with all their power, they aren’t gods. They’ll still die just like anyone else, they might be scared too but they know what needs to be done."
    "And so do I."

    # Play Sofi deep breath noise
    # Turn to face Alverna who is at the far end of the bg

    tm "No, no, no, leave me alone, please, don’t let them come near me! This isn’t supposed to happen, please not me, not like this-"
    s "Dr Alverna!"
    tm "!"
    s "Okay, listen… we three are going to protect you, I promise not a single vibrant will get near you. However, we need this elevator door open. They can hold back the horde, and I can help them. So all you need to focus on, is getting the door open."
    s "Can you do that for me?"
    tm "I…"
    tm "...."
    tm "O-Okay, I can do that… I just need a bit of time."
    s "Got it, we’ll buy you as much time as we can."
    "As I turned to ready myself to assist Breeze and Flair, I suddenly felt a tug on my wrist."
    "Alverna, maybe instinctively, maybe consciously… she had grabbed onto my wrist. The fear in her eyes, she was easy to read. It was like she was begging me to not leave her behind."
    tm "B-Be careful. Don’t die."
    s "I won’t. Promise."
    "Alverna took a long breath, and then turned back to the elevator’s control systems."
    # Turn sofi sprite towards breeze and flair

    s "... Okay then. First real battle. This is what you signed up for Sofi."
    # show Sofi joining breeze and flair
    s "....Breeze, did I make a mistake somewhere? The manual has several chapters that essentially say that the best way to avoid a situation like this… is to just not be in it. And yet…"
    b "Battlefields are unpredictable, so the agents who have the best chance of surviving are not usually the ones who avoid every problem, but the one who can do that AND adapt to the changing conditions."
    b "Besides, we both know this situation is the arsonist’s fault."
    f "Arsoni- are you talking about me, you jackass?"
    b "Gee, I don’t know, is there another fire girl who blasted holes through the facility and caused this chain reaction?"
    f "Okay, first of all, up yours. Secondly, my name is Flair. Not fire girl, not pyromaniac, not arsonist, it’s FLAIR!"
    s "Both of you, please! Just… like… can you direct your anger to the vibrants? They’re gonna break through that ice wall at any moment. And I’m feeling really, really, really, REALLY nervous right now because it may have just dawned at me that these things are triggering a deep primordial fear in me."
    # Show Sofi shake
    b "Alright, I hear you. Listen, just like we did earlier, all you have to do is focus on backing me up, and I’ll do my part to keep you safe. Got it?"
    s "Okay… okay… I got it, I trust you."
    s "Ms Flair, this is a strange time for an introduction, but I’m Sofi. And in case I die here, I’d like you to remember my name… because I feel like Breeze will not remember what to put on my tombstone."
    b "Gimme some credit, I’m not that bad with names."
    s "Oh yeah?"
    s "What’s my full name?"
    b "....."
    s ".....well?"
    b "........No."
    b "I sense I’ve made a mistake of some kind."
    s "Anyways, this is an usual first meeting in a stressful situation, so… forgive me if I mess something up. Humor… kinda helps me relax a little, if that makes sense?"
    f "...."
    f "Sure, I guess? Though, if you mess something up, I probably won’t be able to hold it against you for too long."
    s "Oh, okay then."
    s "...wait a minute."

    # Ice breaking sound
    play sound "audio/shatter.mp3"
    b "Alright, witty banter time is over! Here they come!"
    scene pitchblack
    $ encounter = "Rats"
    
    jump precombat

    jump chapter6
    return
