## fighter class
init python:
    class fighter:
        def __init__(self, name, max_hp = 20, hp = 20, attack = 1, polarity = "North", power = 3, sprite = "bear.png"):
            self.name = name
            self.max_hp = max_hp
            self.hp = hp
            self.attack = attack
            self.polarity = polarity
            self.power = power
            self.sprite = sprite

label deal_damage(damage=0, special=False, sound="", dealer="The enemy attacks"):
        $ damage = max(damage - player_defense, 0)                                 
        $ player_hp -= damage
        play sound [sound] volume 0.2
        if special == True:
            return damage
        "[dealer] for [damage] damage!" 
        if player_defense > 0 :
            "You resisted 3 damage!"
        return



##player: absorb magnet energy
label absorb:
    "You absorb the magnetic energy..."
    $ player.power += 2
    play sound "heal.mp3"
    "Your Flux is now [player.power]!"
    return


##iron filing: one shot one kill (almost)
label iron_attacks:
    if d20 > 14:                                    # 25%
        play sound "chain.mp3"
        if player.polarity == enemy.polarity:
            "The iron filings rush at you in an attempt to stick permanently to your body."
            "But wait! Some of them are repelled! They don't look too happy about that."        
            $ player_hp -= 4
            play sound "swordhit.mp3"
            "You take 4 damage!"       
        else:                            
            "The iron filings rush at you, attaching themselves to your attractive magnetic body."
            "You can't get them unstuck from you!"
            if player_defense ==2:
                $ player_hp = 1
                play sound "sword.mp3"
                "Your defense leaves you with a sliver of hope after the devastating attack!"
            else:
                $ player_hp = 0
                play sound "sword.mp3"
                "The Iron Filings deal 1000 damage! Critical!!"
    else:                                           # 75%      
        call deal_damage(d4, False, "swordhit.mp3", "The iron filings attack")   
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

    if d20 >= 17:                   # 20%                           
        call deal_damage(d10+d4, True, 'sizzle.mp3')
        "The gingerbread baker uses his spatula to heat you past your Curie temperature, dealing [_return] damage!"
    elif d20 <=0:                   # 10%                   
        $ enemy_hp += d4
        play sound "heal.mp3"
        if enemy_hp < enemy_max_hp:
            "The baker heals itself for [d4] hp!"
        else:
            $ enemy_hp = enemy_max_hp
            "The baker fully heals itself back to full hp!"
        return
    else:                           # 70%
        call deal_damage(d4,False, 'sizzle.mp3', 'The gingerbread baker attacks')
    return




label magmen_attacks:
    if d20 >= 17:       
        call deal_damage(d4+d6,True, 'pipe.mp3')
        # $ d6 = d6 + d4 - player_defense                                         
        # $ player_hp -= d6 
        # play sound "pipe.mp3"
        "The magnet men channel their power and attack together for [d6] damage!"
    elif d20 <=4:     
        call deal_damage(d4,True, 'punch.mp3')
        # $ d4 -= player_defense                                       
        # $ player_hp -= d4 
        # play sound "punch.mp3"
        "The red magman growls angrily and attacks you for [d4] damage!"
        $ player_hp += d6
        play sound "heal.mp3"
        "But the blue magman feels a bit sorry for you, so blesses you with [d6] health."
        "The green magman just smiles at you. It's kind of cute."
    else:                                                    
        show magmen at enemyAttack
        call deal_damage(d6, False, 'punch.mp3', 'One of the magnet men attacks')
        # $ d6 -= player_defense
        # $ player_hp -= d6
        # play sound "punch.mp3"
        
        # "One of the magnet men attacks for [d6] damage!" 
    return

