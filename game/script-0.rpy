label script_0_start:
    stop music fadeout 2.0
    scene bg_cellblock_morning at bg_scaled with fade

    play sound "audio/Atmosphere/stationcellblocks.mp3"

    "..."

    "Officer Maddox" "Let's go! Everyone up."

    show char_l_idle at t31 with dissolve

    l "..."

    "My eyes open. The light peers into my view."

    "The officers bang their batons on the cell blocks."

    "I hate when they bang on the metal."
    "I miss when they used to play music through the speakers."
    "Before management changed."
    "Now it’s just sirens and yelling."

    "Officer Maddox" "On your feet, eyes front! If your boots ain’t touching the line in ten, I’m dragging you out myself."

    "My neck is sore."
    "Oh, how I would kill for a few more hours."

    "I stand up and let out a yawn."

    "Officer Maddox" "On the line, 218. You know the drill."

    hide char_l_idle
    show char_l_speak at t31 with dissolve

    l "I'm working on it."

    hide char_l_speak with dissolve

    "My voice is still pretty groggy."
    "I place my feet directly on the line."

    "I hear keys jingle a few cells down—then a groan."

    "Some idiot probably just got smacked awake."

    s "OWIE OWIE! OKAY I'M UP! I'M UP!"

    "Wait. I know that voice."
    "It’s Suki."

    "Oh man, Suki."
    "I can almost guarantee she was up all night, piecing together another 'custom outfit' from the jumpsuits we’re given."
    "Fashion icon of Cell Block C."

    "Officer Reina" "Everyone. Step out."

    play sound "audio/Atmosphere/stationmorning.mp3"

    "A loud buzzer sounds off."
    "The metallic doors slide open in front of me."

    "Officer Bryn" "Move it. Line up."


    show char_n_idle at t21 with dissolve

    hide char_n_idle
    show char_n_speak at t21 with dissolve

    n "Hey, uh—could mine be, like, slightly looser?"
    n "It’s just, my mom said circulation runs weird in our family—"
    n "I mean, not weird weird..."
    n "We’re totally normal."
    n "Healthy. Don’t worry, it's more like—"


    "Officer Bryn" "Keep moving."

    hide char_n_speak
    show char_n_idle at t21 with dissolve

    n "Aaa... yes sir."

    "Niko shuffles forward."


    "I hear him muttering under his breath."

    n "...I mean, like, ninety-nine percent normal..."

    "Officer Bryn" "Keep moving."
    hide char_n_idle with dissolve
    show char_n_speak at t21 with dissolve

    n "Aaa... yes sir."

    hide char_n_speak with dissolve
    show char_n_idle at t21 with dissolve

    "Niko shuffles forward."
    "I hear him muttering under his breath."

    n "...I mean, like, ninety-nine percent normal..."

    hide char_n_idle with dissolve

    "Officer Reina" "Single file everyone."

    "No one says anything after that."
    "We keep walking—straight to the cafeteria."

    play music "audio/Music/daily.mp3" fadein 2.0

    scene bg_cafeteria at bg_scaled with dissolve

    ############### MUSIC CHANGE
    #play music "audio/Music/sunrise.mp3" fadein 2.0
    
    "Gross."
    "I can already smell it."
    "Cold eggs, mashed potatoes, and whatever that gray mush is supposed to be."
    "Meat? Maybe."
    "Tomo’s gonna hate this one."

    scene bg_cafeteria_table at bg_scaled with dissolve

    "I grab my tray and head to my usual spot."


    show char_l_idle at t31 with dissolve

    "I hear another slam of a tray hit the table as I sit down."

    show char_s_idle at t33 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    #stop music fadeout 2.0
    ############### MUSIC CHANGE
    #play music "audio/Music/friends.mp3" fadein 2.0

    s "Your favorite inmate has arrived."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "She bows like she’s on stage."

    show char_t_idle at t22 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Hey now—I might be his favorite."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Yeah totally... not."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "Suki finally sits down."

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Did you see what they served us?!"

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "What—the eggs and mystery meat again? I already want to throw it away."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "No no no—look closer. Open the wrap."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "I peel back the plastic wrap slowly."
    "No way."

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "...No way."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Yes way."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Hold up—brownies?!"

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "It’s been months since we’ve had a treat day."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Exactly."
    s "Which means... someone up top either slipped up or felt generous."
    s "And I don’t think generosity’s in the budget."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "She holds her brownie like it’s evidence in a trial."
    "Tomo eyes it like he’s trying to do the math."

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Didn’t they cut food spending last cycle?"

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Yeah. That’s what I mean."
    s "This feels cursed."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "You don’t have to eat after all, you can always give it to me."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    "Tomo smiles from cheek to cheek."

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Oh no, I’m still eating it Tomo and I am eating yours."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "HUH?"

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Kidding."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "If you want, you guys can have mine."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "No way, really?"

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Woah."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Yeah way. I’m too busy thinking about this week’s schedule to enjoy it."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "Suki splits the brownie with Tomo."
    "She takes a bite and gestures her hand."

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    #stop music fadeout 2.0
    ############### MUSIC CHANGE
    #play music "audio/Music/silly.mp3" fadein 2.0

    s "Mm- Wait yeah, anyone know what the chore rotation is for today?"

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Hopefully not reprocessing again. I still smell like chemical burn from last time."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "I’m praying for laundry duty. Let me have it. I need it."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "You only like laundry duty to steal more material for your projects."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Not stealing. Repurposing."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "No, you stole my pants that one day. I had to walk around with nothing but a towel!"

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Hahaha, oh yeah. You tried to file a formal complaint in a bath wrap."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Wait, what? When did this even happen?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "You were off doing that ductwork inspection that day with Maika. Ventilation Subsection 3C, I think."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    "Maika. I still miss her."
    "Can’t believe there used to be four in our friend group."
    "We’d always get randomly paired for chore rotation."

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Wait—wasn’t that the day Maika found that giant rat?"

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Oh yeah. Lune came back looking like he saw a ghost."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve
    hide char_l_idle with dissolve

    "Ventilation day. So many rats."

    "I swear the rats here don’t look right. Too many legs, or something. I don’t know. Just... wrong."

    show char_l_speak at t31 with dissolve

    l "It crawled out of the vent, okay? And it just... stared at me. It wasn’t normal. The thing was huge!"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Uh-huh. Maika said you screamed so loud she thought you got stuck in the vents."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "I didn’t scream THAT loud—I just... reacted. It was instinct."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Sure. That’s why you spent a week checking under your bunk like it had unfinished business."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "...You could hear me all the way from your cell?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Yep! Haha."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Big bad Lune. Defeated by a single rat."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "...It wasn’t a normal rat..."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Right."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    "I think back to all the stuff we’ve been through."

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "...Man, we’ve been through some stupid stuff."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "No kidding."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "I say there's still more to do."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "What does that mean? What are you planning?"

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Not here, obviously... But—I've decided something."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "That’s never good."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "When we get out of here—We’re opening a restaurant."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "…That is not what I expected her to say."

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "A restaurant. Us?"

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve
    
    # --- Player Choice Inserted Here ---

    menu:
            "Support the idea wholeheartedly.":
                $ trust["suki"] += 1
                $ trust["tomo"] += 1
                $ trust["maika"] += 100
                $ fear["maika"] += 0
                
                l "Honestly... that sounds amazing. I'm in."
                
                hide char_l_idle with dissolve
                show char_s_speak at t33 with dissolve

                s "Knew you'd have taste!"

                hide char_s_speak with dissolve
                show char_s_idle at t33 with dissolve

                hide char_t_idle with dissolve
                show char_t_speak at t22 with dissolve

                t "If we're running it, count me in too."

                hide char_t_speak with dissolve
                show char_t_idle at t22 with dissolve

            "Laugh it off, thinking she’s joking.":
                $ fear["suki"] += 1
                $ trust["maika"] += 0
                $ fear["maika"] += 100
                
                l "Pfft—sure, Suki. A restaurant. Real realistic."

                hide char_l_idle with dissolve
                show char_s_speak at t33 with dissolve

                s "Hey! I'm serious!"

                hide char_s_speak with dissolve
                show char_s_idle at t33 with dissolve

                hide char_t_idle with dissolve
                show char_t_speak at t22 with dissolve

                t "Honestly? I'd eat there. At least it'd be edible."

                hide char_t_speak with dissolve
                show char_t_idle at t22 with dissolve

            "Be skeptical, but thoughtful about it.":
                $ trust["suki"] += 1
                $ fear["tomo"] += 1

                $ trust["maika"] += 0
                $ fear["maika"] += 100

                l "It’s a nice dream. I just... don’t know if we’ll get that chance."

                hide char_l_idle with dissolve
                show char_s_speak at t33 with dissolve

                s "Then we’ll have to *make* the chance, won't we?"

                hide char_s_speak with dissolve
                show char_s_idle at t33 with dissolve

                hide char_t_idle with dissolve
                show char_t_speak at t22 with dissolve

                t "...Man. Now you’ve made me nervous."

                hide char_t_speak with dissolve
                show char_t_idle at t22 with dissolve

    # --- Main Story Resumes Normally Here ---
    
    "({color=#00FF00}Trust with Suki: [trust['suki']]{/color})"
    "({color=#00FF00}Trust with Tomo: [trust['tomo']]{/color})"
    "({color=#FF0000}Fear with Suki: [fear['suki']]{/color})"
    "({color=#FF0000}Fear with Tomo: [fear['tomo']]{/color})"

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Mm-hmm."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Why a restaurant?"

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Because it’d be fun. Don't you think?"

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Actually… Yeah. I kinda do. Anything we make would be an upgrade from the culinary war crimes they serve here."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Wait—we get to make food we actually like? Okay yeah, I’m in."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "See? It’s perfect. I get to boss everyone around too."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Never mind. I'm out."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Kidding. I’d work the front—hostess, full charm, wow the customers. Tomo... can be... our finance guy."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Finally, my intellect is recognized. I'll keep us out of debt."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "If 'nerd' is what you meant, then sure."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Alright, boss. What about me? What’s my glamorous role?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Well… if Maika were here, she’d be our head chef. So you can't have that role."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "I smile at that."

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "So that leaves... Taste-testing."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Taste-testing?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Yep. Quality control. You wouldn’t want your queen getting food poisoning, would you?"

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Can’t have that."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Trusting Lune to look over real food? As the finance guy, he's going to eat all our inventory."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve
    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Hey now—I’d leave some... probably. Maybe. Don’t worry about it."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "Suki pauses."

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "On second thought. Let's have you scrubbing the toilets."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Wait—what?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Haha."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    "I can't help but laugh and smile."
    "The idea of us being free, still friends? I like that."
    "Even if part of me still thinks I’m exactly where I belong."

    hide char_l_idle with dissolve
    hide char_s_idle with dissolve
    hide char_t_idle with dissolve

    stop music fadeout 2.0

    scene bg_cafeteria2 at bg_scaled with dissolve

    play music "audio/Music/familiar.mp3" fadein 2.0

    "That alarm."

    "Breakfast is almost over. Five minute notice."

    "I finish up my tray and head to the trash can."

    "A few guys standing near me begin whispering."

    "I can't catch what they're saying."

    "But I can sense they’re planning something."

    "I think the guards can even sense it."

    "They've been staring at us harder than usual."

    "I hear a chair violently scrape against the floor."

    "Followed by a tray crashing down."

    show char_r_idle at t22 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t22 with dissolve

    r "The hell are you doing?! Outta my way."

    hide char_r_speak with dissolve
    show char_r_idle at t22 with dissolve

    "I knew that voice from anywhere."

    "It was Renn, one of the violent ones."

    "Last time someone mouthed off, Renn sent them to the infirmary."

    "Two broken ribs. I am not even sure if he was charged."

    show char_n_idle at t21 with dissolve

    "He had just knocked over Niko, circulation guy from earlier."

    "Both of their trays fell to the floor."

    "I could sense he was debating whether to pick it up or run the hell away."

    hide char_n_idle with dissolve
    show char_n_speak at t21 with dissolve

    n "Sorry— I didn't mea—"

    hide char_n_speak with dissolve
    show char_n_idle at t21 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t22 with dissolve

    r "Pick it up."

    hide char_r_speak with dissolve
    show char_r_idle at t22 with dissolve

    "Niko attempts to pick up Renn's dropped fork but slips in the process."

    hide char_r_idle with dissolve
    show char_r_speak at t22 with dissolve

    r "Come here, you little—"

    hide char_r_speak with dissolve
    show char_r_idle at t22 with dissolve

    "Renn lunges at him."

    "He grabs him with both hands and begins swinging on him."

    "I hear Niko's groans and panic."

    "The guards seriously not going to do anything?"

    "The other prisoners just watch."

    "They know not to mess with—"

    show char_t_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Hey!"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "I felt time stop."

    "My whole body went stiff."

    "What the hell is- Tomo- doing?"

    "I start heading back to our table."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Leave him alone!"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "His voice echoed in the now silent cafeteria."

    "Tomo grabs a handful of mashed potatoes and chucks it at Renn."

    "Did he seriously just—?"

    "Is he trying to get killed?"

    show char_l_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t22 with dissolve

    l "Tomo! Stop. What are you—?"

    hide char_l_speak with dissolve
    show char_l_idle at t22 with dissolve

    "Renn slowly wipes the food off his face."

    "He shifts focus on Tomo now."

    "Heading right toward our table."

    "I can see all of Tomo's courage instantly vanish."

    "Tomo gulps loud."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "I screwed up, didn't I..."

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t22 with dissolve

    l "You think?"

    hide char_l_speak with dissolve
    show char_l_idle at t22 with dissolve

    show char_s_idle at t33 with dissolve

    "Suki smiles, enjoying this way too much."

    "I see her prepare her tray."

    "Whatever is about to happen, she’s about to make it worse."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "So that was fun, right? You have to admit, great trajectory, solid impact—"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "Renn catches up to our table and grabs Tomo by the shirt."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Please don't kill me."

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "Suki leaps into action and slams her tray onto Renn's head."

    # [NOTE] Officer Reina should be added. Suggest introducing with idle pose at t11 with dissolve, then speak variant when grabbing.
    # [NOTE] Officer Maddox should be added. Suggest introducing with idle pose at t21 with dissolve, then speak variant when grabbing.

    "Officer Reina grabs Suki's hand."

    "Officer Maddox gets a hold of Renn."

    "My hands ball into fists without thinking."

    "Every part of me says move. Jump in. Do something."

    "I hear Renn land a brutal smack against Officer Maddox’s jaw."

    "The crack echoes across the cafeteria."

    "Shouts break out."

    "Guards move in, weapons drawn low, boots pounding against the floor."

    "I'm frozen."

    stop music fadeout 2.0

    scene bg_cafeteria_mess at bg_scaled with dissolve

    hide char_r_idle with dissolve
    hide char_s_idle with dissolve
    hide char_t_idle with dissolve
    hide char_l_idle with dissolve
    hide char_n_idle with dissolve


    "One wrong move... and it won't just be Suki or Tomo getting dragged off."

    "But I can’t just stand here."

    "I catch Suki out of the corner of my eye."

    "She jerks her arm free from Reina’s grip with a sharp twist, almost stumbling."

    "No hesitation. She's already sprinting."

    "Tomo tenses like he’s about to bolt."

    "I’m right there with him."

    "We tear out of there."

    "Pushing through the crowd."

    scene bg_hallway_escape at bg_scaled with dissolve

    "I'm breathing hard. I look back for a moment as I run."

    "The cafeteria's a mess—guards shouting, prisoners ducking, officers wrestling bodies to the ground."

    "I catch sight of two guys breaking off like we did."

    "Not toward the hallway cells like us."

    "Toward Tower A."

    "Looks like they were smart enough to leave too."

    "All three of us flee further into the hallways where we catch our breath."

    "I hear another soul panting next to us."

    play music "audio/Music/Office.mp3" fadein 2.0

    show char_n_idle at t21 with dissolve

    n "Hey."

    show char_t_idle at t22 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Oh—hey."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    "Just when I thought we had escaped it all."

    "Niko’s jumpsuit is all messed up from the beating."

    "I see him let out a nervous smile."

    hide char_n_idle with dissolve
    show char_n_speak at t21 with dissolve

    n "You were the one who helped me, right? Thanks for that."

    hide char_n_speak with dissolve
    show char_n_idle at t21 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Yeah. Of course."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    show char_s_idle at t33 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "You got hit pretty bad. You okay?"

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t21 with dissolve

    n "Yeah. I mean—I’m a healthy guy. Mostly. I’ll be alright."

    hide char_n_speak with dissolve
    show char_n_idle at t21 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Uh-huh... Well, Med-Bay by Cell Block C’s probably the least disgusting one. You know—if you start coughing up blood or something."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "I see him quiver at that thought."

    "He must hate blood or something."

    hide char_n_idle with dissolve
    show char_n_speak at t21 with dissolve

    n "Cool, cool. Good to know."

    hide char_n_speak with dissolve
    show char_n_idle at t21 with dissolve

    "All of his food was wasted when it was knocked over too."

    show char_l_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "If you're still hungry, they usually don’t check IDs in Cafeteria B. You might be able to grab a second tray. Looked like you lost yours after bumping into Renn."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t21 with dissolve

    n "Oh—right. Thanks. But I’m good."

    "I see him pause."

    n "And just for the record— I didn’t bump into him. He bumped into me."

    hide char_n_speak with dissolve
    show char_n_idle at t21 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Huh?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t21 with dissolve

    n "Wanted a reason to strike me, I guess."

    "So it was no accident."

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "What’d you do, insult his haircut?"

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_n_speak with dissolve
    show char_n_speak at t21 with dissolve

    n "I didn’t do anything. I barely even know the guy. I don’t know what that was. Just glad it’s over."

    hide char_n_speak with dissolve
    show char_n_idle at t21 with dissolve

    "You and me both, Niko."

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "I am glad too."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t21 with dissolve

    n "Anyway— I should go. I’m already late for chore rotation."

    hide char_n_speak with dissolve
    show char_n_idle at t21 with dissolve

    "I hear him groan as he shifts position to move."

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Right. Yeah, go ahead."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "See you around."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Don’t die or anything."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t21 with dissolve

    n "I’ll try not to."

    hide char_n_speak with dissolve

    "He seems alright."

    "But people like that? Getting into fights? Scary to know it can happen to anyone."

    # [Background Change Needed Here]

    "A radio crackles down the hall."

    "Heavy boots. Too steady to be an inmate."

    "Someone’s coming."

    hide char_l_idle with dissolve
    hide char_t_idle with dissolve
    hide char_s_idle with dissolve

    show char_l_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Come on, I hear someone. We should head for our chore rotation too."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "As I turn the corner, the someone in question is already in front of me."

    "Officer Amari... great."

    show char_a_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Nope. You're not going anywhere."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "You wanna tell me why I just got called off my route to the cafeteria?"

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "You heard about the brownies?"

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "Shut up, Suki."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Apparently the cafeteria's covered in mashed potatoes and eggs. With half of the east wing guards concussed."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Half? That sounds... bad."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "You don’t say."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Okay but like, technically—it wasn’t us. Not really."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Mhm. Yet you three came from that direction. And you match the description of one of the groups fighting."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "I mean..."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Tomo... Do I need to walk all the way to surveillance to pull the footage?"

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "You don’t. It was me. They actually weren't involved at all."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "Why do I do this to myself?"

    "Taking the blame yet again. I should shut up for once."

    "But I can't."

    "Suki and Tomo both turn toward me."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "You, Lune? Really?"

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "Officer Amari eyes me for a second, then exhales softly."

    "I could sense she was hoping this time would be different."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "That’s disappointing."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "Her disappointment always stung worse than getting yelled at."

    hide char_l_idle with dissolve
    show char_l_idle at t31 with dissolve

    "I stick my hands out before she even instructs."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Alright, Lune. With me. We’re having a talk."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "She clicks the cuff, then sets a hand on my shoulder."

    "We start to walk toward her office."

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Damn."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Hold on. Where are you taking him?"

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Office wing. You two—get to your rotations, now."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Be gentle with Lune. He screams if he sees rats."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "I glance back at them as I'm pulled away."

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "I’ll catch up. You guys go."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Come on. Eyes forward. You know the drill."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    hide char_s_idle with dissolve
    hide char_t_idle with dissolve
    hide char_a_idle with dissolve

    stop music fadeout 2.0

    scene bg_office_hallway at bg_scaled with dissolve

    play music "audio/Music/mystery.mp3" fadein 2.0


    "Here we go."

    "I hate these talks."

    "We walk in silence."

    "Her hand still resting heavy on my shoulder, not shoving, just guiding."

    "The office door creaks when she opens it."

    "I step inside."

    scene bg_office_interior at bg_scaled with dissolve


    "Metal table, two chairs. Smells like coffee in here."

    show char_a_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Hit that button as you step in."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "The button causes the heavy door to let out a hiss and shut violently behind us."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Sit."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "She leans against the desk instead of behind it. Arms crossed."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "You're almost out, you know. Just another couple months."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    show char_l_idle at t31 with dissolve

    "I nod, staring at a scuff mark on the floor."

    "I don’t like being reminded of when I am out of here."

    "I feel like I shouldn’t be free quite yet. Prison life is rough but I deserve it for what I did."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "I need you on your best behavior, Lune. I’d hate to write you up."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "I understand."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Reports of a brawl. Junior officer with a busted jaw. Surely that wasn’t you… was it?"

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "No, it-"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "I almost said Renn’s name."

    "But making an enemy isn’t worth it."

    "She observes me closely."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "What are you responsible for then?"

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "I just have to be upfront."

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "No real fighting like you were told. Just helping someone."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "So you were the one who threw the food at the inmates who were fighting?"

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Yes."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "I hate lying."

    "I feel like I am so bad at it."

    "Dammit Tomo."

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Just trying to stop it- to help…"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "She rubs her nose with the pinch of two fingers and sighs."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Look, I know you want to help. But there are people for that."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "People just watched. No guard stood up. Nothing."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "No one?"

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "None."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "I could tell that information bothered her."

    "Like she was yet again disappointed but now with her own people."

    "She adjusts her glasses to her eyes."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Even still. Getting involved like that... Could cost you your life."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    # --- Player Choice Inserted Here ---

    menu:
            "Stay defiant. I can handle myself.":
                $ trust["amari"] -= 1
                $ fear["amari"] += 1
                
                hide char_l_idle with dissolve
                show char_l_speak at t31 with dissolve

                l "I’ve made it this far, haven’t I?"

                hide char_l_speak with dissolve
                show char_l_idle at t31 with dissolve

                hide char_a_idle with dissolve
                show char_a_speak at t22 with dissolve

                a "Don't let pride be your downfall, Lune."

                hide char_a_speak with dissolve
                show char_a_idle at t22 with dissolve

            "Be quiet. Let her words sink in.":
                $ trust["amari"] += 1

                hide char_l_idle with dissolve
                show char_l_speak at t31 with dissolve

                l "..."

                hide char_l_speak with dissolve
                show char_l_idle at t31 with dissolve

                "I stay silent. Maybe because deep down, I know she's right."

                hide char_a_idle with dissolve
                show char_a_speak at t22 with dissolve

                a "Good. Think before you act next time."

                hide char_a_speak with dissolve
                show char_a_idle at t22 with dissolve

            "Admit you're scared.":
                $ trust["amari"] += 1
                $ fear["amari"] -= 1

                hide char_l_idle with dissolve
                show char_l_speak at t31 with dissolve

                l "I'm scared sometimes. I just don't want to show it."

                hide char_l_speak with dissolve
                show char_l_idle at t31 with dissolve

                hide char_a_idle with dissolve
                show char_a_speak at t22 with dissolve

                a "Fear isn’t weakness. It’s what keeps you alive."

                hide char_a_speak with dissolve
                show char_a_idle at t22 with dissolve

    "({color=#00FF00}Trust with Amari: [trust['amari']]{/color})"
    "({color=#FF0000}Fear with Amari: [fear['amari']]{/color})"

    # --- Story Naturally Continues Here ---

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Sometimes it's not about whether you can fight back. Sometimes it's about whether you even see it coming."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "...What do you mean?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "There was an inmate. About a year back. Most barely remembered her name. Quiet girl, red hair, kept to herself."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "She pauses for a second."

    "Where is this going?"

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "One morning, during early checks... She was found dead in her cell."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "My chest tightens."

    "Someone died in their cell? How does that even happen?"

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "The night before. The camera outside her cell… conveniently lost signal. Six minutes of static. Come to find her hours later with multiple stab wounds on the back of her head."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "The word sinks into my ribs like ice."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "I tried to help her. But by then, she was already gone."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "She was murdered."

    "In her cell."

    "Something’s wrong."

    "Red hair. Quiet. A year ago."

    "I swallow hard."

    show char_l_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "...Wait."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "That person... You're not talking about—"

    "Officer Amari watches me."

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Maika... are you?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Yeah. It was Maika."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "My heart hammers against my ribs."

    "I feel my cuffs bite into my wrists."

    "I didn’t even realize I was pulling against them."

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "But they said it was a heart attack."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "That's what they told the blocks. Easier that way. No investigations. No fear."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "She looks genuinely sorry."

    "This was the truth."

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "But she was murdered. She—"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "I can’t even finish."

    "It feels like the air’s been ripped out of the room."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "I'm sorry."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Why didn’t they say anything?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "Officer Amari’s mouth tightens."

    "The kind of silence that says everything."

    "Because they didn’t care."

    "She knew it."

    "I knew it too."

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "So that's just it?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "I fought to keep it from getting buried. Filed reports. Pushed for investigations. Nothing moved. No one followed up."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "I don't understand. Who would even want to hurt her? She didn’t do anything wrong. I mean... I know her crime was something petty."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Theft. Only supposed to be here for a few months. But that's exactly why you need to be careful, Lune. It doesn't matter who you are. Or how quiet you try to be. You're always at risk."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "She watches me, steady and serious."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "I don't want you ending up like her."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "I won’t let anything happen to me. Or my friends."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "The promise feels thin the second it leaves my mouth. But I mean it."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Good. Be smarter than most. Sometimes laying low isn't enough to survive. And clearly... some of my colleagues don't care enough to protect you."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "I shift slightly in my chair, the weight of it all pressing down harder."

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "So what should I do?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Keep your record clean. No strikes. No infractions. Keep your friends out of trouble, too. Just until you're out."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "And just hope for the best?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "A bitter edge slips into my voice."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Yes. That’s all you can do. Besides the expeditions."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "I blink at her."

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "The what?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Expeditions. Third-party work crews. Mining mostly. Some recon. Field jobs."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "She leans back, arms folding loosely — like she’s done explaining it a hundred times before."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Tough work. But constructed to shorten your sentences."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "Sounds dangerous."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "It can be. But some people say it’s better than sitting still and hoping nothing falls apart."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "I think I just want to finish my time naturally. But thank you for informing me of that."

    l "My friends loved them—"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    # [Background Change Here: Emergency Lighting]

    "A low whine cuts through the air."

    "The lights flicker — once, twice — before locking into a harsh, pulsing red."

    "Alarm."

    "A bad one."

    hide char_a_idle with dissolve
    show char_a_idle at t22 with dissolve

    "Officer Amari stiffens immediately."

    "Her radio crackles to life, static and overlapping voices shouting over each other."

    "\"Tower A breach confirmed—repeat, breach—multiple—\""

    "\"Shots fired—possible weapons drawn—\""

    "\"All available units—respond immediately—\""

    "I sit frozen."

    "It doesn’t even sound real."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Copy. Moving now."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "She turns to me, sharp and focused."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Stay here."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    l "But what about my friends—they are still…"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "I’ll find them. It’s safer in here than out here."

    hide char_a_speak with dissolve

    "She slams the button to open the door."

    "She’s gone before I can say another word."

    "The door hisses behind her as she leaves."

    play sound "audio/Atmosphere/aftermath.mp3"

    "I close my eyes."

    "Tomo."

    "Suki."

    "Where are they?"

    "Were they still near the cafeteria?"

    "Did they even make it to rotations?"

    "The alarm keeps pounding, bouncing off the walls, vibrating under my skin."

    "It’s louder when you’re stuck sitting still."

    "Feels like it's inside my bones."

    "My cuffs rattle against the table."

    "I lower my head."

    "Breathe."

    "Breathe."

    "But Maika’s face pushes through anyway."

    "She died."

    "Who's to say we aren’t next?"

    "I have to move."

    "I take off my shoe and reach for a lockpick I have been saving just in case."

    "I begin to fidget to get them off."

    show char_l_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve
    
    play sound "audio/Atmosphere/another.mp3"

    l "C'mon—c'mon…."

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    scene bg_empty_hallway at bg_scaled with dissolve

    "Open."

    "I slam the door open and step into the hall."

    "Empty."

    "I hear something."

    "Metal on concrete."

    "A distant yell, maybe."

    "Where the hell is everyone?"

    "I don't know where to go."

    "The shot I heard earlier—had to be the cafeteria."

    "I need to stay away from there."

    "I start moving. Fast."

    "All I can think about is Tomo and Suki."

    "Where they’d go."

    "Where they’d run."

    "I told them to head to rotation."

    "But if they bailed— they’d go to Suki's cell. No question."

    "I cut through the west wing and stop mid-sprint."

    "I can't believe what I'm seeing."

    scene bg_west_wing_blood at bg_scaled with dissolve

    "There's a smear of red splattered across the ground."

    "Something's definitely wrong."

    "A guard’s body is slumped against the wall."

    "Visor cracked."

    "Sidearm missing."

    show char_l_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t31 with dissolve

    play sound "audio/Atmosphere/blood.mp3"

    l "Officer. Can you hear me?"

    hide char_l_speak with dissolve
    show char_l_idle at t31 with dissolve

    "No response."

    "He’s out cold."

    "Officer's Radio" "Control is down—Tower A is compromised. Repeat—Tower A is—"

    "Static swallows the rest."

    "Loud, swift footsteps approach me."

    "I duck behind a supply rack."

    "Two inmates bolt past—laughing."

    "One’s carrying an assault rifle."

    "The other—some twisted piece of metal. Blood already on it."

    "They don’t see me."

    "Too busy chasing something else."

    "I'm almost at Suki's cell."

    "The gunshots echo louder with every turn."

    "Siri" "Please. I wasn't involved. Don't do this!"

    "I glance over. I've seen that inmate before… somewhere."

    "The officer slams a baton into her back."

    "Once. Then again."

    "What the hell."

    "I push forward."

    "Come on. Come on."

    "I hit the stairwell—"

    "Turn the corner."

    "I made it."

    "I hear a voice."

    "It’s Amari."

    show char_a_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Drop it, Renn."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    show char_r_idle at t33 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t33 with dissolve

    r "Hand it over."

    hide char_r_speak with dissolve
    show char_r_idle at t33 with dissolve

    "He lunges—"

    "Blade sinking into her side."

    "I freeze."

    show char_t_idle at t21 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t21 with dissolve

    t "Amari!"

    hide char_t_speak with dissolve
    show char_t_idle at t21 with dissolve

    "I glance right."

    "There they are."

    "Tomo’s pressed to the wall."

    show char_s_idle at t31 with dissolve

    "Suki grips a pipe with both hands."

    hide char_t_idle with dissolve
    show char_t_speak at t21 with dissolve

    t "He’s reaching for her gun!"

    hide char_t_speak with dissolve
    show char_t_idle at t21 with dissolve

    "Amari claws at Renn’s face—still standing. Barely."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Run!"

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    # --- Player Choice Inserted Here ---

    menu:
        "Rush forward to help Amari.":
            $ trust["amari"] += 1
            $ trust["tomo"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t31 with dissolve

            l "Hang on!"

            hide char_l_speak with dissolve
            show char_l_idle at t31 with dissolve

            "I lunge after them without thinking—heart hammering."

        "Focus on protecting Suki and Tomo.":
            $ trust["suki"] += 1
            $ trust["tomo"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t31 with dissolve

            l "Stay together—don't split!"

            hide char_l_speak with dissolve
            show char_l_idle at t31 with dissolve

            "I move toward them, but the chaos pulls me forward."

        "Hesitate, overwhelmed by panic.":
            $ fear["amari"] += 1
            $ fear["suki"] += 1
            $ fear["tomo"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t31 with dissolve

            l "..."

            hide char_l_speak with dissolve
            show char_l_idle at t31 with dissolve

            "My legs lock up—but instinct shoves me into motion."

    # Trust/Fear Display
    "({color=#00FF00}Trust with Amari: [trust['amari']]{/color})"
    "({color=#00FF00}Trust with Tomo: [trust['tomo']]{/color})"
    "({color=#00FF00}Trust with Suki: [trust['suki']]{/color})"
    "({color=#FF0000}Fear with Amari: [fear['amari']]{/color})"
    "({color=#FF0000}Fear with Tomo: [fear['tomo']]{/color})"
    "({color=#FF0000}Fear with Suki: [fear['suki']]{/color})"

    # --- Story Resumes  ---

    "I throw myself forward."

    "We all go down."

    hide char_t_idle with dissolve
    show char_t_speak at t21 with dissolve

    t "Lune!"

    hide char_t_speak with dissolve
    show char_t_idle at t21 with dissolve

    "He grabs my arm. Pulls."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "The gun—someone grab the gun!"

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    "I reach."

    "Renn grabs too."

    "Our hands collide—"

    "Gunshots crack."

    "One tears through my shoulder."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Don’t let him take it!"

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t33 with dissolve

    r "Get off!"

    hide char_r_speak with dissolve
    show char_r_idle at t33 with dissolve

    "He slashes at her."

    "Kicks Tomo back."

    "The gun fires until it’s clicking empty."

    "Renn slams me down, hard."

    "Hands around my throat."

    "He’s too heavy to push off."

    "I can't breathe."

    "I can’t—"

    show char_i_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t11 with dissolve

    i "Enough."

    hide char_i_speak with dissolve
    show char_i_idle at t11 with dissolve

    "Renn stops."

    "Everything stops."

    "A swarm of guards floods the hallway."

    scene bg_special_forces_arrival at bg_scaled with dissolve

    "I can barely see—the lights are too bright."

    "My body feels too heavy."

    hide char_i_idle with dissolve
    show char_i_speak at t11 with dissolve

    i "Restrain them."

    hide char_i_speak with dissolve
    show char_i_idle at t11 with dissolve

    "Guards tackle every prisoner in reach."

    "I catch a glimpse of Tomo slammed into the floor."

    "He groans, struggling."

    "Suki’s struck hard across the face, shoved into cuffs."

    "She’s still bleeding."

    hide char_r_idle with dissolve
    show char_r_speak at t33 with dissolve

    r "You don't know what you're stopping."

    hide char_r_speak with dissolve
    show char_r_idle at t33 with dissolve

    # [NOTE] Officer Vance should be added.
    "Officer Vance" "Silence."

    hide char_i_idle with dissolve
    show char_i_speak at t11 with dissolve

    i "Who do you think you are? You think this place owes you something?"

    i "You've proven me right. There’s no rehabilitation. Only punishment."

    i "My authority will not be challenged."

    i "Everyone here—Your sentence is now doubled. Minimum of 5 years extension."

    hide char_i_speak with dissolve
    show char_i_idle at t11 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t21 with dissolve

    t "Hey! Wait, we didn't do anything—"

    hide char_t_speak with dissolve
    show char_t_idle at t21 with dissolve

    hide char_l_idle with dissolve
    hide char_t_idle with dissolve
    hide char_s_idle with dissolve
    hide char_a_idle with dissolve
    hide char_r_idle with dissolve
    hide char_i_idle with dissolve



    "An officer, Maddox, strikes him, cutting him off."

    "Blood runs down my arm."

    "My shoulder won't stop bleeding."

    "My fingers are numb."

    "I can't feel my hand."

    "Suki’s voice sounds far away."

    "Tomo’s face—He’s saying something—"

    "...I can’t…"

    "I can’t tell where I am."

    "My eyes won’t open."

    "I just hear."

    "A soft beep."

    "I blink."

    stop music fadeout 2.0

    scene bg_medical_recovery at bg_scaled with dissolve


    "The light floods in—sharp, white."

    "Burns a little."

    "I hear a voice."

    show char_s_idle at t31 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "...Stop squirming. It’s just a little disinfectant. It’s disinfectant, not acid."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    show char_t_idle at t22 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "...It feels like both."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    show char_l_idle at t21 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "...Suki...?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "She jumps to my side."

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "You're awake, Lune."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    "His voice is still rocky."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "...Yeah. I’m here. I think. Where am I?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Medical."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "You were out for hours. We didn’t know if—You lost a lot of blood."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    "I see Tomo rubbing the scrape on his shoulder."

    "I was seriously out for that long?"

    "I hear medical staff passing by nearby."



    "Medic Rowan" "Vitals are stabilizing. Keep pressure on that side."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "You passed out right after they showed up. They rushed you straight here."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Are you guys okay?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "I look over."

    "Tomo’s got bruises and gauze taped across his arm."

    "Suki’s uniform is stained with something dark and dried."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "I got cut but it was nothing deep."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Bruised ribs. I think. Hurts to breathe a little."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "You were worse off than both of us. You didn’t even move when they dragged you out."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Feels like I got hit by a shuttle."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "My shoulder throbs."

    "I try not to wince."

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Could’ve been worse."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Yeah. Way worse. They say it was all planned."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "What?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "Renn. He was trying to distract the guards with the fights he started. So his guys could raid Tower A... full of firearms."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "They were trying to take everyone down in here. Take over the station. Steer it off course."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    "My stomach churns."

    "Those psychos were going to kill us all."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Jesus. That explains the fire. The desperate need to get a hold of everyone's weapons."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Yeah. It didn’t matter who you were. If you were in the way, you were dead."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "And we all got punished. For surviving."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Double sentences. Like we asked for any of this."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    "She looks down."

    "Doesn’t say more."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "I was supposed to be out soon."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t22 with dissolve

    t "I know..."

    hide char_t_speak with dissolve
    show char_t_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Me too."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "But we’re alive. We made it out. That has to count for something."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "They don’t answer right away."

    "But they don’t argue either."

    "I see a tear building on Tomo’s face."

    # --- Player Choice Inserted Here ---

    menu:
        "Try to comfort Tomo.":
            $ trust["tomo"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Hey... we’re still here. That has to mean something."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "I try to steady my voice. For him."

        "Stay quiet. Let him have his moment.":
            $ trust["tomo"] -= 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "..."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Some things... you can’t fix with words."

        "Change the subject. Lighten the mood.":
            $ trust["tomo"] += 1
            $ fear["suki"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "We should ask for hazard pay after all this."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Tomo almost smiles. Suki doesn’t."

    # Trust/Fear Display
    "({color=#00FF00}Trust with Tomo: [trust['tomo']]{/color})"
    "({color=#00FF00}Trust with Suki: [trust['suki']]{/color})"
    "({color=#FF0000}Fear with Suki: [fear['suki']]{/color})"

    # --- Story Resumes Here ---

    "I force myself to look at it positively but I can't take this anymore."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "I need to check on someone. Make sure she’s okay."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "I shift, pulling my legs over the side of the bed."

    "My shoulder burns hot."


    "I leave to look for Amari."

    
    hide char_s_idle with dissolve
    hide char_t_idle with dissolve

    scene bg_medical_far_wing at bg_scaled with dissolve

    "I ask where she is."

    "I make my way to the far bay."

    "They said she was stable. That’s all they knew."

    "The walk hurts."

    "But I keep going."

    "I reach the room."

    "She’s propped up on the bed."

    "Her side wrapped tight."

    "Pale, but alert."

    show char_a_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "...You shouldn’t be up."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Neither should you."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "She gives a weak smile."

    "I sit beside her."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Are you okay?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Better now. The meds are strong."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "I'm sorry for what happened."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "I can't look her in the eye."

    "I feel a sense of responsibility over her injuries."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "You were right. This place... it’s not safe. I should have stopped him sooner. Should have seen it coming."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "She doesn’t answer right away."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "You don’t need to be sorry. You helped your friends. You helped me. That matters."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "We barely got out. I feel unsafe. For them. And now that we got the time extensions, I—"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "I know. I know. I'm sorry. I tried to talk with Commander Iven. He was strict about it."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Nothing we can do?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "I want to say there is, but there isn't."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "I think back to what she told me."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "What about... the expeditions? You told me that’s always an option."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "It is, but after what happened today... Commander Iven has closed down any more sign-ups."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Will there be any more?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "I don't know. I'm sorry, Lune."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "It's okay. I'll just... Keep my eye out."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "She looks at me."

    "There's a sad look on her face."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Look, the next expedition is going to be a mining expedition. Maybe I can talk to one of our cave operators, Cale. I can have him convince Commander Iven that we might need a few more people on board."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "You would do that?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "I would. It would be you and the two others, right?"

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Yeah. Yeah, thank you."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Just sign yourself up. There's a sheet in my bag. If you're serious. Sign yourself up and be ready. I won't wait on you."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Okay. Thanks. For everything."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve
    
    scene bg_prison_cell at bg_scaled with dissolve

    "I go back to my cell for the rest of the day."

    "I wait and rest."

    "The day moves slow."

    "Evening hits."

    "Lights dim."

    "I hear my cell door unlocking."

    show char_a_idle at t22 with dissolve

    "Officer Amari stands outside."

    "Clipboard in hand."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "It’s time."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "I can't believe it."

    show char_s_idle at t31 with dissolve
    show char_t_idle at t33 with dissolve

    "Suki and Tomo are waiting down the hall."

    "Still in uniform."

    "Still unsure."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "What’s going on?"

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "Are we in trouble?"

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    show char_l_idle at t21 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "No. I signed us up."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "They look at each other."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "...For what?"

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "A contract expedition. We’re leaving tonight."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Those expeditions that reduce time?"

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Yes."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "Wait—for real?"

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "You—when did you even—"

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Amari got us in. Said she could talk to someone. We got the green light."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "You're serious."

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Yeah. Grab your stuff. We're going."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "Tomo opens his mouth like he’s about to say something."

    "Then closes it."

    "Just follows."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Okay, but what kind of expedition is this?"

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    "I pause."

    "Then tell her."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Mining."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "She stops walking."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Mining? Like—actual, hauling-rocks-from-a-cave mining?"

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Yeah."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "You can barely move your arm."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "I’ll manage."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "She stares at me."

    "Not angry. Just... worried."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "You sure?"

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    # --- Player Choice Inserted Here ---

    menu:
        "Reassure her with confidence.":
            $ trust["suki"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Positive. I’ll be fine."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "I try to keep my voice steady—even if my shoulder throbs."

        "Be honest about your doubts.":
            $ trust["suki"] += 1
            $ fear["suki"] -= 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "No. But staying here's worse."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Her eyes soften slightly."

        "Brush it off with humor.":
            $ fear["suki"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Maybe they’ll let me mine one-handed."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "She snorts, but the worry doesn't really leave her face."

    # Temporary Trust/Fear Display
    "({color=#00FF00}Trust with Suki: [trust['suki']]{/color})"
    "({color=#FF0000}Fear with Suki: [fear['suki']]{/color})"

    # --- Story Resumes Smoothly Here ---

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve


    l "Come on. Let’s head to the dock."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve
    hide char_a_idle with dissolve
    hide char_s_idle with dissolve
    hide char_l_idle with dissolve
    hide char_t_idle with dissolve


    scene bg_space_dock at bg_scaled with dissolve
    
    "We all begin to move."

    "The docks stretch out in front of us."

    "Steel and cold floodlights."

    "A fleet of low-hauler ships — blunt, utilitarian, nothing elegant about them — sits humming on their pads."

    "Engines thrumming low, almost a growl."

    "We fall into line with the others."

    "Dozens of inmates."

    "All in identical roughcut uniforms — names faded, boots scuffed, hopes even worse."

    "They process us fast."

    "Scan our wristbands."

    "Check our vitals."

    "Hand out thin oxygen packs and worn duffel bags, barely big enough to carry more than a spare jumpsuit and a pair of gloves."

    "I tighten my grip on mine."

    "The ship we’re assigned to — Unit 12A — is a battered old model."

    scene bg_unit12a_interior at bg_scaled with dissolve

    "We head to our cabins and sleep. This is the best sleep I think I’ve had in years."

    "I wake up to the sounds of our shuttle like I have been for the past two weeks."

    "I was lucky enough to share living quarters with the other two for the entire trip."

    "It was fun, and exciting. A break from everything."

    "I know today is the day."

    "We finally land."

    scene bg_ship_descent at bg_scaled with dissolve

    "Muffled shifts rumble through the ship’s gravity systems."

    "We’re entering orbit."

    "A low chime rings over the intercom."

    "No alarm."

    "Just a notice."

    "\"All hands prepare for atmospheric descent.\""

    "I move toward the nearest viewing port."

    "Barely a window — more like a thick-glass slit wedged between armor panels."

    "But it’s enough."

    "Outside—the planet spins slowly beneath us."

    "It’s beautiful."

    "Clouds curling soft and pale over deep oceans."

    "Wide sweeps of green."

    "Mountains stitched across the horizon like dark threads."

    "Sunlight spilling over everything — bright, clean, untouched."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "...Weird. It actually looks... nice."

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    show char_s_idle at t33 with dissolve

    "Suki presses against the glass too, elbowing him lightly."

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "First rule of survival: if it looks that pretty, it probably wants to kill you."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "I almost laugh."

    "Almost."

    "But she’s right."

    "We’re not here to hike trails or swim oceans."

    "We’re here for the caves."

    "The dark."

    "The things buried under all that beauty."

    "The ship tilts gently — adjusting angle."

    "The view shifts."

    "From forested stretches to jagged rocky regions — gray bluffs like old bones poking through the skin of the planet."

    "Mining zones."

    "Marked even from orbit."

    "Suki shifts her weight uneasily."

    "Still not saying much."

    "Still bouncing one knee against the floor."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Hey, Lune. You think... after all this... maybe we get to stay here?"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "What, retire on a hostile rock?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "Tomo shrugs."

    "Half-joking."

    "Half not."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Better than Astraea."

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    # --- Player Choice Inserted Here ---

    menu:
        "Agree with him — anything is better than Astraea.":
            $ trust["tomo"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Honestly? I'd take a rock over that hellhole any day."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Tomo grins, small but real."

        "Stay cautious — nowhere is truly safe.":
            $ fear["tomo"] += 1
            $ trust["suki"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Doesn’t mean it’s safe. Pretty places kill you the same as ugly ones."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Suki nods slightly, like she agrees."

        "Say nothing — focus on the mission.":
            $ trust["suki"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "..."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "No point dreaming yet. We haven’t earned it. But if things work out maybe."

    # Trust/Fear Display
    "({color=#00FF00}Trust with Tomo: [trust['tomo']]{/color})"
    "({color=#00FF00}Trust with Suki: [trust['suki']]{/color})"
    "({color=#FF0000}Fear with Tomo: [fear['tomo']]{/color})"

    # --- Story Resumes Here ---

    "Another chime sounds."

    "Sharper this time."

    "\"All surface teams report to bay deployment zones. Final gear checks. Planetfall in T-minus ten minutes.\""

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "..."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "Suki tugs her gloves tighter."

    "Tomo checks the seals on his oxygen pack."

    "I pull my gear into place, feeling the weight settle onto my shoulders."

    "Helmet clipped loose at my belt."

    "Pouch secured."

    "Minimal supplies."

    "No real protection."

    "I glance back out the window."

    "The planet spins — green, gold, and blue like a living painting."

    "Beautiful."
    "Alive."

    "And somewhere down there our job waits for us."

    "Our saving grace to freedom."

    scene bg_landing_zone at bg_scaled with dissolve


    "The landing wasn’t as bad as I thought."

    "Rough, sure — engines shrieking, hull rattling — but we made it in one piece."

    "The bay doors grind open."

    "Heat rushes in."

    "Not burning."

    "But warm."

    "Alive."

    "Outside—a bright, wide plain stretches toward a line of thick woods."

    "Grass waves in the wind."

    "Real grass."

    "Golden, tall, almost reaching our knees."

    "The sky is sharp blue."

    "Clouds move fast above us, dragged by unseen currents."

    show char_t_idle at t31 with dissolve

    "Tomo steps down first, boots crunching into the dirt."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Not dead yet. Good start."

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    show char_s_idle at t33 with dissolve

    "Suki follows, adjusting her pack."

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "Give it five minutes."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "I step down last."

    "The ground feels strange after so long in artificial gravity."

    "Lighter."

    "Springy, almost."

    "The guards fall into position fast—"

    "Black-suited, helmets down, visors opaque."

    "Professional."

    "Efficient."

    "No shouting."

    "No panic."

    "Just tight hand signals and sharp commands."

    "One of them — a senior officer, judging by the red stripe on her arm — steps forward."

    "Officer Brynn" "Surface Divisions, listen up. Assignments incoming. Standard formation: eight per team division. One commanding officer, one junior officer, one engineer, six contract workers."

    "Contract workers."

    "That’s what we are here I guess."
    
    "Not inmates."

    "Not prisoners."

    "Just numbers attached to labor."

    # --- Player Choice Inserted Here ---

    menu:
        "Feel relieved — at least it’s better than prison.":
            $ fear["tomo"] -= 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Better a number than a prisoner."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Tomo seems to relax just a little."

        "Feel bitter — it’s just another kind of cage.":
            $ fear["tomo"] += 1
            $ trust["suki"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Doesn't matter. We're still stuck."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Suki's mouth tightens slightly in agreement."

        "Stay silent and focused.":
            $ trust["suki"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "..."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "There's no use complaining. Not now."

    # Trust/Fear Display
    "({color=#00FF00}Trust with Tomo: [trust['tomo']]{/color})"
    "({color=#00FF00}Trust with Suki: [trust['suki']]{/color})"
    "({color=#FF0000}Fear with Tomo: [fear['tomo']]{/color})"

    # --- Story Resumes Here ---

    "Another officer reads off names."

    "Tomo gets paired with me and Suki."

    "Just as Amari promised."

    "We've clung together this long."

    scene bg_assignment_field at bg_scaled with dissolve

    "Our assigned commanding officer steps forward."

    show char_i_idle at t22 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "..."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "Commander Iven."

    "I recognize him immediately."

    "The one who signed off on the sentence extensions after the riot."

    "The one who turned months into years with the flick of a pen."

    "My jaw tightens."

    "I force my hands to stay loose at my sides."

    "Suki shifts slightly beside me — not saying anything, but her mouth presses into a thin line."

    "Tomo looks down at his boots like he’s trying not to explode."

    "Figures."

    "We finally get a shot at freedom, and he’s the one holding the leash."

    "And standing just behind him—"

    show char_a_idle at t11 with dissolve

        
    play sound "audio/Atmosphere/nature.mp3"

    "Amari."

    "Wearing expedition gear now."

    "Same calm eyes."

    "Same quiet presence."

    "She catches my gaze for a second."

    "I nod."

    "She nods back."

    "Some promises are harder to keep than others."

    "But she’s here."

    "Watching over us."

    "A man with a company logo on his shirt approaches."

    show char_c_idle at t33 with dissolve

    "Cael."

    hide char_c_idle with dissolve
    show char_c_speak at t33 with dissolve

    c "I’m Cael. You three—Lune, Suki, Tomo—you’re in my division."

    hide char_c_speak with dissolve
    show char_c_idle at t33 with dissolve

    "I guess this green-haired guy is our engineer."

    "This is the one Amari told us about."

    "The one that got us in."

    "Cael begins listing other names — a \"Veyla\" and..."

    "Two more names hit my ears wrong."

    "Niko."

    "And Renn."

    show char_n_idle at t31 with dissolve
    show char_r_idle at t33 with dissolve

    "I see Niko waving awkwardly from a few rows down, trying to look casual and failing miserably."

    "Renn just grins slow and ugly when he catches me looking."

    "Not good."

    "I left the station to avoid people like you."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Move."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "Commander Iven calls us over with a short wave."

    "He barks that we should follow every step he asks of us."

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    s "..."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    "Suki mutters under her breath as we shoulder our gear and move."

    "We fall into step."

    "Nine of us total, marching out across the field."

    call hide_all_characters

    scene bg_march_to_river at bg_scaled with dissolve

    "The air smells different out here."

    "Sharp."

    "Fresh."

    play sound "audio/Atmosphere/nightbefore.mp3"

    "No metal, no cleaning chemicals."

    "Just sun-baked grass and something sweeter drifting off the trees."

    "The officers keep the pace steady but not brutal."

    "No one's screaming at us."

    "No one's waving guns."

    "They’re serious—"

    "But it’s a professional seriousness, not cruelty."

    show char_c_idle at t22 with dissolve

    "Cael checks a small scanner strapped to his wrist as we move."

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "River’s about half a click east. Cave system’s across it."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    "I glance sideways at Suki."

    show char_s_idle at t31 with dissolve

    "It’s nice to see us not be cuffed as hard out here."

    "We can move our hands freely."

    "She’s watching the trees carefully, one hand hovering near her belt knife."

    show char_t_idle at t33 with dissolve

    "Tomo’s scanning the sky — like he expects something to swoop down and grab him."

    "I can’t blame them."

    "The beauty here feels... fragile."

    "Like the world is wearing a skin too thin to trust."

    "The field gives way to thicker brush."

    "We push through dry reeds and low shrubs—"

    "Boots snapping twigs, packs rattling softly."

    "In the distance, I hear it first—"

    "A soft rush."

    "Water."

    "The river."

    scene bg_riverbank at bg_scaled with dissolve
        
    play sound "audio/Atmosphere/nature2.mp3"

    "We break through the last line of trees."

    "And there it is."

    "Wide and fast, cutting through the land like a silver knife."

    "The water glints hard in the sun—fast-moving, but shallow enough we could probably ford it if we had to."

    "Beyond it—"

    "The ground rises into sharp cliffs."

    "Dark openings yawn along the rock face."

    "Mouths of the caves."

    "Waiting."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Stay alert. We wait for Division 2. Our partnering group to catch up."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    show char_v_idle at t11 with dissolve

    "The girl that was called earlier, the other inmate, Veyla, scribbles notes into a datapad, mumbling to herself."

    "I’ve never seen her on the station before."

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    "Cael kneels to check soil readings — probably making sure we don’t pitch camp on a sinkhole."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    "Tomo dumps his pack onto the ground and flops down beside it, exhausted."
    "Suki stands by the riverbank, arms crossed, staring at the caves."

    # --- Player Choice Inserted Here ---

    menu:
        "Crack a joke to lighten the mood.":
            $ trust["suki"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Bet you five credits there's nothing worse than bad air in there."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Suki snorts, almost smiling."

        "Voice your concerns seriously.":
            $ trust["tomo"] += 1
            $ trust["suki"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Stay sharp. First steps inside could be a mess."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Tomo straightens up slightly."

        "Say nothing. Keep tension bottled up.":
            $ fear["suki"] += 1
            $ fear["tomo"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "..."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "The silence weighs heavier."

    #  Trust/Fear Display
    "({color=#00FF00}Trust with Tomo: [trust['tomo']]{/color})"
    "({color=#00FF00}Trust with Suki: [trust['suki']]{/color})"
    "({color=#FF0000}Fear with Tomo: [fear['tomo']]{/color})"
    "({color=#FF0000}Fear with Suki: [fear['suki']]{/color})"

    # --- Story Resumes Here ---

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "The entrances don't look welcoming."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "They’re not supposed to be. But it's only temporary"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "The river hums in my ears."

    "The sun beats steady on my back."

    "The caves loom across the water."

    scene bg_riverbank_staging at bg_scaled with dissolve

    "We bunch up near the riverbank, adjusting packs, double-checking gear."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Standard protocol. You're entering Section 7-B of the cave system. First sweep is exploration. No mining until tunnels are secured. One week rotation."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "Stay together. No stragglers. No shortcuts. Log findings. Report hazards immediately."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    "Tomo adjusts his pack, falling into step beside me."

    t "...You know... I was thinking about it last night. If we pull this off—We can become free. One week of work should be more than enough!"

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    "He smiles — a little crooked, a little forced — but real."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Someone’s feeling optimistic."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "Well, can you blame me? You two dragged me out of a life sentence. I'm not screwing it up."

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Your nerd self does not have a life sentence. Stop trying to act tough."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    "He laughs — a quick, nervous sound."

    "But it's real."

    "No bitterness."

    "Just nerves under hope."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Just know, if you screw it up, I'm taking your rations."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "You'd do that anyway."

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    show char_n_idle at t11 with dissolve

    "Niko adjusts his oxygen pack nervously."

    hide char_n_idle with dissolve
    show char_n_speak at t11 with dissolve

    n "...Are there... like, wild animals in there?"

    hide char_n_speak with dissolve
    show char_n_idle at t11 with dissolve

    show char_r_idle at t33 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t33 with dissolve

    r "Only the ones that used to be people."

    hide char_r_speak with dissolve
    show char_r_idle at t33 with dissolve

    "Niko goes pale."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    "Iven ignores them."

    i "Division 2 has breached section 6. We are behind schedule now. Move fast."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    scene bg_cave_entrance at bg_scaled with dissolve

    "The crew starts filing into the cave."

    "Boots clanging against stone."

    "Lights flickering on their helmets."

    hide char_s_idle with dissolve

    "Suki disappears into the dark first."

    hide char_t_idle with dissolve

    "Tomo follows."

    hide char_r_idle with dissolve

    "Even Renn, muttering something under his breath."

    hide char_v_idle with dissolve

    hide char_n_idle with dissolve

    hide char_i_idle with dissolve

    hide char_a_idle with dissolve


    "Veyla hangs back a second longer than the others — quiet, scribbling notes into her pad — then vanishes into the dark too."

    "I glance back at Cael."

    show char_c_idle at t22 with dissolve

    "Still setting something up."

    "If I’m going to talk to him — this is my only chance."

    hide char_l_idle with dissolve
    show char_l_idle at t21 with dissolve

    "I shoulder my pack tighter and step toward him."

    scene bg_cave_edge at bg_scaled with dissolve
    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Hey. Cael, right?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "The one and only."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "I'm Lune. Well, prisoner 218. I just... wanted to thank you. In person."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Thank me?"

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Officer Amari told me about you making space for us. For me and my friends. I know you had to pull some strings for it to happen. You didn’t even know me, but you did it anyway. I wanted to thank you for that."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "Cael smirks lightly."

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "I'm kidding. I know this whole sentence reduction thing is really important to some of you. Amari told me good things. And well... I trust her."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "I see. Well—thank you again. For everything."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Just promise me you put in that hard work, yeah? We got a lot of ground to cover. And a lot of resources to gather. It’ll be fun."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Most certainly. I'll try my hardest."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Well great, because—"

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    "The radio crackles loud."

    "Radio" "Cave technician blue, come in, over."

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "This is CT Blue, reporting, over."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    "Radio" "We’re going to need those charges set up by T-minus five. We need to have everything established by 0600 hours. Over."

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Dispatch, I need two people to man the charges. I need CT Orange over here. Over."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    "Only static answers back."

    "Cael mutters under his breath."

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Damn it."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Is everything okay?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Yeah. That damn engineer from Division Two—he’s always wandering off. He might already be in the cave."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "If you need two people, maybe I can help."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "That's okay, kid. I'll just take the strike on my record. I'll find that damn guy and face the consequences of being late."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "I mean it. I can help you. Just like you helped me. I'm a quick learner—I promise."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "Cael pauses—then grins a little."

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "You mean it? Well, alright. It is pretty simple after all, so just follow my instructions and you’ll be fine."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Got it."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "Cael pulls a small handheld device from his belt."

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Alright—you’re going to want to hold this charge here, place it directly on that marker there, and set the timer to 2.15."

    "He holds it up—small, square, heavy."

    c "Make sure it’s 2.15. Not 215. We don’t want you blowing off your hands like the last guy."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Like the last what—?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "I'm kidding."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    "He smirks again."

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Once you have that set, on my mark, you hit that big red button. Got it?"

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "The red button. Okay. Red button."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Ready?"

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Ready."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Three, two, one. Press."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    "I press the button."

    "The charge beeps quietly."

    "Locking into place."

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Well, look at you. Certified engineer. Not too bad. Thanks, kid."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    "He claps me lightly on the back."

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Let's go now and catch up with the others."

    play sound "audio/Atmosphere/breathing1.mp3"

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    scene bg_cave_worksite at bg_scaled with dissolve

    "The cave’s cooler than the surface."

    "Dry air, dust kicking up with every step."

    "Echoes chase every sound down the stone corridors."

    "We spread out in sections, assigned dig points."

    show char_s_idle at t31 with dissolve
    show char_t_idle at t33 with dissolve
    show char_r_idle at t22 with dissolve
    show char_n_idle at t11 with dissolve

    "Suki kneels near a jagged wall, using a portable sonic chisel — a sleek, black tool that vibrates at a high frequency to fracture rock cleanly."

    "Tomo fumbles with a gravity sifter — a compact machine that pulls lighter minerals into collection bags while heavier rubble drops straight through."

    "It hums and whirs like an overeager vacuum cleaner."

    "Renn is further down, taking broad, reckless swings with his manual breaker — a brute-force drill that judders with every strike."

    "He's already cracked two tools."

    "Niko... Niko's staring at his assignment — a deep crack in the wall — like it personally offended him."

    hide char_n_idle with dissolve
    show char_n_speak at t11 with dissolve

    n "Okay but like... what if something’s living in there?"

    hide char_n_speak with dissolve
    show char_n_idle at t11 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Then tell it we’re unionizing."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "I don’t think rocks care about workers’ rights."

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    "I dig my sonic chisel into the wall carefully."

    "Press, hold, crack."

    "Press, hold, crack."

    "Thin veins of mineral glint under the dust."

    "It's hard work."

    "Sweaty."

    "Repetitive."

    "But real."

    "Every shard we pull — every bag we fill — shaves off time."

    "Earns freedom."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Hey, Lune."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    "She wipes dust off her face with the back of her sleeve."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "You ever think about what you'll do first? When you're out?"

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    # --- Player Choice Inserted Here ---

    menu:
        "Stay hopeful — dream about the future.":
            $ trust["suki"] += 1
            $ trust["tomo"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Yeah. A real home. No guards. No cages."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Suki’s smile grows a little wider."

        "Stay grounded — focus on survival first.":
            $ trust["cael"] += 1
            $ trust["amari"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "One step at a time. We survive this first."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Amari nods slightly, approving."

        "Stay detached — don’t think that far ahead.":
            $ fear["niko"] += 1
            $ fear["suki"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "No point dreaming. Things happen."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Niko shifts awkwardly nearby."

    # Trust/Fear Display
    "({color=#00FF00}Trust with Suki: [trust['suki']]{/color})"
    "({color=#00FF00}Trust with Tomo: [trust['tomo']]{/color})"
    "({color=#00FF00}Trust with Cael: [trust['cael']]{/color})"
    "({color=#00FF00}Trust with Amari: [trust['amari']]{/color})"
    "({color=#FF0000}Fear with Suki: [fear['suki']]{/color})"
    "({color=#FF0000}Fear with Niko: [fear['niko']]{/color})"

    "I crack another section loose."

    "Toss it into my collection bin."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Actually, maybe get a place with real windows. A real bed."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "Suki grins."

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "I’m buying a stupidly expensive coffee machine. One of the ones that costs more than rent."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "I'm going to build a server rack. Big enough to crash local networks."

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t11 with dissolve

    n "I'm gonna... uh... sleep for like a month."

    hide char_n_speak with dissolve
    show char_n_idle at t11 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t22 with dissolve

    r "...I’m gonna find whoever built this station and punch 'em."

    hide char_r_speak with dissolve
    show char_r_idle at t22 with dissolve

    "Sweat drips down my neck."

    "My arms are starting to ache."

    "Not used to this kind of grind."

    "But it’s... satisfying, in a way."

    "Real work."

    "Real results."

    scene bg_cave_mining_site at bg_scaled with dissolve

    "Then — without warning — a soft chime sounds from the overhead speakers wired into the portable base we left outside the cave."

    "Not an alarm."

    "Not danger."

    "A calm tone."

    "Three rising notes."

    show char_c_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Alright, Surface Team Beta — drop your tools. Lunch rotation starts now."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    show char_t_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Saved by the bell."

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    show char_s_idle at t33 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    "Suki leans back on her heels, flexing her sore fingers."

    s "I could kiss that speaker."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    show char_n_idle at t11 with dissolve

    "Niko wipes dust off his face, grinning like he just survived a war."

    show char_r_idle at t22 with dissolve

    "Even Renn straightens up slightly — grumbling, but moving toward the exit."

    "I drop my chisel, rolling my shoulders out."

    "Muscles ache in ways I didn’t even know existed."

    scene bg_cave_break_chamber at bg_scaled with dissolve

    "We pull back to a widened chamber deeper inside the cave."

    "Not far — just far enough that the walls don't press so close around us."

    "The mining gear gets stacked to the side."

    "Dust still hangs low in the air, clinging to everything."

    "Lunch crates get cracked open on a smooth stretch of rock."

    "Quick, efficient."

    "No fancy setup — just finding a spot to sit and breathe."

    "I drop down next to Suki, brushing grit off my pack before sitting on it."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    "Tomo’s already passing out ration packs like it’s a holiday."

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "And honestly?"

    "Compared to Astraea Prime?"

    "It kind of is."

    "The protein breads are soft, dense with actual flavor."

    "The drinks are citrusy and cold from portable coolers."

    hide char_s_idle with dissolve
    show char_s_speak at t33 with dissolve

    "Suki bites into hers and lets out a sigh so exaggerated it makes Tomo laugh."

    s "This is it. This is peak civilization."

    hide char_s_speak with dissolve
    show char_s_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "I might cry."

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t11 with dissolve

    "Niko unwraps his meal slowly, like he’s worried it’ll vanish if he moves too fast."

    n "I don't mind this. I am happy."

    hide char_n_speak with dissolve
    show char_n_idle at t11 with dissolve
    "Amari sits cross-legged near the cluster of crates."

    show char_a_idle at t22 with dissolve

    "Polished, calm, perfectly at ease in the cave gloom."

    show char_s_idle at t31 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Alright, Officer Sunshine. Story time. You owe us."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Not a mining job. Survey contract."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    show char_t_idle at t33 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "Survey? Like... old wreckage?"

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "Colony ruins. Dead world. Lot of sandstorms. Old structures barely standing."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Sounds cooler than rocks and pickaxes."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    "Amari shrugs, almost smiling."

    hide char_a_idle with dissolve
    show char_a_speak at t22 with dissolve

    a "It wasn’t bad. Until the storms."

    hide char_a_speak with dissolve
    show char_a_idle at t22 with dissolve

    "She leans back slightly, tapping a knuckle against her canteen."

    "The cave hums around us."

    "The faint tremor of machines deeper in the tunnels."

    "Division 2’s equipment, probably."

    "They're already ahead of us."

    "Pushing further into the dark."

    "We’re supposed to rendezvous with them soon."

    "Expand the dig."

    "Amari shifts slightly, about to say something else."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "I'm sorry to cancel the party so early, but—that storm outside that's approaching? We don't want to be trapped in here. It's best we start wrapping things up."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t22 with dissolve

    r "Seriously? We're leaving so... soon?"

    hide char_r_speak with dissolve
    show char_r_idle at t22 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "Can't believe I'm agreeing with this brute, but it's true. We were promised weeks in here. Not a few days."

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "I say good riddance. I feel myself getting more gross every minute I stay in here."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "We made good progress, team. Let's take our winnings and go. The station beds don't seem that bad just about now."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "Hmm. A nap doesn't sound too bad."

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Come on, Tomo—you'll be fortunate enough to carry my bags out of the cave."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "Right..."

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Haha."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t22 with dissolve

    r "What's the deal, huh? You seriously think we can't handle a little storm? We have enough supplies to last through it—and then some."

    hide char_r_speak with dissolve
    show char_r_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "I know. It's just... In good conscience, I can't continue the operation. Safety first, you know."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t22 with dissolve

    r "You're not in charge. You don't have that authority to make that call for us."

    hide char_r_speak with dissolve
    show char_r_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "I—"

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "He may not have the authority. But I do. And we are leaving. You have one hour to pack your stuff and record all of your earnings."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "We will still honor the progress you have made thus far and apply reduction amounts."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t31 with dissolve

    n "Can we at least get, like, extra for this? I mean—I wouldn't have signed up if I knew it was only for a few days!"

    hide char_n_speak with dissolve
    show char_n_idle at t31 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Don't test our generosity here. You are fortunate that we even gave you this opportunity."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "There will be more opportunities. Don't you all worry. We usually have one every five years."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t22 with dissolve

    r "Five years? You think I'm going to wait that long? You know how long I'm sentenced for?"

    hide char_r_speak with dissolve
    show char_r_idle at t22 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Don't make me pull out my baton, 829. You will do as instructed and start heading toward the exit with your belongings."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "I'm trying to do the math in my head."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "I think we made enough that I get about a year left."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "I think I get about nine months left."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "That makes me so happy. What about you, Tomo?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "He already went to go get my bags. I saw him go that way."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "The poor kid. Haha."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Relax, relax. He'll get a brownie the moment we're back on the station."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Hey, Lune. Sorry about the short trip. Do you think you got enough time off?"

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    # --- Player Choice Inserted Here ---

    menu:
        "Stay optimistic — be proud of the work.":
            $ trust["cael"] += 1
            $ trust["suki"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Yeah. We worked hard and earned it. Proud of everyone."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Cael nods approvingly."

        "Voice disappointment — wish you had more time.":
            $ trust["renn"] += 1
            $ fear["amari"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Wish we could've done more. It feels... unfinished."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Renn chuckles low, but Amari watches quietly."

        "Focus only on survival — staying alive matters more.":
            $ trust["amari"] += 1
            $ trust["veyla"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Doesn’t matter. We’re alive. That’s what counts."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Amari’s eyes soften slightly."

    # Temporary Trust/Fear Display
    "({color=#00FF00}Trust with Cael: [trust['cael']]{/color})"
    "({color=#00FF00}Trust with Suki: [trust['suki']]{/color})"
    "({color=#00FF00}Trust with Renn: [trust['renn']]{/color})"
    "({color=#00FF00}Trust with Veyla: [trust['veyla']]{/color})"
    "({color=#00FF00}Trust with Amari: [trust['amari']]{/color})"
    "({color=#FF0000}Fear with Amari: [fear['amari']]{/color})"

    # --- Story Resumes Here ---

    hide char_l_idle
    hide char_c_speak

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Yeah. Surface readings say level 10. Visibility zero. Wind-force might hit 110 miles per hour if it keeps escalating."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Yeah. Surface readings say level 10. Visibility zero. Wind-force might hit 110 miles per hour if it keeps escalating."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "I get it. You're looking out for us. Thank you."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "Attention! I need all metal equipment in these containers! Make sure to separate them based off of—"

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    call hide_all_characters
    
    play sound "audio/Atmosphere/caveexplosion.mp3"

    "AAHH!!"

    "I—I can’t see anything, it’s all dust!"

    "...eughhhh."

    l "Suki?! Tomo?! Where are you—say something!"

    l "I feel so heavy, I can't—I can't move. Help! Hello? Anybody? Please!"

    l "Please!"

    hide char_n_idle with dissolve
    show char_n_speak at t31 with dissolve

    a "...Niko? Niko, look at me. Breathe. You're okay."

    hide char_n_speak with dissolve
    show char_n_idle at t31 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t31 with dissolve

    n "I can't feel my arm."

    hide char_n_speak with dissolve
    show char_n_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Amari!"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "Lune! Oh my goodness—he’s stuck! Tomo, shine the light this way, he’s over here—come help me lift this."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "Lune! I'm here, I'm here!"

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    a "On three. One—two—three."

    "They lift."

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "Are you okay, sweetie?"

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Thank you. I think so. What the hell was that?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "I don't know. Is anything broken? Can you walk?"

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "I can walk. I can walk."
    
    play sound "audio/Atmosphere/crumble1.mp3"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "Are you okay, Lune? Was Suki with you?"

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "No, she wasn’t."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Cael! What the hell was that?!"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "Ow... ugh..."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Cael."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t22 with dissolve

    c "I—checking the readings—agh—now on my device."

    hide char_c_speak with dissolve
    show char_c_idle at t22 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    play sound "audio/Atmosphere/crumble2.mp3"

    i "Amari, search for the rest. Start taking head count and see if anyone's injured."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t31 with dissolve

    r "The hell kind of mining job is this?"

    hide char_r_speak with dissolve
    show char_r_idle at t31 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Quiet."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "777... 801... 218... 447..."

    a "Where’s the girl?"

    play sound "audio/Atmosphere/cavenormal.mp3"

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Yeah, where’s Suki?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_v_idle with dissolve
    show char_v_speak at t31 with dissolve

    v "I last saw her by the supply kits. Over there."

    hide char_v_speak with dissolve
    show char_v_idle at t31 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "On it."

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    "Tomo rushes ahead, kicking up dust with every step."

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "Suki?! Suki, where are you—?"

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    "I stumble after him, lungs burning from the dust."

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "I see her!"

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    "She's crumpled near the jagged wall, half-buried under a collapsed supply shelf."

    "A gash runs across her temple, bleeding into her hairline."

    "Tomo drops to his knees beside her."

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "She's breathing! She's breathing!"

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    "Officer Amari is right behind us, already pulling medical gloves from her pack."

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "Clear back—let me through."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    "I freeze — watching her work."

    "Suki's face is pale."

    "Her breaths shallow."

    "One of her arms lies at an odd angle."

    "Officer Amari checks her pulse, her airway — fast, efficient."

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "Stable, but unconscious. Possible concussion. Fractured arm at minimum."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    "Tomo runs a shaking hand through his hair."

    t "Is she gonna be okay?"

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "I don't know yet."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    "I kneel beside Suki — not touching — just close enough that if she wakes up, she'll know we’re here."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Form up! Secure the injured! We’re falling back to the secondary shelter point!"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "Cael limps over, clutching his side."


    "The dust is finally starting to settle."

    scene bg_cave_camp_postcollapse at bg_scaled with dissolve

    play sound "audio/Atmosphere/cavewater.mp3"

    "Pale light from the portable rig throws long shadows across the broken ground."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Cael. Status."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "It seems to—it seems to have come from the stabilizer line by the entrance. The charges must’ve gone off."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Charges?"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "They're stabilizer charges. Shock absorbers. Low potency. Barely enough to shake dust off the beams."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Low? That felt like a blast to me."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "I know. I don't quite understand it yet. They were set to 2.15. And that sure as hell didn't feel like a 2.15. Something must have amplified the blast."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Are you sure you set them to 2.15?"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "I can assure you I did. We both did."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Both?"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Yeah—well, me and... the kid."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_v_idle with dissolve
    show char_v_speak at t31 with dissolve

    v "Hmm."

    hide char_v_speak with dissolve
    show char_v_idle at t31 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "What kid?"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Well—"

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t33 with dissolve

    n "Are we sure that it's done? Can anyone confirm this place won't still collapse on our heads?"

    hide char_n_speak with dissolve
    show char_n_idle at t33 with dissolve

    # --- Player Choice Inserted Here ---

    menu:
        "Stay calm — reassure everyone it'll be okay.":
            $ trust["niko"] += 1
            $ trust["veyla"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "If it was gonna fall again, we'd know by now. We're good."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Niko visibly relaxes a little."

        "Stay tense — warn them to stay ready for anything.":
            $ trust["amari"] += 1
            $ trust["cael"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Stay alert. This might not be over yet."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Amari nods grimly."

        "Stay silent — keep your doubts to yourself.":
            $ fear["niko"] += 1
            $ fear["veyla"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "..."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "The silence makes the tension worse."

    # Temporary Trust/Fear Display
    "({color=#00FF00}Trust with Niko: [trust['niko']]{/color})"
    "({color=#00FF00}Trust with Veyla: [trust['veyla']]{/color})"
    "({color=#00FF00}Trust with Amari: [trust['amari']]{/color})"
    "({color=#00FF00}Trust with Cael: [trust['cael']]{/color})"
    "({color=#FF0000}Fear with Niko: [fear['niko']]{/color})"
    "({color=#FF0000}Fear with Veyla: [fear['veyla']]{/color})"

    # --- Story Resumes Here ---

    hide char_v_idle with dissolve
    show char_v_speak at t31 with dissolve

    v "Truth is, we don’t know the severity of the damage yet."


    hide char_v_speak with dissolve
    show char_v_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "Commander. 369 is still alive... that's all of us."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Good. Division 1 is accounted for."

    i "What about Division 2, Cael?"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "I have no readings. I lost signal with them."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    scene bg_cave_partial_collapse at bg_scaled with dissolve

    "Commander Iven straightens, scanning the battered team around him."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Change of priorities. This operation’s scrapped. We find Division 2. We secure any survivors. Then we get the hell out."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "We’re leaving?"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "We're not risking more casualties. Not without knowing what we're dealing with."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "I shift uneasily — looking back at the route we came through."

    "Broken."

    "Collapsed."

    "Heavy stone and twisted metal choking the entire passageway."

    hide char_n_idle with dissolve
    show char_n_speak at t33 with dissolve

    n "Uh... Commander? I don't think we're leaving that way."

    hide char_n_speak with dissolve
    show char_n_idle at t33 with dissolve

    "We all turn."

    "The entrance — gone."

    "Not just damaged. Gone."

    "Crushed under tons of debris."

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    "Amari steps forward, running her scanner slowly across the blockage."

    a "Structural collapse. Full obstruction. Estimated depth — minimum thirty meters."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "...Thirty meters?"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "He sits down hard on a nearby crate."

    hide char_v_idle with dissolve
    show char_v_speak at t31 with dissolve

    v "Not diggable without heavy machinery. Which we do not have."

    hide char_v_speak with dissolve
    show char_v_idle at t31 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Alternative exits?"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "Cael adjusts a portable relay dish he's been fiddling with near the center of the camp."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "There are auxiliary tunnels deeper inside. Surface breaks in certain sectors."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Good. Chart a route."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "Cael holds up a hand — calm, steady."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Already working on it. But listen—"

    "He taps the side of his wrist console, flashing a holographic display."

    "A tiny blinking signal pulses faintly."

    c "I triggered an emergency beacon. Set to bounce off the planetary satellites. Backup’s already been called."

    "He looks around — meeting everyone's eyes slowly."

    c "It'll take a while, but they'll come. We've just gotta hold out."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    "Tomo looks over at Suki’s stretcher — at the small rise and fall of her chest under the emergency blanket."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "But what about her?"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    "Amari answers gently."

    a "Best thing we can do is keep her stable. Moving her too much could make it worse."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_v_idle with dissolve
    show char_v_speak at t31 with dissolve

    v "Assuming there’s no second blast."

    hide char_v_speak with dissolve
    show char_v_idle at t31 with dissolve

    "Nobody says anything to that."

    "Cael crouches by the fireless heater we set up, checking the power cells."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Look. I’ve been on expeditions where comms cut out. Where routes collapsed. It's scary. But it’s survivable. You just have to think smart, move smart, and not panic."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    "His voice is calm."

    "Grounded."

    "Something solid to hold onto."

    "For now."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Alright. Everyone rest up. Regroup. We move once the scans are done. Even if it takes days."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "Tomo drags a hand down his face, exhausted."

    "Niko curls tighter into his jacket."

    "I sit down heavily, feeling the cold of the cave seep through my clothes."

    "The lights from the portable rigs flicker gently across the rocky walls."

    scene bg_cave_shelter_night at bg_scaled with dissolve

    "We take shifts sleeping that day."

    "Two on watch at all times."

    "Suki sleeps fitfully — murmuring sometimes under her breath."

    "Tomo refuses to move far from her."

    "The rest of us take turns dozing against the cold rock walls, huddled in thin blankets."

    "The cave hums around us — alive with distant echoes, groaning under its own weight."

    "But no more blasts. No more collapses."

    "Just waiting."

    "Day three."

    "Still no backup."

    "The beacon Cael set up still blinks patiently."

    "Still transmitting."

    "But nobody’s answering."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Could be storm interference. Or dust in the upper atmosphere. Or... or maybe it just takes longer out here."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    "Nobody says what we’re all thinking."

    "Maybe no one’s coming."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    "Commander Iven calls us into a loose circle."

    i "We’ve waited long enough."

    "He glances at each of us — dust-streaked, exhausted, bruised."

    i "Division 2’s last known path ran along Sector 6C. If they're alive, they're deeper inside."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_v_idle with dissolve
    show char_v_speak at t31 with dissolve

    v "And if they're dead?"

    hide char_v_speak with dissolve
    show char_v_idle at t31 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    "Iven doesn't flinch."

    i "Then we find another way out."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    "Tomo glances at Suki — still sleeping lightly under her emergency blanket."

    t "She can't move far. Not yet."

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    "Cael taps his console again, grimacing."

    c "We could rig a lightweight sled. Make it easier to transport her if needed."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t31 with dissolve

    "Niko shifts uneasily, picking at the cuff of his jacket."

    n "...We don't even know if there's a way out."

    hide char_n_speak with dissolve
    show char_n_idle at t31 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Staying still isn’t safer forever either. If pressure builds wrong in these chambers, we’re sitting ducks."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    # --- Player Choice Inserted Here ---

    menu:
        "Speak up carefully — suggest that moving might be smarter than waiting.":
            $ trust["cael"] += 1
            $ trust["amari"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Maybe... maybe Cael's right. Sitting here feels like a death sentence too."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

        "Stay quiet — let the officers debate it out.":
            $ fear["iven"] -= 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "..."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "Better not to get involved. Let the officers figure it out."

        "Privately whisper to Tomo that you don't trust Cael's judgment.":
            $ trust["tomo"] += 1
            $ fear["cael"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Keep your eyes open. I don't trust his math either."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

    "({color=#00FF00}Trust with Cael: [trust['cael']]{/color})"
    "({color=#00FF00}Trust with Amari: [trust['amari']]{/color})"
    "({color=#FF0000}Fear with Iven: [fear['iven']]{/color})"
    "({color=#00FF00}Trust with Tomo: [trust['tomo']]{/color})"
    "({color=#FF0000}Fear with Cael: [fear['cael']]{/color})"

    # --- Main Story Resumes Normally Here ---

    "Silence."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "We hold another night. One more."

    "He looks toward Cael."

    i "If no word by morning, we move."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "Cael nods — slow, reluctant."

    "Everyone starts settling back down — silent agreements made."

    scene bg_cave_shelter_night_later at bg_scaled with dissolve

    "We cluster near the heaters again, under the flicker of portable lamps."

    "Tomo wraps Suki’s blanket tighter around her."

    "Veyla returns to her datapad, checking radiation levels and oxygen readings."

    "Niko dozes lightly, boots still laced, ready to bolt if needed."

    "I lean my head back against the stone wall. Let my eyes drift shut."

    "It’s not real sleep."

    "Just a thin, fraying thread of rest."

    scene bg_cave_disturbance at bg_scaled with dissolve

    "My sleep is interrupted by shouting."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Which one of you was it! Which one of you laid their fingers on me."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "Commander, I had them cuffed all night."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "I told you to keep watch while I slept."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "I did. I was awake the entire time, I promise. I wasn’t going to let anyone hurt each other. There’s no one that could have done that."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Look at me. I'm going to need stitches for this."

    a "I—I don't know how that—"

    i "If I find you conspiring with them, it won’t end well for you."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "Me? Why would I—"

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Enough. I know it was one of them. They will have to learn not to test their boundaries with me."

    i "Cael. Hand me the key."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Here."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "You all lose your dinner now. While you sit there with your empty stomachs, you think twice about testing me."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t31 with dissolve

    n "You can't do that."

    hide char_n_speak with dissolve
    show char_n_idle at t31 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Excuse me?"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t31 with dissolve

    n "You can't. I counted the rations. We only have about a week left of food. You starting to take control over it just—"

    hide char_n_speak with dissolve
    show char_n_idle at t31 with dissolve

    hide char_v_idle with dissolve
    show char_v_speak at t33 with dissolve

    v "I was awake. Not a single person moved in his direction. What I think is that he carved that wound himself."

    hide char_v_speak with dissolve
    show char_v_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "What? Why would he carve himself?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_v_idle with dissolve
    show char_v_speak at t33 with dissolve

    v "Exactly for this result. He wants an excuse to control the food."

    hide char_v_speak with dissolve
    show char_v_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "I don't like this."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "Cael—you have to believe me. I didn’t fall asleep. I made sure everyone stayed sleeping."

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "I know, Amari. I don’t know what could have happened. The last few days have everyone on edge. Let's just focus on riding it out."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "It’s okay, Suki. I still have this granola bar for you. I had it in my pocket since yesterday. You can have it."

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_s_idle with dissolve
    show char_s_speak at t31 with dissolve

    s "Thanks, Tomo."

    hide char_s_speak with dissolve
    show char_s_idle at t31 with dissolve

    "She seems quieter than usual."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "You can't what, huh?"

    "Commander Iven immediately pulls out his nail baton."

    i "You try to tell me what I can and cannot do?"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "Niko immediately shuts down, frozen in fear."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "I’m in charge here. I want to hear you say it."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t31 with dissolve

    n "You're... you're in charge."

    hide char_n_speak with dissolve
    show char_n_idle at t31 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "I want to hear all of you say it."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    # --- Player Choice Inserted Here ---

    menu:
        "Obey calmly — signal to the others to stand down too.":
            $ trust["tomo"] += 1
            $ trust["suki"] += 1
            $ trust["amari"] += 1

            $ fear["tomo"] += 1
            $ fear["suki"] += 1
            $ fear["amari"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "You're in charge, Commander."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

        "Comply but glare at him — let him know you’re not broken.":
            $ trust["renn"] += 1
            $ fear["iven"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "You're in charge. For now."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

        "Refuse to speak — a quiet act of defiance.":
            $ trust["veyla"] += 1
            $ fear["iven"] += 2
            $ trust["renn"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "..."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "I don't say it. He can force the words, but not the meaning."

    "({color=#00FF00}Trust with Tomo: [trust['tomo']]{/color})"
    "({color=#00FF00}Trust with Suki: [trust['suki']]{/color})"
    "({color=#00FF00}Trust with Amari: [trust['amari']]{/color})"
    "({color=#00FF00}Trust with Renn: [trust['renn']]{/color})"
    "({color=#00FF00}Trust with Veyla: [trust['veyla']]{/color})"
    "({color=#FF0000}Fear with Iven: [fear['iven']]{/color})"

    # --- Main Story Resumes Normally Here ---
    hide char_l_idle with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t33 with dissolve

    r "F*** you."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t33 with dissolve

    r "F*** you."

    hide char_r_speak with dissolve
    show char_r_idle at t33 with dissolve

    "Commander Iven points the nail end of the baton right between Renn’s eyes."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "You think I'm playing?"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    a "Commander, please—"

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "You're in charge, Commander. You’ve made that clear. They won't question it."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Maybe I should make an example out of one of you. Is that what it will take?"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t33 with dissolve

    t "Please—we get it. You’re in charge."

    hide char_t_speak with dissolve
    show char_t_idle at t33 with dissolve

    hide char_r_idle with dissolve
    show char_r_speak at t33 with dissolve

    r "Yeah... You're in charge."

    hide char_r_speak with dissolve
    show char_r_idle at t33 with dissolve


    scene bg_cave_tense_watch at bg_scaled with dissolve

    "A noise cuts through the standoff."

    "Footsteps."

    "Fast."

    "Erratic."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    "Commander Iven snaps his head toward the tunnel mouth."

    i "...What the hell was that?"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    play sound "audio/Atmosphere/mystery2.mp3"

    "We all turn — scanning the darkness beyond the edge of the portable lights."

    "Another noise — heavier this time."

    "Boots slamming against stone."

    "Suki flinches on her stretcher."

    "Tomo instinctively shifts closer to shield her."

    "Niko scrambles to his feet, pale and blinking."

    "Veyla narrows her eyes, already pulling her scanner."

    "Renn cracks his knuckles."

    hide char_r_idle with dissolve
    show char_r_speak at t31 with dissolve

    r "...That ain’t one of ours."

    hide char_r_speak with dissolve
    show char_r_idle at t31 with dissolve

    scene bg_cave_mouth_dark at bg_scaled with dissolve

    "From the shadows — a figure emerges."

    "Slim. Fast. Moving low."

    "A gas mask gleams under the rig lights — reflective eyes cold and unreadable behind tinted lenses."

    "Breathing tubes clack faintly as he moves."

    "He doesn't run toward us."

    "He bolts across the cavern mouth — vanishing deeper into the tunnels."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Who the hell—?"

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Cael. Veyla. Lune. With me."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "We move quickly — gear rattling, boots grinding against loose stone."

    "Amari stays back by Suki, hand hovering near her sidearm."

    "We move into the tunnel cautiously — light beams sweeping across rough walls and scattering dust."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Be careful!"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "We push forward — down a narrow throat of stone."

    hide char_v_idle with dissolve
    show char_v_speak at t33 with dissolve

    "Veyla’s datapad beeps quietly, searching for heat signatures."

    v "No Division 2 tags. That’s not one of ours."

    hide char_v_speak with dissolve
    show char_v_idle at t33 with dissolve

    "Cael adjusts the charge pack strapped across his back — grim determination etched into every step."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "This planet was supposed to be abandoned. No colonies. No locals."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Then who the hell is that?"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "We round another corner — and there he is."

    "The masked man."

    play sound "audio/Atmosphere/breathing1.mp3"

    "Standing just beyond the light — breathing hard, head tilted slightly toward us."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    "Cael steps forward cautiously — hands raised slightly."

    c "Hey. We're not here to hurt you. Are you hurt? Do you need help?"

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    "The masked figure says nothing. Doesn't move."

    "For a second — I think maybe he’s frozen. Maybe he’s scared."

    "And then — he moves."

    "Fast."

    "He swings something up from behind his back — a gleaming, battered mining pick."

    "The head arcs through the air — aiming straight for Cael’s skull."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Shit—!"

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    "Commander Iven’s weapon is up immediately."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Drop it! Drop it now!"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "The masked man doesn’t obey."

    "He spins — disappearing back into the tunnels with terrifying speed."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "After him!"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "We break into a run — lights bouncing wildly against the cave walls."

    "But he's fast. Way too fast."

    "Within seconds — he's swallowed by the dark. Gone."

    "We slow — breathing hard, weapons still raised."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Damn it."

    play sound "audio/Atmosphere/madness.mp3"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "Veyla taps her datapad furiously, trying to track anything — but the tunnels are a maze, twisted and dense."

    hide char_v_idle with dissolve
    show char_v_speak at t33 with dissolve

    v "Nothing. He's gone."

    hide char_v_speak with dissolve
    show char_v_idle at t33 with dissolve

    "Cael rubs the side of his head — wincing at how close the swing came."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "If I hadn't ducked—"

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    "He doesn’t finish the sentence."

    "None of us say anything."

    "We just stand there — hearts pounding in the heavy dark — staring into the tunnels."

    "Because now?"

    "Now we know."

    "We aren't alone down here."


    scene bg_cave_after_chase at bg_scaled with dissolve

    "We move back fast — boots crunching against loose stone, breath clouding the cold air."

    "No sign of the masked man."

    "Nothing but echoes chasing us back to the temporary shelter."

    "The others look up as we appear — eyes wide, tense."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    "Commander Iven is already snapping orders."

    i "Perimeter secure. Double watches starting now."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "He stalks toward the portable heater, barking more instructions."

    "I drop next to Tomo and Suki — still out cold, twitching now and then in her sleep."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    "Tomo leans close."

    t "What the hell happened?"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "We saw someone. Gas mask. Fast."

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    hide char_v_idle with dissolve
    show char_v_speak at t33 with dissolve

    "Veyla crosses her arms, datapad hugged tight against her chest."

    v "Not one of ours. Not Division 2."

    hide char_v_speak with dissolve
    show char_v_idle at t33 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    "Cael runs a hand through his hair — stopping to wince at the scrape where the pickaxe nearly caught him."

    c "He went for my head. No warning."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Maybe he’s the one who cut Commander Iven."

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    hide char_v_idle with dissolve
    show char_v_speak at t33 with dissolve

    "Veyla nods slightly."

    v "Fits the timeline. Someone slipped in during the night. Sabotaged the beacon. Marked the Commander."

    hide char_v_speak with dissolve
    show char_v_idle at t33 with dissolve

    hide char_n_idle with dissolve
    show char_n_speak at t31 with dissolve

    "Niko fidgets by the supply crates, glancing nervously at every shadow."

    n "Was he... living down here?"

    hide char_n_speak with dissolve
    show char_n_idle at t31 with dissolve

    "Nobody answers."

    "Nobody knows."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    "Commander Iven steps toward us, growling low."

    i "Doesn’t matter who he is. If he’s down here — we’ll find him."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "He glares at all of us like we’re somehow to blame."

    "I force myself to look away — back toward Suki."

    "She stirs again. Breath hitching."

    "Tomo notices too."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Hey—Suki? You awake?"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "Suki's eyes snap open."

    "Wild. Unfocused."

    "And then—she screams."

    "Not a startled gasp. Not a pained cry."

    "A raw, throat-tearing scream."

    "So loud the walls seem to vibrate with it."

    "She thrashes violently — arms flailing, legs kicking — almost throwing herself off the stretcher."

    "Tomo leaps back, nearly falling over."

    hide char_a_idle with dissolve
    show char_a_speak at t11 with dissolve

    "Officer Amari bolts forward, trying to pin her down gently."

    a "Suki! Suki, it’s okay — it’s okay, you’re safe!"

    hide char_a_speak with dissolve
    show char_a_idle at t11 with dissolve

    "Suki doesn't hear her."

    "Her face is twisted in terror — mouth open wide — screaming, screaming, screaming."

    "Her body convulses like something invisible is trying to rip its way out of her."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Restrain her! Now!"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "I scramble forward — helping Amari and Tomo hold her down without hurting her."

    "Her hands claw at the air. At her own throat. Like she’s trying to tear something off of herself that none of us can see."

    "Niko is frozen in place — staring, horrified."

    "Veyla grabs the portable med kit — ripping it open, searching for a sedative."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Suki — Suki, please—!"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "She gasps violently, arching off the stretcher — eyes rolling back."

    "Amari manages to inject her — a fast, hard stick of the needle into her upper arm."

    "For a moment — nothing changes."

    "The screaming doesn’t stop."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Suki! Please—please, just open your eyes!"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "I scramble for the water kit — hands slipping on the cold casing."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "She’s hallucinating—she’s shaking, hard. Someone help me—she’s going to seize!"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "Cael dives toward us, scanner in one hand, medpack in the other."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Hold her steady! I’m checking vitals—!"

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve


    "Cael dives toward us, scanner in one hand, medpack in the other."

        # --- Player Choice Inserted Here ---

    menu:
        "Stay at Suki's side — try to steady her through it.":
            $ trust["suki"] += 2
            $ trust["tomo"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "You're okay, Suki. We're right here. Just hold on."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "I press my hand over hers — keeping her grounded, feeling her fingers twitch under mine."

        "Step back — let Cael and Amari handle the medical emergency.":
            $ fear["suki"] += 2
            $ trust["cael"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "I'll clear space—I'm in the way."

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

            "I stumble back, heart hammering, letting the professionals work."

        "Snap at Niko — force him to move and help instead of freezing up.":
            $ trust["amari"] += 1
            $ fear["niko"] += 1

            hide char_l_idle with dissolve
            show char_l_speak at t21 with dissolve

            l "Niko—don't just stand there! Help steady her legs!"

            hide char_l_speak with dissolve
            show char_l_idle at t21 with dissolve

    "He doesn't move."

    "({color=#00FF00}Trust with Suki: [trust['suki']]{/color})"
    "({color=#00FF00}Trust with Tomo: [trust['tomo']]{/color})"
    "({color=#FF0000}Fear with Suki: [fear['suki']]{/color})"
    "({color=#00FF00}Trust with Cael: [trust['cael']]{/color})"
    "({color=#00FF00}Trust with Amari: [trust['amari']]{/color})"
    "({color=#FF0000}Fear with Niko: [fear['niko']]{/color})"

    # --- Main Story Resumes Normally Here ---

    "Suki convulses harder — her legs kicking so violently it almost knocks the medpack out of Cael’s hands."

    scene bg_cave_full_collapse at bg_scaled with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "It has to be from malnutrition. Commander Iven, we need to treat her—this isn’t sustainable."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    "Commander Iven barely glances at us — his voice cold and sharp."

    i "She's faking it."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "I freeze."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Faking it? Do you hear these screams? She’s spasming!"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "Suki bucks violently against the stretcher — limbs thrashing."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Amari—get her head elevated. I’ll grab water from the kit."

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t33 with dissolve

    a "On it."

    hide char_a_speak with dissolve
    show char_a_idle at t33 with dissolve

    "Tomo presses Suki’s shoulders down — tears glimmering in his wide eyes."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "You’re okay, Suki. I’ve got you—it’s just a bad dream... stay with me."

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "Amari cradles Suki’s head carefully — trying to stop it from slamming into the rock."

    hide char_a_idle with dissolve
    show char_a_speak at t33 with dissolve

    a "I need help keeping her still! Lune, hold her legs!"

    hide char_a_speak with dissolve
    show char_a_idle at t33 with dissolve

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Holding!"

    play sound "audio/Atmosphere/failure.mp3"

    "I grab her calves — but her body is burning hot, convulsing uncontrollably."

    l "Her body’s burning up real bad. She's—"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "Suki’s mouth snaps open— and a guttural, monstrous scream tears out."

    hide char_s_idle with dissolve
    show char_s_speak at t11 with dissolve

    s "GRRRRRRRRRROWAAAAAAAAAAAAAAHHHHHHHHHH!!"

    hide char_s_speak with dissolve
    show char_s_idle at t11 with dissolve

    "The sound doesn’t even sound human."

    hide char_v_idle with dissolve
    show char_v_speak at t33 with dissolve

    "Veyla steps back sharply, her face blank but wary."

    v "That. That sound came out of her."

    hide char_v_speak with dissolve
    show char_v_idle at t33 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "I'll shine the light your way, Amari. Assess the situation."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    hide char_a_idle with dissolve
    show char_a_speak at t33 with dissolve

    a "I don't know what's— she's kicking hard!"

    hide char_a_speak with dissolve
    show char_a_idle at t33 with dissolve

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "Strap her down. Or let her burn herself out."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "The words hit like a slap."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Burn herself out—?! Are you insane?!"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Commander, stand down. We need her alive—!"

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    scene bg_cave_fight_breaks_out at bg_scaled with dissolve

    "I see something move quick."

    "Renn moves. Fast."

    "Too fast for anyone to react."

    "He lunges at Commander Iven — grabbing the baton at his belt — ripping it free."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "—gh!"

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "Renn whirls, tossing the baton to Niko — who catches it instinctively, eyes wide in terror."

    hide char_r_idle with dissolve
    show char_r_speak at t31 with dissolve

    r "Help me! Now!"

    hide char_r_speak with dissolve
    show char_r_idle at t31 with dissolve

    "Niko freezes."

    "Renn shoves him roughly."

    hide char_r_idle with dissolve
    show char_r_speak at t31 with dissolve

    r "You wanna die in here? Starving? Getting picked off one by one?! Move!"

    hide char_r_speak with dissolve
    show char_r_idle at t31 with dissolve

    "Niko moves — hesitant, clumsy — but he swings."

    "The baton glances off Commander Iven’s arm — enough to drive him back a step."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    t "Suki’s still seizing! Forget him—someone help her!"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "I drop the water kit — lunging back toward the stretcher."

    "Amari struggles to keep Suki’s head stable — blood leaking from her bitten lip."

    hide char_a_idle with dissolve
    show char_a_speak at t33 with dissolve

    a "She’s going into full seizure! I need restraints — now!"

    hide char_a_speak with dissolve
    show char_a_idle at t33 with dissolve

    "Cael ducks a wild swing from Commander Iven — slamming his medpack against the cave wall for support."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Enough! We can’t fight each other—we’ll all die if we keep this up!"

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    "Veyla stays at the edge of the light — silent, unreadable, watching everything unfold."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "I have the water— Amari, here—!"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "I toss the kit toward her."

    "She catches it one-handed — barely — while still cradling Suki."

    "Renn wrestles Iven toward the cave wall — gritting his teeth."

    hide char_r_idle with dissolve
    show char_r_speak at t31 with dissolve

    r "You wanna starve us?! Beat us?! Not today!"

    hide char_r_speak with dissolve
    show char_r_idle at t31 with dissolve

    "Niko stands awkwardly nearby — still clutching the baton, shaking."

    "Commander Iven roars — throws Renn off with a brutal shove."

    "The two of them stagger apart — both breathing hard, bloody and furious."

    hide char_c_idle with dissolve
    show char_c_speak at t11 with dissolve

    c "Enough! Everyone stand down!"

    hide char_c_speak with dissolve
    show char_c_idle at t11 with dissolve

    "For a second — a fragile, shaking second — nobody moves."

    scene bg_cave_supernatural_event at bg_scaled with dissolve

    "For one second — everything is still."

    "Suki lies limp on the stretcher. Chest heaving. Face twisted in pain."

    "Tomo leans over her — whispering her name over and over, voice shaking."

    "And then— she rises."

    "Not by sitting up. Not by pushing herself up."

    "Her entire body lifts."

    "Straight off the stretcher."

    "Hovering."

    "The air crackles. The lamps flicker violently — shadows lurching against the cave walls."

    "A guttural noise rips out of Suki's mouth — low and wet and impossible. Like a dozen voices twisting together."

    hide char_t_idle with dissolve
    show char_t_speak at t31 with dissolve

    play sound "audio/Atmosphere/hellish.mp3"

    t "Suki—?"

    hide char_t_speak with dissolve
    show char_t_idle at t31 with dissolve

    "Officer Amari lunges forward instinctively, reaching to pull her down — but stops short."

    "Frozen."

    "Helpless."

    "Commander Iven raises his weapon slightly — but even he hesitates."

    "Because none of us — none of us — know what the hell we’re looking at."

    "The air feels wrong."

    "Heavy. Pressurized. Sick."

    scene bg_cave_renns_betrayal at bg_scaled with dissolve

    "And in the chaos — Renn moves."

    "Fast."

    "He darts toward Cael's dropped belt — snatching the supply crate key from its clipped ring."

    hide char_l_idle with dissolve
    show char_l_speak at t21 with dissolve

    l "Renn—! What are you—?!"

    hide char_l_speak with dissolve
    show char_l_idle at t21 with dissolve

    "But he’s already gone."

    "Slipping past us — dodging hands — tearing deeper into the tunnels."

    "Gone."

    "Taking the only food security we had left with him."

    "Commander Iven reacts fast."

    "He rounds on Niko — grabbing him by the jacket and slamming him hard against the cave wall."

    hide char_i_idle with dissolve
    show char_i_speak at t22 with dissolve

    i "You were with him. You helped him."

    hide char_i_speak with dissolve
    show char_i_idle at t22 with dissolve

    "Niko stammers — panicking — but it doesn’t matter."

    "Iven cuffs him fast — slapping on a restraining clamp from his belt kit."

    "Niko doesn’t fight."

    "Doesn’t even try."

    "He just slumps against the wall, panting, eyes huge and glassy."

    "Suki floats there — still."

    "The noises she makes are softer now — a low, rattling breathing that doesn’t match anything human."

    "The light above us buzzes — and then stabilizes."

    "She's still in the air."

    "Then slams to the ground."

    "Still unconscious — or maybe not. I can’t tell anymore."

    "None of us can."

    "The group regathers slowly — shellshocked. Broken."

    "Tomo kneels near Suki, not touching her, just watching."

    play sound "audio/Atmosphere/lostsouls.mp3"

    return