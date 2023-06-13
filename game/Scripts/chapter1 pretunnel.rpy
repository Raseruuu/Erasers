label pretunnel:

    ## Meeting Breeze
    ##EXT. Cafe
    scene bg_cafe
    show white:
        alpha 0.5
    play music flairtheme fadein 2.0 volume 0.2
    pause(0.5)
    show sofi at scenter with easeinbottom
    s "Made it…"
    s "And not a moment too late… I hope?"
    show sofi at cutejump
    s "Alright, just gotta focus."
    s "Scan your surroundings."
    s "Keep an eye out for any suspicious individuals because you never know when someone could drop on you and-"
    show cc with easeinright:
        yalign 1.0 xanchor 0.5 xpos 2400

    cc "Hello Ma’am, can I take your order?"
    show sofi at test1
    s "GAAAHH!!"
    s "Sorry, you startled me for a moment…"
    show sofi:
        linear 5 xoffset -400
    cc "It’s fine, though with all that energy, it makes me wonder why you would even go to a coffee shop in the first place…"
    s "Ha ha right, I mean this is a coffee shop after all."
    s "People come here for a pick-me-up to survive the daily grind."
    s "I mean why else would a responsible young lady like myself go to a coffee shop like this if they're full of so much energy?"
    s "It’s for coffee of course, and totally not some secret organization that’s-"
    cc "Ma’am you’re holding up the line."
    cc "So please order something otherwise my boss'll kill me."
    show sofi:
        linear 0.5 xoffset -500
    s "... Oh sorry."


    scene black with irisout
    scene bg_cafe with irisout
    show white:
        alpha 0.5
    "One cup of decaf later"
    show sofi at scenter with dissolve:
        zoom 1.5 yoffset -150
    s "Maybe it was a mistake to come here in the first place."
    s "I felt so hyped about it earlier, but now that I'm actually on an assignment…"
    s "It's kinda scary."
    with hpunch
    s "I mean… I'm not built for this kind of work!"
    s "I was just someone who worked at a media company up until a few months ago! I wasn’t even an actual journalist, I was just the glorified intern! I don’t think my bosses even knew my name!"
    s "Hell, I had to take a side gig as a freelance storyteller just to pay my rent!"
    s "And now I’m doing something that could land me in prison for the rest of my life?!"
    with vpunch
    s "What was I thinking!? Maybe I should just say screw this job, get a train ticket, leave the city, never look back. Maybe I can go back to my hometown, see if I can track down my extended family, maybe they’ll have a farm I can work on?"

    ## TODO:[Sofi's backstory possibly be added here]

    s "... sigh."
    s "No, I can't think like that."
    s "You were chosen for this assignment for a reason, so you can't chicken out here!"
    s "For the fate of the world!"
    s "...no pressure."

    hide sofi
    "I whip out my phone, as I reassess the special \"note\", I got before I came here."
    n "Hi, this is Noa, from Twisted Fates Dating Service!"
    n "We set up a lovely date for you this evening at a lovely cafe at Cafe Haven, 13th Lakestreet!"
    n "Your date should be around your age, has dashing blue hair, and a sexy cold disposition."
    n "And once you see him, Tell him \"You\'re wearing nothing but a smile~\"."
    n "See you then~♡."

    s "I know this whole insurgency is supposed to keep things on the down low, but this is just embarrassing."
    s "Still codes and passphrases like this were all in the manual."
    s "So all I gotta do is find this guy, tell him the passphrase, and then we can go on our mission before-"

    show breeze at sright with dissolve
    u "Hey, I'm here with Twisted Fates. I'm your blind date."
    show sofi at sleft with dissolve:
        xzoom -1.0
    s "He… finds… me."
    "I look up from my phone to see someone that looks just like what the note described, sitting at my table."
    s "He's here."
    s "He's actually here and-"
    s "Ok, calm down."
    s "You need to remember your training."
    s "Just follow procedure, and say the passphrase to let him know you're on his side."
    s "Inhale"
    s "I'm wearing nothing but a-"

    u "Save the secret words for next time."
    u "I know you're one of us."
    s "Are… Are you sure?"
    s "Cuz the manual states that-"
    u "This ain't training newbie. I could tell who you were the moment you stepped into the shop."
    s "Y-You did?"
    u "I waited an entire hour for someone, only for that someone to literally barge in and act like the most suspicious person on the planet."
    u "What do you think?"
    s "I… well…"
    "I tried to think up any excuse for my behavior but he got me there."
    "I hunch over, feeling dejected about my shoddy performance."
    s "Guess, I really am not cut out for this, after all."
    u "Hey, lighten up. If it were any other situation. A counter-agent would've sniffed you out, and our entire organization would be compromised."
    u "But luckily nobody in this Cafe really cares about insurgencies or the government."
    u "They're either stressed-out Office workers or stressed-out College students, too stressed out to care about anything else."
    u "It's why this place makes such a good rendezvous point."
    u "Well that and for laundering money for our cause…"
    s "Now that you mention it, we are talking about such a heavy subject and nobody seems to bat an eye…"
    s "But during my training, we were always told to keep things covert."
    u "Yeah well, whatever you learned in basic training means nothing in the field."
    u "Here's a tip, newbie: \nBe more flexible in how you approach problems."
    u "Rules and training can only go so far when anything can happen out on a mission. "
    u "Be Sharp, Be Adaptive, and most importantly, Be Creative."
    u "If you follow those ideas, you'll do fine out on the field."
    s "That was… incredibly insightful of you."
    u "Good."
    u "Now let's go to the Real Rendezvous point and discuss our mission there."
    s "Real rendezvous point?"
    stop music fadeout 1.0
    ############################################################################

    ## The Real Rendezvous Point
    ## EXT. Unisex Bathroom
    scene black with pixellate
    scene white with zoomin
    play music guildtheme fadein 2.0 volume 0.2
    s "THIS IS A BATHROOM!"
    u "Yeah, it is."
    s "AND YOU THINK IT WAS A GOOD IDEA TO DRAG ME IN HERE WITH YOU!?"
    u "I don’t see any problem with that."
    u "They’re private places so, of course, no one is going to bother us."
    s "Are you even aware of what you’re saying right now?"
    s "Like a girl and a guy in a bathroom together doesn’t paint a good image."
    u "Oh, I get it."
    u "You’re a shy pooper."
    s "..."
    s "...Say that again, and I CAN, and WILL slap you."
    "Realizing that explaining the moral issues to this situation was a waste of time, I decided to look for any areas where this place could be bugged."
    "Though finding any bugs here would be concerning for entirely different reasons."
    "Meanwhile, Breeze merely shrugged before retreating to one of the corners of this small room."
    "As I continued searching, he pulled out a can of soda from his pocket before slurping it down."
    s "By the way, I never happened to get your name, buddy. Whatever shall it be?"
    b "... It’s Breeze."
    b "Is there any reason why you’re talking like that?"
    s "Breeze huh? That is a wonderful name that your parents gave to you. My name is Sofi. Do you happen to have a dollar I can borrow?"
    "For a split second, Breeze’s eyes widened, realizing what I was trying to do."
    b "Hey Sofi, didn’t I tell you to lighten up?"
    b "Whatever training you were given, it’s usually wrong."
    s "Force of habit, and it’s hard to listen to a guy that drags ladies into the restroom with you."
    b "Relax, this is a friendly territory, so no need to stress out over it."
    b "Besides, we have more important stuff to discuss."
    b "Like our Mission Briefing."
    "I look up at Breeze as he crushes the Soda in his hand."
    "From there, she suddenly pulled out a small device that was hidden inside the crushed can."
    "I knew at first sight what it was and retreated to the center of the room."
    s "Are you sure it’s safe to activate that here?"
    b "It’s fine, like I said, nobody is going to bother us."
    "Taking his word for it, I hesitantly channeled some of my magic into the device with him."
    "We both did this until the device lit up, and a holographic miniature woman began to project out of the device."
    "This projection was apparently the boss of the whole operation."
    u "Greetings agents, I hope you’re doing well this evening."
    u "Thank you very much for responding to the call."
    "Even as I’m looking at her right now. It’s hard to keep calm when the boss is actually speaking to you."
    "Fortunately this is probably just a recording, so I can still be relatively calm."
    u "Sofi, are you paying attention?"
    s "Wait… What?"
    b "The boss asked you a question, newbie."
    s "I… well…uh…"
    u "You thought this was a recording, did you not?"
    s "Uh…"
    u "No need to hide it, I can see it in your eyes."
    s "I’m So Sorry Ma’am! I didn’t mean any disrespect!"
    s "I just didn’t think I would ever meet you!"
    u "Relax, Relax, you are not in trouble."
    u "I have not said anything yet."
    s "...What?"
    u "If you were worried about spacing out, I was just trying to make it look like you weren’t listening."
    u "It’s a little joke I like to do around new recruits."
    b "It’s not a very funny joke, in my opinion."
    u "Aw, and I thought it was a very funny joke."
    b "Well it’s a waste of time, so let’s just cut to the chase."
    s "... For once, I agree."
    u "...You guys are no fun."
    u "Very well, we will skip the rest of the pleasantries."
    b "So what’s the agenda for today?"
    u "A few days ago, a video was beginning to circulate around social media."
    u "It was your typical video about a few people exploring some abandoned facilities they were not supposed to, but when some of our intel watched it, it was cause for concern."
    u "During one expedition, the man that was filming was apparently attacked by something inhuman."
    s "Could it be some kind of animal attack?"
    u "Our analysts thought the same, and under normal circumstances we would assume as much. However, every time this video was uploaded, it was immediately scrubbed off the site."
    u "What is even stranger was that the data surrounding the video’s existence was completely erased."
    u "Almost as if someone is trying to make it look like the video did not even exist in the first place."
    u "This could only mean one thing if our hunch is clear."
    u "Right, Breeze?"
    b "It means that the video shows something that someone very powerful does not want to spread."
    b "However, they’re going overkill. In their attempts to hide it, it just makes it more likely people will keep asking about it. Amateur work, honestly. ."

    ##* ## (The fk is this)

    s "A Vibrant!? You mean those monsters created from magic corruption?"
    u "It might be a possibility, and the administration is trying to cover up the fact that there is an outbreak right here in our city."
    b "Do you have any idea where that video was filmed?"
    u "Our people did a thorough investigation from analyzing the video, and we believe we have triangulated a general location based on reports from our undercover assets in the city."
    u "From there, we narrowed down places where a potential nest could be, and that leads us… here. An old service tunnel that is been disused since the city came under new management."
    u "Your devices will have received directions on where to go. \"Your mission is to conduct a reconnaissance operation. Go to the destination marked on your devices, determine if it's a single vibrant, a nest, or something more sinister. If luck is on our side, it will have only been an elaborate ruse from a man desperate for attention of the faceless masses."
    s "Ma’am, if I may ask a question?"
    u "You may ask your question, agent."
    s "I was just thinking that… if it is a Vibrant, why would someone be trying so hard to cover it up?"
    u "You have good instincts. Our analysts pondered the same question. From what we could gather…"
    u "It does not look like any of the Vibrants we have seen."
    b "Ah, so they think it’s New type then? And that, for whatever reason, someone doesn’t want it to be revealed?"
    u "That is what our analysts believe, there is no record of a vibrant like that in our database. Therefore, we can only surmise that it must either be some sort of new type or that someone is trying to deceive the world into thinking that it is. Because of this, if it is a new type, we cannot be sure of what sort of capabilities it possesses. Exercise extreme caution."
    u "Good luck, Agents."
    u "And Breeze, if I may…"
    b "What’s up, Kizu-nee?"
    u "....This is strictly a reconnaissance mission."
    u "Do not do anything unnecessary. I do not care for reckless agents who get themselves killed."
    u "I hope to see you soon, safe and sound."
    "And just like that, the transmission ended and the device used to communicate with her suddenly broke into pieces."
    "The communication devices were designed that way to hide any evidence and prevent any outside forces from tapping into our frequencies during calls."
    "But even knowing that, didn’t stop me from jumping up in surprise."
    b "You okay?"
    "I look up and see Breeze staring at me with a stern but compassionate expression."
    s "Just trying to process what just happened is all."
    s "It still all feels so surreal even after I got to meet you and the boss."
    b "Yeah well, process it faster."
    b "We got a mission to take care of."
    "And just like that, Breeze began to walk out the bathroom, as he left me to my thoughts."
    "As I looked back at him, I couldn’t help but think about my new partner in crime."
    "He’s cold, stern, and either lacks any self-awareness or merely doesn’t care what others think."
    "On the other hand, he seems reliable, wise, and isn’t afraid to speak his mind."
    "I don’t know why, but it feels like I can trust him, despite his quirks."
    b "Hey, you coming or what?"
    s "Oh, sorry!"
    "And so, realizing that he was leaving without me, I began to run out of the cafe with him."
    "I wasn’t sure what was going to happen once we got to our destination, but I only hoped we could both make it out alive."
    "Because, despite our rocky introductions, I kinda want to understand this guy a little more."

    return
