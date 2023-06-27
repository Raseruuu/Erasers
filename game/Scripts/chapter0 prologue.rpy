label prologue:
    scene black
    play music tomotheme volume 0.1
    play sound "audio/crowd.mp3" fadeout 1.0
    u "Welcome!"
    pause 1
    play sound "audio/ahem.mp3" volume 0.5
    u "{i}clears throat{/i}"
    stop sound
    u "Welcome, weary travelers! Come sit closer, my eyesight is not what it once was."
    u "A name? Ah, yes..."
    scene stage
    play sound "audio/spotlight.mp3"

    show sofi with fade
    s "I’m Sofi The Story Weaver."
    s "I’ve come a long way, gathering stories in my travels."

    # show images relating to the things she’s talking about

    s "Tales of great heroes, monstrous creatures, of love and romance, of heartbreak and tragedy. I’ve heard them all, committed them to memory, and I have come to pass them on to you."
    s "Stories, after all, are made to be told. For if we keep them to ourselves..."

    play sound "audio/spotlight.mp3"
    ## a small spark of fire starts up
    scene black with Dissolve(2.5)
    s "But... what story should I tell you?"
    s "Hmmmm..."
    s "Ah, I have one here!"
    scene magicstory
    s "The Story of Magic."
    s "The gift that was granted to humanity, a power that allows us to reshape reality according to our whims. To bring us to prosperity, enlightenment, and peace."
    s "Through these gifts, humans stepped out of the shadows, and brought forth the age of magic."
    # Show earth and the spread of magic
    s "But... like every story, this chapter in history would also..."

    play sound "audio/bookclose.mp3" volume 0.5
    scene black with fade
    s "Come to a close."
    s "Humans were capable of great things, but some sought to use magic for evil."
    s "Evil humans abused the gift of magic to do harm to others, to usher in an age of darkness."
    s "And then... something broke."
    scene redearth with Dissolve(2.5)
    s "The Crimson Calamity, as if heralded by the thunderous cry of a world in pain, came from beyond the veil."

    scene vibrantattack

    s "This new threat could not be reasoned with, it could not be frightened, or bought. It only hungered."
    s "The spark of life would soon fade, devoured by the ravenous maw."

    # show the world growing dark... but then, a small spark illuminates
    scene black with Dissolve(2.5)
    s "Until..."
    s "He arrived."

    # show Eraser's Silhouette
    show eraser with fade
    s "A mysterious stranger who took up the mantle of our savior. On his watch, we would not perish."
    s "The downtrodden masses rallied around his banner, and through his leadership, his power, and his determination to save us... humanity would finally defeat the Crimson Calamity!"

    # Show a triumphant group of people and a lone Eraser

    s "But... no victory comes without its price."
    play sound "audio/shatter.mp3" volume 0.2
    hide eraser with shatter_out

    scene black
    s "Magic faded. And..."
    s "So did our savior."
    s "The age of prosperity ended, and ushered in the age of depravity, which was then devoured by the age of calamity, and when the dust settled... the age of silence remained. A penitant age for our sin of hubris."
    s "Centuries passed, civilizations rose and fell, our story pressed on even as the world we once knew faded into oblivion and myths."
    s "No one was left to remember the Crimson Calamity, the Vibrants. Nor the hero who sacrificed everything to save us, the man we only knew as Eraser."
    # Show a moment of silence with a darkened world

    s "At least, that was the story up until 20 years ago."
    s "Like an old friend, magic returned to us, and brought with it the great wonders we once enjoyed."

    # show the new world, or a representation of it

    s "But, like I said earlier; where there is light, there is darkness."

    scene redearth with Dissolve(2.0)
    s "Humanity’s greatest threat had also returned, predators of magic, Vibrants."

    scene vibrantattack with Dissolve(2.0)
    s "But don’t you fret, little ones. Our enemies are powerful, but humanity is not as weak as it once was. We will defeat this enemy, and bring peace to the land."
    s "With magic on our side... nothing is impossible!"

    # show humans triumphing over vibrants
    s "But, stories are not just told to entertain. They are also lessons from the past, lessons that we must learn lest we suffer the same fate."
    s "Our ancestors’ abuse of magic nearly destroyed us all."

    # Show a human silhouette succumbing to Umbra
    s "And if we stray from the path of harmony; then perhaps, the story of humanity too will come to a close."

    scene stage with Dissolve(1.5)
    s "And with that, we end our story... for now."
    play sound "audio/applause.mp3"
    s "I'm glad you all enjoyed that, I'll see you next time!"
    ## slide BG to show camera facing Sofi, recording light turns off
    scene black
    stop sound fadeout 10.0
    s "{i}sigh...{/i} It's finally over."
    scene black with fade

    jump pretunnel