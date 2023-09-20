


label start:

    hide black
    
    $ player = fighter("Player")
    $ bunny = fighter("Bunny",1,1,0)
    $ iron = fighter("Iron Filings", 5, 5, 1)
    $ enemy = fighter("Enemy")

    label .encounter:
        call roll_enemy

        $ player_hp = player.hp
        $ enemy_hp = enemy.hp
        $ player_max_hp = player.max_hp
        $ enemy_max_hp = enemy.max_hp
        $ enemy_name = enemy.name
        jump battle
    
    "welcome"
    "initialising now"
    jump .encounter
    label .resume:
        scene
        "resuming content now"
        "some more flavour text that's conditional on your power"
        "let's enter another encounter"
        jump .encounter

    return


    


