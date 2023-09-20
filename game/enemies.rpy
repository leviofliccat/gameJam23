##player: absorb magnet energy
label absorb:
    "You absorb the magnetic energy..."
    $ player.power += 1
    "your power is now [player.power]"
    return


##iron filing: one shot one kill (almost)
label iron_attacks:
    if d20 <= 18:                                                   
        "The iron filings rush at you, attaching themselves to your sexy magnetic body."
        "You can't get them unstuck from you!"
        if player_defense ==2:
            $ player_hp = 1
            "Your defense leaves you with a sliver of hope after the devastating attack!"
        else:
            $ player_hp -= 1000
            "The Iron Filings deal 1000 damage!"
    else:                                                    
        $ player_hp -= d4
        "The Filings attack for [d4] damage!"    
    return
    

label bunny_attacks:
    $ roll = renpy.random.randint(1,10)
    if roll >=7:
        "The bunny smiles at you and gives you a seductive wink."
    elif roll <=3:
        "The bunny looks at you fondly."
    elif roll <= 5:
        "The bunny bounces up and down, rather like a large jelly."
    else:
        "The bunny's cute smile disappears for a split second, and what seems like pure malice gleams in its dark eyes."
        "But a moment later it's back to its bouncy self."
    "The bunny deals 0 damage!"
    return

# label ginger_attacks:
#     if d20 >= 19:                                            # 20%       
#         $ player_hp -= d10
#         "The Enemy makes a wild attack for [d10] damage!"
#     elif d20 <=2:                                            # 20%
#         $ enemy_hp += d4
#         if enemy_hp < enemy_max_hp:
#             "The Enemy heals itself, raising [d4] hp!"
#         else:
#             $ enemy_hp = enemy_max_hp
#             "The Enemy fully heals itself back to full hp!"
#     else:                                                    # 60%
#         $ player_hp -= d4
#         "The Enemy attacks for [d4] damage!" 
#     return



label pick_enemy:
    if enemy == iron:
        call iron_attacks
    elif enemy == bunny:
        call bunny_attacks
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
    if en <= 2:
        $ enemy = bunny
        
    else:
        $ enemy = iron

    # elif en ==3:
    #     $ enemy = ginger
    # else:
    #     $ enemy = tower
    return
    