define f = Character("Ferro")


label start:
    $ counter = 0
    
    $ player = fighter("Player")
    $ bunny = fighter("Bunny Magnet",1,1,0,"South",0,"bunny.png")
    $ iron = fighter("Iron Filings",6, 6, 1,"North",0,"ironfiling.png")
    $ ginger = fighter("Gingerbread Baker Magnet", 20, 20, 1, "North", 0, "gingerbreadman.png")
    $ magmen = fighter("Magnet Men", 9, 9, 3, "North", 0, "magmen.png")
    $ enemy = fighter("Enemy")

    "Controls: SPACE or CLICK to continue. CLICK to select. ESC or RIGHTCLICK for menu. Hold CTRL to skip."
    play sound "fall.mp3"
    with vpunch 
    "{i}!!! \nWhat was that?{/i}"
    "{i}In a daze, I open my eyes to be greeted by darkness.{/i}"
    f "Ugh... Everything hurts..."
    f "Where am I?"
    play sound "<from 0.1 to 1.0>flip.mp3"
    with vpunch
    "{i}With a groan and a surprising amount of effort, I manage to turn over.{/i}"
    ##bg light beam
    "{i}A small streak of light lies at the edge of my vision, parallel to the cold floor I lie on.{/i}"
    #transition to some shadows
    "{i}But some small dots cast shadows in the light...\nMagnets!{/i}"
    "{i}Fridge magnets, that had fallen off the fridge!{/i}"
    "{i}After recovering from the initial shock that I, the most attractive, beautiful magnet in this house, had rolled under the fridge, I steel myself.{/i}"
    "{i}This is my chance!{/i}"
    with hpunch
    "{i}I won't let the other magnets take my place at the top of the fridge!{/i}"
    with hpunch
    "{i}I deserve all the attention and glory!{/i}"
    f "It's time to fight my way out of here and regain my rightful place on the fridge!"
    "{i}Over there! I must defeat that magnet to absorb its magnetic energy and increase my magnetic flux!{/i}"
    "{i}With enough flux, I'll have enough power to stay stuck right at the top of the fridge!{/i}"
    jump .encounter
    label .resume:
        scene black
        call storytext
        "Entering another encounter!"
        if player.power >= 10:
            jump .finale
        jump .encounter
    label .encounter:
        call screen combat_start
        call roll_enemy
        scene black
        $ player_hp = player.hp
        $ enemy_hp = enemy.hp
        $ player_max_hp = player.max_hp
        $ enemy_max_hp = enemy.max_hp
        $ enemy_name = enemy.name
        $ counter += 1
        jump battle



label storytext:
    if counter==1:
        "{i}For my first battle, that was pretty easy. It sort of felt like the bunny was going easy on me...{/i}"
        f "Well, I guess it's time to keep going!"
    elif counter > 1 and player.power<10:
        f "Another one down! I think 10 Flux should be enough power..."
    if player.power >= 10:
        f "Phew, I finally have enough power! It's time to make my way up the fridge!"
        #jumping noises
        f "This is it! Right in the middle of the fridge, where everyone can see me."
        f "...Hang on.{w=0.5} What's going on?!"
        scene black
        f "No!{p=0.5}Whose hand is that?!!"
        f "Don't take me away!! NOOOOOO!!!!!"
        "Thanks for playing!"
        $ renpy.full_restart()
    return
        
    


