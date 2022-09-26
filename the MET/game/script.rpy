﻿# the MET

# Declare characters
define larry = Character("Larry")
define annie = Character("Annie")
define mystery = Character("?")
define chad = Character("Chad")
define brad = Character("Brad")

# Declare images
image bg livingroom night = "images/livingroom_night.jpeg"

label start:

    # play music "night"

    scene bg livingroom night
    with fade

    show larry scared
    
    larry "Wait, please! Please, stop!"
    larry "I'll give you anything--money, you want money? I'll give you all the money you want!"
    larry "I'll give you anything you want, just tell me what you want! I'm begging you ... I have a family!"

    mystery "You should have thought of them before messing with my family."

    larry "No, no, don't do this! My daughter--"

    mystery "The way I see it, I'm doing her a favor."

    # thud of body hitting the ground

    mystery "Well ..."
    mystery "That's been quite enough excitement for one night!"

    scene bg livingroom day
    with fade

    annie "Good morning, Larry, dear! Did you have a good night's rest?"
    annie "Why, Larry, you've bled all over the carpet! A bit inconsiderate of you, I must say."
    annie "You're just going to lie there, are you?"
    annie "Well, I certainly never expected a sex trafficker to have any manners."
    annie "I suppose it's up to me to clean up around here."

    # task: use stain remover to clean the carpet
    $ choiceA = False
    $ choiceB = False
    menu stain_remover:
        "You find a bottle of stain remover."

        "Offer Larry a drink." if choiceA == False:
            $ choiceA = True
            "His teeth are now cleaner than ever! And he's hydrated."
            jump stain_remover
        
        "Drink it yourself." if choiceB == False:
            $ choiceB = True
            "Tastes like orange juice. You get a stomach ache."
            jump stain_remover

        "Scrub the carpet.":
            jump clean_carpet

label clean_carpet:

    annie "Much better! ... What's that stench, though?"
    annie "Larry, sorry to embarrass you, but you smell like you haven't showered in quite a while."

    # task: drag larry's body into the bathtub
    $ choiceB = False
    $ choiceC = False
    menu bathtub:
        "Larry's being an inconsiderate guest."

        "Drag him into the bathroom.":
            annie "Not to worry, though! Please feel free to use the hallway bathroom to freshen up."
            annie "Let me help you out--I see you're having some trouble getting up this morning."
            jump bathroom_1
        
        "Drag him outside." if choiceB == False:
            $ choiceB = True
            "The body is heavy, but you manage to push it out the front door."
            "Police officers see that you're in possession of a life-size human piñata and arrest you for suspicious activity."
            jump bathtub

        "Drag him onto the couch." if choiceC == False:    
            $ choiceC = True
            "You help Larry get comfortable on the couch with a blanket and some pillows."
            "It doesn't help the smell."
            jump bathtub
    
    jump bathroom_1

label bathroom_1:

    scene bg bathroom

    annie "Oh dear, we've got a bit of a pickle. You don't quite fit inside the bathtub, Larry."
    annie "Hmm ... let me think."
    annie "Ah, I've got it! Let me find my tools."
    annie "No, don't worry, it won't be any trouble at all! I promised to be a good host, didn't I? Only the finest hospitality for you, Larry."

    jump kitchen_1

label kitchen_1:
    
    scene bg kitchen
    with fade

    # task: find the right tool to chop larry up
    $ choiceA = False
    $ choiceB = False
    $ choiceD = False
    menu find_tool:
        "Find something that will help Larry rest in pieces."

        "Scissors" if choiceA == False:
            $ choiceA = True
            annie "I think I'll need some bigger scissors than these."
            jump find_tool

        "Blender" if choiceB == False:
            $ choiceB = True
            annie "I don't think Larry will fit inside this ... yet."
            jump find_tool

        "Meat cleaver":
            annie "This will work wonderfully!"
            jump meat_cleaver

        "Rolling pin" if choiceD == False:
            $ choiceD = True
            "You're not strong enough to flatten him."
            jump find_tool
        

label meat_cleaver:
    scene bg bathroom
    with fade

    annie "Alright, we're about to get started--please hold still!"
    annie "There you go, dear! Now you fit inside the bathtub very nicely."

    # sound: doorbell, pounding on door

    annie "Oh, that must be the police! I've been expecting them. Sit tight, Larry, will you?"

    jump front_door

label front_door:

    scene bg front door
    with fade

    # show chad and brad, side by side
    
    annie "Hi, can I help you two?"

    brad "Good mornin' and sorry to bother you, ma'am. I'm Officer Brad, and this here is my partner, Officer Chad."

    chad "We're here on official business regarding the case of a missing person, and we'd just like to ask you a few questions, maybe take a look around the place if you don't mind."

    annie "Not at all, please come in and make yourselves at home."

    brad "Well thank you very much, ma'am. You've got a real nice place."

    jump couch_1

label couch_1:

    show bg couch
    with fade

    chad "Allow me to get to the point. What do you know about Larry Russell?"
    chad "Some of his acquaintances contacted our station to report that he's gone missing, and they also say that he recently booked a short-term rental at this address."

    annie "Ah yes, I remember Larry! I rent this apartment out to tourists, and he was my most recent client."
    annie "Plenty of travelers book rentals at this location since it's so close to the Met."

    chad "What can you tell us about Larry? Did you interact with him at all?"

    annie "Well, his stay here ended yesterday, and I certainly haven't got any Larry's living in the house anymore."

    brad "Hey, uh, sorry to interrupt the investigation, but would you mind if I used your restroom? Drank a lot of coffee with my donuts this mornin' and I'm startin' to regret it."

    annie "Of course! There's a bathroom down this hallway."
    
    $ choice_bathroom = False
    menu brad_bathroom:
        "What should you do?"
        
        "Let Brad use the bathroom." if choice_bathroom == False:
            $ choice_bathroom = True
            annie "Go right ahead, Officer Brad."
            jump bathroom_fail

        "Tell Brad to wait while you check the bathroom.":
            annie "Just give me a moment to make sure everything's in working order."
            jump bathroom_success

label bathroom_fail:
    
    hide brad   # brad leaves the living room

    chad "Right, uh, so I'd like to ask you a few more questions."
    
    annie "No problem at all!"

    chad "Do you know what time Larry arrived at this apartment, two days ago?"

    annie "Well, I was away visting my son, so I don't know exactly when."

    show brad   # brad returns

    brad "Hey, Chad, I think I found our guy."

    chad "What?"

    brad "He's in the bathtub."

    chad "God, Brad, did you walk in while someone was showering again?"

    brad "That was one time! And no, Larry is--well, he's not alive anymore."

    chad "Brad ... you actually did something helpful for once. I--I think I might cry."

    "No getting out of this one. Brad and Chad arrest you on the spot as their prime suspect."

    jump brad_bathroom

label bathroom_success:
    scene bg bathroom
    with fade

    # task: enter the bathroom and pull the shower curtain
    $ choiceA = False
    $ choiceC = False
    menu pull_shower_curtain:
        "Larry's still lying there in the bathtub."

        "Spray some air freshener." if choiceA == False:
            $ choiceA = True
            "Not strong enough. The body is still pretty visible."
            jump pull_shower_curtain

        "Pull the shower curtain.":
            annie "That should do it! They won't notice Larry now."
            scene bg bathroom shower curtain    # change art for shower curtain
            with fade
            jump couch_2

        "Flush Larry's parts down the toilet." if choiceC == False:
            "They won't fit. Maybe after some hydrofluoric acid ..."
            $ choiceC = True
            jump pull_shower_curtain

    jump couch_2

label couch_2:

    annie "Alright, please go ahead!"

    brad "Don't mind if I do."

    hide brad

    chad "Right, uh, so I'd like to ask you a few more questions."
    
    annie "No problem at all!"

    chad "Do you know what time Larry was supposed to check out yesterday?"

    annie "Hmm, I'm not sure. His rental contract stated that he just needed to vacate the property by midnight."
    annie "I didn't see him move out, but he did return his set of keys on time."

    show brad

    brad "Hey Chad, did you get aroun' to askin' my list of questions yet?"

    chad "No, I was just--"

    brad "Okay, ma'am, could you tell us what Larry looks like?"
    brad "I think knowing his hair color and height would really help me recognize Larry when we find him."

    chad "Brad, those details were provided in the case file. We should--"

    brad "Oh really? Well, that's all the questions I had."
    brad "Thanks very much, ma'am, you've been a great help, I think we've got everything we need to find this missing Larry person."

    chad "No, Brad, we don't. We've discussed this before. If you would just--"

    # task: get the arms and put them in a trashbag
    $ choiceA = False
    $ choiceB = False
    menu get_arms:
        "They've been talking for a while ..."

        "Ask a question." if choiceA == False:
            $ choiceA = True
            annie "Sorry to interject, but how do you two feel about our current economic and political system?"
            "Brad and Chad turn to look at you, their faces blank."
            "With no explanation, they arrest you for asking questions."
            jump get_arms

        "Just let them talk." if choiceB == False:
            $ choiceB = True
            "They keep talking."
            "..."
            "You die of boredom."
            jump get_arms

        "Slip away.":
            "This is your chance to get rid of some evidence."
            "You go to the bathroom, put Larry's arms in a trashbag, and return. Your absence goes unnoticed."
            jump dispose_arms

label dispose_arms:

    chad "If we're going to make any kind of progress, I need you to--"

    annie "Officer Brad, would you do this old lady a favor?"

    brad "Sure, ma'am, what is it?"

    chad "No, Brad, you are not getting distracted again like last--"

    annie "I need to take out the trash to the sidewalk, but I've been feeling quite frail these days."
    annie "You've got a nice, strong pair of arms, would you be a dear and help me?"

    brad "That would be my pleasure ma'am! We're here for public service and I intend to serve."

    hide brad

    # task: ask chad if he likes dogs
    $ choice_cat = False
    $ choice_bird = False
    menu chad_likes_animals:
        "You have an opening to talk to Chad. What do you say?"
        
        "Do you like cats?" if choice_cat == False:
            $ choice_cat = True
            chad "I've rescued a couple cats on the job. Do you own a cat?"
            annie "No, I don't."
            jump chad_likes_animals

        "Do you like dogs?":
            chad "Well, yes, I do, but I think we're all getting off track here and I'd really--"
            annie "Perfect! You don't mind helping to feed the neighbor's dog, do you?"
            annie "I'll just grab a bowl from the kitchen. Wait here a moment, please!"
            jump kitchen_blender

        "Do you like birds?": if choice_bird == False:
            $ choice_bird = True
            chad "Yes, I love birdwatching, actually."
            annie "But haven't you heard that birds are actually government drones?"
            chad "Wait, what?"
            jump chad_likes_animals   

label kitchen_blender:
    
    scene kitchen

    # task: blend torso and put into a large dog bowl

    jump couch_3

label couch_3:

    scene couch

    annie "Here we go, fresh protein for the pup next door."

    chad "I really don't think feeding dogs is part of the protocol."

    brad "How could you make a sweet old lady walk so far? She's already done the work of making the food, and you can't just deliver for her?"
    brad "Shame on you Chad, shame. Do I even know you?"

    chad "... Fine, I guess."

    annie "Go on, it's just the apartment over on the left."

    brad "I'll even go with you to help!"

    # objective pop-up: kitchen to bake pie

    jump kitchen_3

label kitchen_3:

    scene kitchen
    with fade

    jump couch_4

label couch_4:

    scene couch
    with fade

    annie "Thank you, Brad, and thank you, Chad. You two are truly, truly wonderful."
    annie "It makes me feel at ease to know that such diligent officers are out protecting the streets."

    brad "Happy to help anyway I can, ma'am."

    chad "Well ... I suppose we can always spare the time for some public service."

    annie "I only need help with one more chore, if you would be willing?"

    brad "Anything for you ma'am! Ask away!"

    annie "So my son--he's hosting a barbeque this afternoon, but I won't be able to make it, so I told him that I'd send over a nice cut of meat."
    annie "I've got a roll of butcher paper and some twine, and I just need help wrapping the stuff up."

    # task: bring legs from bathtub to kitchen

    jump kitchen_4

label kitchen_4:

    scene kitchen
    with fade

    chad "Say, uh ... what kind of meat is this?"

    annie "Some fresh fish filets I picked up from the farmer's market."

    brad "They sure look fresh to me! Real nice for an autumn barbeque, don't you think, Chad?"

    chad "Uh, looks like the fishmonger missed a couple of fish scales."

    chad "(Are those ... ? They look a bit like toenails.)"

    brad "Honestly, I'm gettin' pretty hungry myself, just thinkin' about barbeques."

    # ding sound

    annie "Oh! I nearly forgot about my pie! Wait one moment, please."

    # annie takes pie out of oven

    annie "Please try a slice! It's the least I can do to thank you both for helping me out so much today."

    brad "That pie sure looks good, ma'am. What do you think, Chad?"

    chad "It's not strictly professional to eat on the job ... but it has been a long few hours since breakfast."

    annie "Please, I insist! I've been told that my meat pies are fantastic."

    # brad, chad enjoy the pie

    brad "That was delicious!"
    brad "Well, I guess we had better get goin' back to the station. Did we get all the evidence we needed Chad?"

    chad "More or less, I suppose. We asked some good questions and did some public service."

    brad "Yeah! Maybe the Chief will award us a medal for our good work."

    annie "That certainly sounds well deserved."

    # brad, chad leave

    jump ending

label ending:

    scene bg livingroom day
    with fade

    annie "Works every time."
    annie "Now, time to brew up a nice cup of tea."

    "the end."

    return