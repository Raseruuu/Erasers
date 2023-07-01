label pretunnel:
    scene black
    play sound "trainmoving.mp3" volume 0.2
    scene train
    show sofi with fade
    # Sofi has her eyes closed
    # She opens her eyes and stretches

    s "Wha- huh?"

    # show sofi surprised

    s "Oh, crap! Did I miss my stop, what time is it?"
    show sofi:
        xpos 0.52
    show sofi with move:
        xpos 0.48
    show sofi at center with move
    s "Oh there's my phone!"

    # show sofi, sigh of relief

    s "Phew..."
    s "Okay, still on time... still... on time."
    s "......"

    # Sofi wearily sighs, like she’s regretting her life choices

    s "Sofi you stupid idiot, are you really gonna go through with this?"
    s "Is this what I should be doing? I mean, what am I trying to accomplish here?"
    s "I was mad back then, angrier than I’ve ever been. I was in a really vulnerable place, and I just... I didn’t want to just sit there and accept it. No. I wanted to strike back, even if it cost me everything, I wanted to..."
    s "...send a message."
    s "...and I’m about to do something {b}crazy{/b}. Like, most people who get mad just post about it or make a video essay, and my dumb ass here is about to throw everything away just because-"
    s "......"
    s "I’m still mad though. I don’t think I’ll ever not be mad. But, is this the path I should take?"
    s "There’s no going back once I do."

    scene stationmap with Dissolve(1.0)
    s "....."
    s "I could quit."
    s "My stop’s coming up, I can just... not get off the train. I haven’t crossed that line yet, there’s still a way out."
    scene train with fade
    show sofi:
        xpos 2.0
    # Sofi paces
    show sofi at right with move
    s "I could skip my stop, keep going, take a bus, another train. Maybe even get a plane ticket to somewhere far outside of the city."
    show sofi at left with move:
        yrotate 180
    s "I don’t carry much with me, so I can just abandon my life, make them think that I just had an accident or something."
    show sofi at right with move:
        yrotate 0
    s "It’s not like I owe them anything, right?"
    show sofi at left with move:
        yrotate 180
    s "Sure they did train me, yes I memorized the manual front to back, and yes there were lots of friends I made along the way but..."
    show sofi at right with move:
        yrotate 0
    s "what I’m about to do could amount to treason. And what if this whole thing is some kinda trap, some kinda deep cover operation to stop dissenters before they carry out their plans?"
    show sofi at left with move:
        yrotate 180
    s "But then why would they go through the trouble of training me? There were so many chances they could’ve had?"
    show sofi at right with move:
        yrotate 0
    s "But then what do I really know about how this whole thing works, and furthermore-"

    play sound "audio/ringtone.mp3" volume 0.1

    s "AGH!"
    s "Oh god, that scared me, but it's just my phone."
    show sofi at left with move:
        yrotate 180
    ## show Evan or his silhouette at right
    play sound "audio/phonebeep.mp3"
    s "Hello?"
    e "Hey, Sofi! I wanted to thank you again for filling in on such short notice! You did a great job, the bosses liked you, the kids loved you. Really good to tell them the truth about magic!"

    # Show sofi smile
    s "I had some space in my schedule and it was on the way."
    e "You really saved me there, I mean..."
    e "Who would’ve guessed that Mary was aiding a terrorist cell?"

    # Show Sofi sad
    s "Yeah, it’s crazy."
    e "I mean, seriously... she was in our office building! Where we had kids! What was she planning?"
    s "I don’t know."
    e "Honestly, this may not sound PC, but I hope they execute her. We can’t have people like her wandering freely."
    s "Right... Listen, I gotta go so I’ll talk later."
    e "Btw, I was talking to the bosses and they seem willing to overlook the... outburst from last year. Now, they can’t give you back your old position, but since the kids loved your story, and Mary’s gonna probably rot in a federal prison... maybe you could apply for her old job?"
    e "I can definitely put in a good word for you!"
    s "Thanks, I'll give it some thought!"
    e "Sounds good! Best of lu-"
    play sound "audio/endcall.mp3"
    s "..."
    s "I guess the call dropped. I'm not mad though, he was kind of rambling..."
    s "....."

    # she closes her eyes, and a look of anger appears on her face as she remembers the past
    ## show sofi_angry with eyes closed

    # Hold on Sofi for a few seconds, let her emotions run their course from anger, to sadness, to weariness, whatever seems right

    s "...."
    s "I guess I’m a traitor too."
    # Sofi’s stop comes up and she walks out the door
    ## play sound "train stopping, doors open"
    s "...."

    # Show Sofi sad and then sigh

    s "No turning back now."
    ## train announcement
    play sound "audio/trainstop.mp3"
    s "Sounds like it's time for my stop."
    scene black with fade

    ## Meeting Breeze
    scene cafe
    play sound "audio/cafe.mp3"
    show sofi at left with fade
    # Show sofi trying to look inconspicuous, maybe with both eyes closed, or one eye closed
    play sound "audio/ringtone.mp3" volume 0.1
    s "I'm getting a call from... Twisted Fates Dating Service?"
    play sound "audio/phonebeep.mp3"
    s "Hello?"
    noa "Hi, this is Noa, from Twisted Fates Dating Service!"
    noa "We set up a lovely date for you this evening at a lovely cafe at Cafe Haven, 13th Lakestreet!"
    noa "Your date should be around your age, has dashing blue hair, and a sexy cold disposition."
    noa "And once you see him, Tell him 'You're wearing nothing but a smile.'"
    noa "See you then~♡."
    s "I can’t help but cringe at all this."
    s "I mean, I know this whole operation is supposed to be covert so it’s not like they can just send a message like, 'HEY, YO, GIRL, GO HERE AND MEET UP WITH ANOTHER FIELD AGENT FOR INSURGENCY TREASON STUFF!'"
    s "Still, could that passphrase be any cringier?"

    # Show sofi blank stare as if she’s thinking about it
    s "......."

    # Sofi slaps her cheeks, face cheeks obviously, fuckin’ degenerates
    s "Okay, for real now. Inconspicuous, spy mode on. Let’s do this!"
    s "Scan your surroundings, but obviously don’t make it LOOK like you’re scanning!"
    s "What do you see?"

    # These do not need images and can use theater of the mind or silhouettes
    s "Office worker at the table on the far left, he’s overworked, unkempt, didn’t shower today... or yesterday... or maybe even this week. Probably works at an exploitative company."
    s "Not a threat. What else?"
    s "Woman outside with a dog on her phone and a kid running around. His mom? Sister? Babysitter? She looks busy, there’s trouble at home? Her body language suggests anger and annoyance."
    s "Not a threat. What else?"
    s "Two people a few spaces behind me in line, are they a couple? Seem to be the same age, seem pretty friendly, she touched his arm and he’s giving her a look but she’s- oh he’s getting friendzoned. Poor du-"
    show sofi at center with move
    cc "Ma’am, are you alright?"
    show sofi:
        xpos 0.52
    show sofi with move:
        xpos 0.48
    show sofi at center with move
    s "Agh!"

    s "What, yes, I-I’m Sofi, yes, that’s me, what’s up, what’s good bro, what do you need?"
    cc "I... need to know what you want to order?"
    s "Huh, o-oh right, cafe, right. I’m just here to order... um... something... to drink!"
    s "Which, I’m going to do."
    s "Riiiiight now."
    cc "...?"
    s "....."
    cc "....."
    s "........"
    cc "Ma’am... we really need to keep the line moving."

    # Show Sofi getting smaller with shyness and embarrassment
    s "Sorry! I just um... I... uh... words... I’m... uhhhh..."
    cc "...Hoooooow about a Tall Mocha Cappuccino?"

    # In a quiet voice, because she is experiencing emotional damage
    s "...yes, please, thank you."
    show sofi with move:
        xpos 1.5

    # transition scene to her sitting at her table
    # Show Sofi suffering
    scene cafe with fade
    show sofi at right
    play sound "audio/drinksip.mp3"
    s "......"
    s "It’s okay to cry Sofi. Every field agent probably has a similar story of their first mission."
    s "You’ll probably laugh at this someday!"
    s "Just sitting around a campfire with your guildmates, trading stories while on a vibrant hunt, and you can tell them about the time you imploded in the middle of a cafe."
    s "...."

    # Sofi pained groaning
    s "Well, first you need to actually find them."
    s "The mission brief said it's someone with blue hair and a cold disposition..."
    s "Well, that’s pretty basic. Not sure how to spot a 'cold disposition' from a distance..."
    s "Come to think of it, I’ve only ever seen other trainees and my mentor. I’ve never seen another field agent before."
    s "Let’s see... Guild mostly deals with fighting monsters and against those who would seek to use magic for evil purposes so..."
    s "This guy’s supposed to be like... someone who’s gonna show me the ropes, so he’s probably more experienced than me, right?"

    # Possibly show quick sketch of Sofi’s imagination
    s "Does he look like maybe... an old wizard? Too inconspicuous?"
    s "Wait, no, he probably fights monsters so maybe a badass monster hunter?"
    s "Wait... what if... he’s pretty handsome? Like, a prince from a faraway land come to redeem his family name?"

    # Sofi girl blush and squeal
    s "Ahhhhhh!"
    show breeze:
        xpos -1.0
    s "No, no, no, calm down, Sofi! Professionalism! Professionalism."
    s "I’m sure I’ll know him... when I see him."
    show breeze at left with move
    with Pause(3.0)
    s "...."
    b "...."
    s "Um...."
    b "Uh... sorry to disappoint, but I’m not an exiled prince."
    s "....."
    b "...."
    s "Um... a-are you... uh... Breeze? The person I’m supposed to meet here?"

    # Breeze slowly nods
    s "And... you heard all that?"
    show breeze with move:
        ypos 1.1
    show breeze with move:
        ypos 1.0
    b "...Sorry."

    # Show sofi sprite slide down as if she’s trying to hide her shame
    show sofi with move:
        ypos 1.1
    s "....I wanna die. Can you just hand in my resignation form? And I’ll just... live here for now."
    b "No can do, I’m afraid."

    # Sofi pained groan of sadness
    s "How’d you know it was me? I thought I was doing a really good job following the manual’s rules for covert behavior."
    b "Um... you were... at first."
    b "Sorry but... I think even an enemy agent, fresh out of one of those training academies in the capitol would’ve been able to spot you immediately."
    b "Good thing this cafe is friendly territory."
    b "Because if it were anywhere else, we probably wouldn’t be having this conversation."
    b "You’d probably be dead, or captured. I mean, on a scale of 1 to 10... your covert skills were probably at like a 3?"
    b "Did you struggle with that in your training?"
    s "...I actually got the highest marks during the assessment trials."
    b "Oh..."
    s ". . . . . . . "
    b "A-are you sure? Was your training group really small or-"
    s "Please stop, at this point you’re just kicking a girl while she’s down."

    # More Sofi pained noises

    s "Can we just start over? I don’t want this to be my first memory as part of the guild."
    b "...sure, I guess?"

    # Sofi collects herself and picks herself back up
    # She clears her throat
    show sofi with move:
        ypos 1.0
    s "So... uh... what was I supposed to say again? Something about a-"
    s "Ah!"
    s "Ahem!"
    s "I’m wearing nothing but-"
    b "Please. Don’t. We can just skip that portion, for our own sake. But mostly for yours."
    s "But... the manual says..."
    b "Yeah, I know, I know. But, I’m gonna give you some advice, newbie."
    b "An agent who does everything by the book is predictable, and a predictable agent won’t be predictable for very long."
    s "B-Because he’ll be so efficient that he’ll be a great asset to the guild?"
    b "Uhhhh, no, it’s because he’ll probably be dead and his body disposed of in a ditch somewhere in the middle of nowhere."
    b "The manual will help, sure. But it’s important to be flexible, since you’ll probably end up running into things that go outside the scope of your training. And it’s in that moment, where the only thing that’ll save you is your wit, determination, and a lot of luck... that’s what’ll determine if you’re truly cut out for this life."

    b "Anyways, we’ve confirmed our identities, so let’s head out."
    show breeze at slightright with move
    s "Wh- right now? We’re leaving now?"
    b "No, this space is just a rendezvous in friendly territory. Though... friendly or not, it’s not good to talk openly about... certain things in mixed company."
    s "Oh, right, that was in the manual too."
    b "Great, so let’s head upstairs."
    s "Right. Upstairs."
    s "..."
    s "Wait, what? We can just... go up there?"
    b "Yeah, it’s a weird business model, but the cafe also doubles as a short-stay inn upstairs."
    b "Hm... bed and breakfast would probably have been a more appropriate business descriptor, but that wasn’t my choice to make so...."

    # Breeze shrugs

    s "Uh-huh..."

    # Show the sprites begin to walk off screen, have Sofi stall
    show breeze with move:
        xpos 0.9
    show sofi with move:
        yrotate 180
    with Pause(1.0)
    b "Something wrong?"
    s "...You’re like...not gonna murder me, right?"
    b "......."
    s "....."
    b "......."
    s "...Please say something."
    b "We... should probably hurry upstairs."
    show breeze with move:
        xpos 2.0
    s "...That’s not a no."

    scene black with fade

    # Fade in to private room upstairs, there’s nothing particularly special about it, it’s just a normal room
    scene rendezvous with fade
    show sofi at right
    show breeze at center
    # Show Breeze in the corner while Sofi’s sprite is pacing around
    # Breeze seems to be checking the time on his phone or something
    s "Hey what was your name again, buddy?"
    show sofi at right with move
    b "What? Did I forget to introduce myself?"
    show sofi at left with move
    b "It’s Breeze."
    show sofi at right with move
    s "Breeze huh? That is a wonderful name that your parents gave to you. Nice and… airy?"
    show sofi at left with move
    s "And, my name is Sofi, of course. My parents told me that it means Wisdom, I guess they wanted me to grow up to be a wise girl."
    show sofi at right with move
    s "Though, I also heard that it might also mean pure? Name meanings are weird like that."
    show sofi at left with move
    s "Ha… I’m not sure if I really live up to either of those names."
    show sofi at right with move
    s "I mean, I came upstairs to a private room with a boy I just met for the first time today."
    show sofi at left with move
    s "I don’t usually do things like this, you know?"
    show sofi at right with move
    b "Yeaaaaah? I guess that’s- wait, did you say usually?"
    show sofi at left with move
    s "Eheheh, so… what else do you like, music? Movies? Books? Read any good books lately? I recently read a book about two people who got heartbroken and found comfort in each other."
    show sofi at right with move
    s "You know, in the fan community, there’s actually some debate about whether the two characters hooked up or not on that first night."
    show sofi at left with move
    s "My theory is that-"
    show sofi at right with move
    b "What are you doing?"
    show sofi at left with move
    s "Wh-what do you mean? I’m just making some light convo?"
    show sofi at right with move
    b "Noooooo, you’re wandering around the room like you’re looking for-"
    show breeze at left with move
    b "Wait a minute, you’re checking for bugs!"
    s "Well, thanks for spelling it out! And why aren’t you doing the same, that’s like… one of the basic rules of covert operations! And you know how the state’s surveillance program has ramped up in recent years-"
    s "Wait a minute, was that you guys?"
    b "Uhhhhhh, maybe, but we’re not the only enemies of the state. On the surface, our guild, The Erasers, is just a normal monster hunting guild and other such odd jobs. The whole insurgency thing is for the inner circle."
    b "But that’s beside the point, you don’t need to check for listening devices here."
    b "Like I said, this place is friendly territory."
    b "What I meant was that the guild uses this space as a money laundering front, among other things. So the staff here are our people."
    b "I don’t really know the full details, need-to-know basis. Bottom line though, you don’t have to worry about the administration or a rival guild planting listening devices."
    b "Lemme see your phone?"

    # Sofi hands him the phone, this doesn’t need to be anything, just tilting Sofi towards Breeze’s sprite
    show sofi at center with move
    show sofi at right with move
    s "What are you gonna do with it?"
    b "I need to start the mission briefing."

    # Breeze pulls out his own phone, obviously he doesn't have a sprite for that
    b "Your phone’s newer than mine. No problem, no problem, lemme just… figure this out..."
    # beeping noise
    b "Okay got it."
    # Breeze puts the phones down on the table, both phones are glowing
    ## From both phones, something starts to form between them. A small projection of a humanoid shape.
    s "I stared blankly at the figure until recognition started to form. I’d only ever seen her once before, but this would probably be the first time I’ve seen her up close."
    s "A small hologram of the leader of the guild, in a small and cute form, appeared on the table."
    # show Kizuna at center
    # Kizuna’s sprite should be visible now. I don’t know if we’re using a chibi kizuna or just a shrunken down version of her full sprite
    s "Ms Kizuna."
    k "Greetings agents, I hope you’re doing well this evening."
    s "Even as I’m looking at her right now. It’s hard to keep calm when the boss is actually speaking to you."
    s "Fortunately this is probably just a recording."
    k "Sofi, are you paying attention?"
    b "Anywaaaays, let’s just cut to the chase."
    k "Very well, we will skip the pleasantries."
    k "A few days ago, a video began to circulate around social media."
    k "The uploader is… um…"
    k "XXXTresPassinNathan69?"

    # Snickering Sofi sound
    # Beat
    # Sofi throat clear

    s "Sorry."
    k "Right… well, this… Mr. Nathan’s content is primarily, him trespassing, and then filming it."
    k "Under normal circumstances, this wouldn’t be relevant to our goals. However…"

    # Show bg sewer tunnel, shake the cam a bit as if it’s being filmed, no dialogue though because I don’t want to
    scene sewer_tunnel with fade
    k "Watch closely."
    show play at truecenter
    hide play with Dissolve(0.7)
    show rat2 at offscreenright
    with Pause(2.0)
    # Hold the scene
    # Show a Vibrant sprite (probably the base form but with a non-red color) rush across the screen and blur it like it’s a motion blur
    show rat2 at offscreenleft with move:
    with hpunch
    # Pause the image or show the shake then the pause
    show pause at truecenter
    hide pause with Dissolve(0.7)
    s "What is that? Some kind of animal?"
    k "Our analysts thought the same, and under normal circumstances we would assume as much. However, every time this video was uploaded, it was immediately scrubbed off the site as well as search engines."
    b "Someone’s trying to bury the video?"
    s "Is that really so strange? Lots of people get videos taken down."
    b "That’s true but… our analysts wouldn’t just engage in conspiracy theories, there’s something else in the video? If it was just an animal attack, why try so hard to hide it?"
    scene rendezvous with fade
    show breeze at left
    show sofi at right
    # show kizuna1 at center
    b "..."
    show breeze at slightright with move
    # Breeze gets closer to the image
    b "Zoom in on that blurry thing right there?"

    # make the blurry vibrant bigger
    b "...Is that a vibrant? Why does it look like that?"
    # The vibrant is probably a strange color, this is an easy thing to do with access to the assets

    k "We are unsure."
    k "If that is indeed a vibrant, it is not one we’ve ever seen before."
    k "In the best case scenario, it is either an animal or a fabrication."
    s "And, worst case scenario?"
    k "...A mutant strain, a new breed, a hybrid, whether it’s a solitary predator or part of a larger nest. There is no record of such a creature in our database, that means this creature, if it is a vibrant is an anomaly of sorts."
    k "And that, my dear agents, are what you are to uncover."
    b "So, this is a recon mission, essentially?"
    b "Alright. Where that video was filmed?"
    k "Our people did a thorough investigation from analyzing the video, and we believe we have triangulated a general location based on reports from our undercover assets in the city."
    k "From there, we narrowed down places where a potential nest could be, and that leads us… here."
    k "An old service tunnel that has been in disuse since the city came under new management."
    k "Your mission is to conduct a reconnaissance operation. Go to the destination marked on your devices, determine if it's a single vibrant, a nest, or something more sinister, then report in."
    k "If luck is on our side, it will have only been an elaborate ruse from a man desperate for the attention of the faceless masses."
    k "I will also remind you to exercise extreme caution. If this is indeed a new strain, then its capabilities are unknown."
    k "And Breeze, if I may…"
    b "What’s up, Kizu-nee?"
    k "...This is strictly a reconnaissance mission."
    k "Do not do anything unnecessary. I do not care for reckless agents who get themselves killed."
    k "May safe winds guide your sails back to me, my Erasers."
    jump tunnel
    return
