##  RPG fight

# Random Number Generator
label dice_roll:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return

## BATTLE
label battle:
    ## initialise variables
    $ player_hp = player_max_hp
    $ enemy_hp = enemy_max_hp
    $ player_attack = player.attack
    $ enemy_attack = enemy.attack
    $ player_defense = 0
    $ selected_action = ""
    $ action_text = ""
    $ pole = ""

    show screen hp_bars_1v1
    
    show knight at left
    if enemy == bunny:
        show bunny at right
    elif enemy == iron:
        show ironfiling at right
    elif enemy == ginger:
        show gingerbreadman at right
    elif enemy == magmen:
        show magmen at right

    ## battle state
    while player_hp > 0 and enemy_hp > 0:

        # Player Turn

        # Rolling variables
        call dice_roll
        call roll_polarity_enemy
        call roll_polarity_player
        
        call screen player_phase
        ## choice screen
        call screen stats
        
        if selected_action == "Quick Attack":
            if player.polarity != enemy.polarity:                                           
                $ player_attack = d6
                if d10 >= 5:                                                
                    $ player_attack += d4
                    $ enemy_hp -= player_attack
                    play sound "hit.mp3"
                    "Critically attractive! You deal [player_attack] damage!"
                else:                               
                    $ enemy_hp -= player_attack
                    play sound "hit.mp3"
                    "The power of attraction!  You hit for [player_attack] damage!"
            elif player.polarity == enemy.polarity:  
                play sound "bounce.mp3"                                                     
                "You and the enemy repel each other... You bounce off the enemy and miss!" 

        elif selected_action == "Skill Attack":
            "You channel your magnetic field and direct its power towards the enemy!"
            $ player.power -= 1
            if pole == enemy.polarity:
                $ player_attack = d6 + d4
                $ enemy_hp -= player_attack
                play sound "pew.mp3"
                "Nice work! The field lines give the enemy a good hard shove! You deal [d6] damage."
                if enemy_hp >0:
                    "Despite the recoil, the enemy comes back for more."
                else:
                    "The enemy seems to have exploded from the impact."
            else:
                "Your field lines are too strongly attracted! You are pulled towards the enemy and your faces slam together!"
                $ player_hp -= d4
                $ enemy_hp -= 1
                play sound "hit.mp3"
                with vpunch
                "You take [d4] damage. The enemy takes 1 damage."

        elif selected_action == "Defend":
            play sound "shield.mp3"
            "You prepare your defenses..." 
            $ player_defense = 3
            "Defense is now 3!" 
            $ player.power += 1
            "You recover 1 Flux."

        elif selected_action == "Heal":
            if player.power < 1:
                "You don't have enough Flux for that."
                $ selected_action = ""
                call screen stats
            else:
                $ player_hp += d6
                $ player.power -= 1
                play sound "shield.mp3"
                "You heal [d6] health!"


        if enemy_hp <= 0:
            scene black
            show knight
            "You win the combat encounter!"
            call absorb
            hide screen hp_bars_1v1
            jump start.resume

        # Enemy Turn
        call screen enemy_phase
        call dice_roll
        $ d4 = d4*enemy_attack
        $ d10 = d10*enemy_attack
        call pick_enemy
        $ player_defense = 0
        $ selected_action = ""
        $ action_text = ""
            

    "Ouch! Your magnetisation points have been reduced to zero!"
    menu self_heal:
        "Will you try to heal yourself?"
        "Spend 2 Magnetic Flux to replenish MP":
            if player.power < 2:
                "Oops! You don't have enough flux for that!"
                "Guess you have to die then."
                hide screen hp_bars_1v1
                scene black
                "Maybe you can try again?"
                call screen confirm(message="Play again?", yes_action=Jump('start'), no_action=Quit(confirm=False))
            else:
                $ player_hp = player_max_hp
                $ player.power -= 2
                "You feel rejuvenated, yet at somewhat of a loss anyhow."
                "The journey continues!"
                jump start.resume

        "Give up":
            "...oh, okay then."
            hide screen hp_bars_1v1
            scene black
            "Maybe you can try again?"
            call screen confirm(message="Play again?", yes_action=Jump('start'), no_action=Quit(confirm=False))
    




