## BATTLE
label battle:
    ## initialise variables
    python:
        player_hp = player_max_hp
        enemy_hp = enemy_max_hp
        player_attack = player.attack
        enemy_attack = enemy.attack
        player_defense = 0
        selected_action = ""

    show screen hp_bars_1v1
    
    show bear at left
    if enemy == bunny:
        show bunny at right
    elif enemy == iron:
        show iron at right
    elif enemy == ginger:
        show ginger at right
    elif enemy == magmen:
        show magmen at right

    ## battle state
    label .battle_state:
        play music "highoctane.mp3" loop volume 0.1
        while player_hp > 0 and enemy_hp > 0:

            # Player Turn

            # Rolling variables
            call dice_roll from _call_dice_roll
            if counter != 1:
                call roll_polarity_enemy from _call_roll_polarity_enemy
                call roll_polarity_player from _call_roll_polarity_player
            call screen player_phase
            ## choice screen
            $ pole = ""
            call screen stats
            
            if selected_action == "Quick Attack":
                if player.polarity != enemy.polarity:                                           
                    $ player_attack = d6
                    if d10 >= 5:                                                
                        $ player_attack += d4
                        $ enemy_hp -= player_attack
                        show bear at playerAttack
                        play sound "hit.mp3"
                        "Critically attractive! You deal [player_attack] damage!"
                    else:                               
                        $ enemy_hp -= player_attack
                        show bear at playerAttack
                        play sound "hit.mp3"
                        "The power of attraction!  You hit for [player_attack] damage!"
                elif player.polarity == enemy.polarity:  
                    show bear at playerAttack
                    play sound "bounce.mp3"                                                     
                    "You and the enemy repel each other... You bounce off the enemy and miss!" 

            elif selected_action == "Skill Attack":
                show bear_field as bear at left with dissolve
                "You channel your magnetic field and direct its power towards the enemy!"
                show bear at left with dissolve
                show field_south at field with dissolve
                $ player.power -= 1
                if pole == enemy.polarity:
                    $ player_attack = max(d6 + d6, 5)
                    $ enemy_hp -= player_attack
                    play sound "pew.mp3" volume 0.5
                    "Nice work! The field lines give the enemy a good hard shove! You deal [player_attack] damage."
                    hide field_south with dissolve
                    if enemy_hp >0:
                        "Despite the recoil, the enemy comes back for more."
                    else:
                        play sound "explosion.mp3" volume 0.2
                        show explosion at right
                        call enemy_death_transition from _call_enemy_death_transition
                        hide explosion with dissolve
                        "The enemy explodes!"
                else:
                    "Your field lines are too strongly attracted! You are pulled towards the enemy and your faces slam together!"
                    hide field_south
                    $ player_hp -= d4
                    $ enemy_hp -= 1
                    play sound "hit.mp3"
                    show bear at slam_player
                    call enemy_slam from _call_enemy_slam
                    "You take [d4] damage. The enemy takes 1 damage."

            elif selected_action == "Defend":
                play sound "shield.mp3"
                show bear at defend_tint
                $ player_defense = 3
                "You prepare your defenses..." 
                if player.power < 7:
                    $ player.power += 1
                    "You recover 1 Flux."
                else:
                    "But for some logistical reason, you don't recover any Flux."

            elif selected_action == "Heal":
                if player.power < 1:
                    "You don't have enough Flux for that."
                    $ selected_action = ""
                    call screen stats
                elif player_hp = player_max_hp:
                    "You're already at full health!"
                    $ selected_action = ""
                    call screen stats
                else:
                    $ player_hp += d6
                    $ player.power -= 1
                    play sound "heal.mp3"
                    show bear at heal_tint
                    "You heal [d6] health!"


            if enemy_hp <= 0:
                call enemy_death_transition from _call_enemy_death_transition_1
                play sound "success.mp3"
                "You win the combat encounter!"
                call absorb from _call_absorb
                hide screen hp_bars_1v1
                jump start.resume

            # Enemy Turn
            call screen enemy_phase
            call dice_roll from _call_dice_roll_1
            $ d4 = d4*enemy_attack
            $ d10 = d10*enemy_attack
            call pick_enemy from _call_pick_enemy
            $ player_defense = 0
            $ selected_action = ""
            $ action_text = ""
                

    "Ouch! Your health has been reduced to zero!"
    menu self_heal:
        "Will you try to heal yourself?"
        "Spend 3 Magnetic Flux to replenish health":
            if player.power < 3:
                "Oops! You don't have enough flux for that!"
                "Guess you have to die then."
                hide screen hp_bars_1v1
                scene black
                "Maybe you can try again?"
                call screen confirm(message="Play again?", yes_action=Jump('start'), no_action=Quit(confirm=False))
            else:
                $ player_hp = player_max_hp
                $ player.power -= 3
                "You feel rejuvenated, yet at somewhat of a loss anyhow."
                "The journey continues!"
                jump battle.battle_state

        "Give up":
            "...oh, okay then."
            hide screen hp_bars_1v1
            scene black
            "Maybe you can try again?"
            call screen confirm(message="Play again?", yes_action=Jump('start'), no_action=Quit(confirm=False))
        




