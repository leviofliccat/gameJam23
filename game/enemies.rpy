## fighter class
init python:
    class fighter:
        def __init__(self, name, max_hp = 20, hp = 20, attack = 1, polarity = "North", power = 3, sprite = "knight.jpg"):
            self.name = name
            self.max_hp = max_hp
            self.hp = hp
            self.attack = attack
            self.polarity = polarity
            self.power = power
            self.sprite = sprite


##player: absorb magnet energy
label absorb:
    "You absorb the magnetic energy..."
    $ player.power += 2
    "Your Flux is now [player.power]!"
    return


##iron filing: one shot one kill (almost)
label iron_attacks:
    if d20 <= 18:        
        play sound "chain.mp3"
        if player.polarity == enemy.polarity:
            "The iron filings rush at you in an attempt to stick permanently to your body."
            "But wait! Some of them are repelled! They don't look too happy about that."        
            $ player_hp -= 2
            play sound "swordhit.mp3"
            "You take 2 damage!"       
        else:                            
            "The iron filings rush at you, attaching themselves to your attractive magnetic body."
            "You can't get them unstuck from you!"
            if player_defense ==2:
                $ player_hp = 1
                play sound "sword.mp3"
                "Your defense leaves you with a sliver of hope after the devastating attack!"
            else:
                $ player_hp -= 1000
                play sound "sword.mp3"
                "The Iron Filings deal 1000 damage! Critical!!"
    else:                                                    
        $ player_hp -= d4
        play sound "swordhit.mp3"
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
    if player_hp < player_max_hp:
        $ player_hp = player_max_hp
        play sound "heal.mp3"
        "The bunny restores you to full health!"
    else:
        "The bunny deals 0 damage!"
    return

label ginger_attacks:
    if d20 ==20:                                                 
        $ player_hp -= d10
        play sound "sizzle.mp3" volume 0.2
        "The gingerbread baker uses his spatula to heat you past your Curie temperature, dealing [d10] damage!"
    elif d20 <=2:                                           
        $ enemy_hp += d4
        play sound "heal.mp3"
        if enemy_hp < enemy_max_hp:
            "The Enemy heals itself, raising [d4] hp!"
        else:
            $ enemy_hp = enemy_max_hp
            "The Enemy fully heals itself back to full hp!"
        return
    else:        
        $ d4 = d4 - player_defense                                            
        $ player_hp -= d4
        play sound "sizzle.mp3" volume 0.2
        "The gingerbread man attacks for [d4] damage!" 
    if player_defense >0 :
        "You resisted 3 damage!"
    return

label magmen_attacks:
    if d20 >= 17:       
        $ d6 = d6 + d4 - player_defense                                         
        $ player_hp -= d6 
        play sound "pipe.mp3"
        "The magnet men channel their power and attack together for [d6] damage!"
    elif d20 <=4:     
        $ d4 -= player_defense                                       
        $ player_hp -= d4 
        play sound "punch.mp3"
        "The red magman growls angrily and attacks you for [d4] damage!"
        $ player_hp += d6
        play sound "heal.mp3"
        "But the blue magman feels a bit sorry for you, so blesses you with [d6] health."
        "The green magman just smiles at you. It's kind of cute."
    else:                                                    
        $ d6 -= player_defense
        $ player_hp -= d6
        play sound "punch.mp3"
        show magmen at enemyAttack
        "One of the magnet men attacks for [d6] damage!" 
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
    