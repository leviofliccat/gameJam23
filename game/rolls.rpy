# Random Number Generator
label dice_roll:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return

label pick_enemy:
    if enemy == iron:
        call iron_attacks from _call_iron_attacks
    elif enemy == bunny:
        call bunny_attacks from _call_bunny_attacks
    elif enemy == ginger:
        call ginger_attacks from _call_ginger_attacks
    elif enemy == magmen:
        call magmen_attacks from _call_magmen_attacks
    return

label roll_polarity_enemy:
    $ d2 = renpy.random.randint(1,2)
    if d2 == 1:
        $ enemy.polarity = "North"
    else:
        $ enemy.polarity = "South"
    return

label roll_polarity_player:
    $ d2 = renpy.random.randint(1,2)
    if d2 == 1:
        $ player.polarity = "North"
    else:
        $ player.polarity = "South"
    return

label roll_enemy:
    $ en = renpy.random.randint(1,4)
    if counter == 0:
        $ enemy = bunny
    elif en ==1:
        $ enemy = bunny
    elif en==2:
        $ enemy = iron
    elif en ==3:
        $ enemy = ginger
    elif en == 4:
        $ enemy = magmen
    return
    