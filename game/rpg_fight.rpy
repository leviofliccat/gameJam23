##  RPG fight

## fighter class
init python:
    class fighter:
        def __init__(self, name, max_hp = 10, hp = 10, attack = 1, polarity = "North", power = 0):
            self.name = name
            self.max_hp = max_hp
            self.hp = hp
            self.attack = attack
            self.polarity = polarity
            self.power = power


# Random Number Generator
label dice_roll:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return

# label init_start:

    # $ player = fighter("Player")
    # $ bunny = fighter("Bunny",1,1,0)
    # $ iron = fighter("Iron Filings", 5, 5, 1)
    
    # call roll_enemy
    # scene

    # $ player_hp = player.hp
    # $ enemy_hp = enemy.hp
    # $ player_max_hp = player.max_hp
    # $ enemy_max_hp = enemy.max_hp
    # $ enemy_name = enemy.name
    
    
    


## BATTLE

label battle:

    $ player_hp = player_max_hp
    $ enemy_hp = enemy_max_hp
    $ player_attack = player.attack
    $ enemy_attack = enemy.attack
    $ player_defense = 0

    show screen hp_bars_1v1
    show screen player_power_box
    show screen polarity_box
    
    show knight at left
    if enemy == bunny:
        show bunny at right
    elif enemy == iron:
        show ironfiling at right


    while player_hp > 0 and enemy_hp > 0:

        # Player Turn

        # Rolling variables
        call dice_roll
        call roll_polarity_enemy
        call roll_polarity_player

        call screen selectAction(player)
        menu:
            "What are you going to do?"

            "Quick Attack":
                if player.polarity != enemy.polarity:                                           
                    $ player_attack = d4
                    if d10 >= 5:                                                
                        $ player_attack += 1   
                        $ enemy_hp -= player_attack
                        "Critically attractive! You deal an extra 1 damage for [player_attack] damage!"
                    else:                               
                        $ enemy_hp -= player_attack
                        "The power of attraction!  You hit for [player_attack] damage!"
                elif player.polarity == enemy.polarity:                                                       
                    "You and the enemy repel each other... You bounce off the enemy and miss!" 

            "Attack with magnetic field":
                menu:
                    "Attack with North pole":
                        "You channel your magnetic field and direct its power towards the enemy!"
                        if "North" == enemy.polarity:
                            $ player_attack = d6
                            $ enemy_hp -= player_attack
                            "Nice work! The field lines give the enemy a good hard shove!"
                            if enemy_hp >0:
                                "Despite the recoil, the enemy comes back for more."
                            else:
                                "The enemy seems to have exploded from the impact."
                        else:
                            "Your field lines are too strongly attracted! You are pulled towards the enemy and your faces slam together!"
                            $ player_hp -= d4/2
                            $ enemy_hp -= 1
                            "You take [d4/2] damage. The enemy takes 1 damage."
                            
                    "Attack with South pole":
                        if "South" == enemy.polarity:
                            "You channel your magnetic field and direct its power towards the enemy!"
                            $ player_attack = d6
                            $ enemy_hp -= player_attack
                            "Nice work! The field lines give the enemy a good hard shove!"
                            if enemy_hp >0:
                                "Despite the recoil, the enemy comes back for more."
                            else:
                                "The enemy seems to have exploded from the impact."
                        else:
                            "Your field lines are too strongly attracted! You are pulled towards the enemy and your faces slam together!"
                            $ player_hp -= d4/2
                            $ enemy_hp -= 1
                            "You take [d4/2] damage. The enemy takes 1 damage."

            "Defend":
                "You prepare your defenses..." 
                $ player_defense = 2    
                "Defense increased by 2!"                             
        
        if enemy_hp <= 0:
            "You win the combat encounter!"
            call absorb
            jump start.resume

        # Enemy Turn - Semi-randomized behavior!

        call dice_roll
        $ d4 = d4*enemy_attack - player_defense
        $ d10 = d10*enemy_attack - player_defense
        call pick_enemy
        $ player_defense = 0
            

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
                "You feel rejuvenated, yet at somewhat of a loss anyhow."
                "The journey continues!"
                jump start.resume

        "Give up":
            "...oh, okay then."
            hide screen hp_bars_1v1
            scene black
            "Maybe you can try again?"
            call screen confirm(message="Play again?", yes_action=Jump('start'), no_action=Quit(confirm=False))
    

    menu harder_menu:
        "Play this level again?":
            $ player_hp = player_max_hp
            $ enemy_hp = enemy_max_hp
            jump battle
        "continue":
            scene
            jump start.resume
        "Proceed" if player.power >=5:
            jump finale



label finale:
    "congrats u won"
    return