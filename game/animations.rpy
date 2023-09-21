transform playerAttack:
    xalign 0.0
    linear 0.3 xpos 700
    ease 0.5 xpos 0

transform enemyAttack:
    xpos 1.0
    linear 0.3 xpos 0.7
    ease 0.5 xpos 1.0

transform slam_player:
    xalign 0.0
    linear 0.2 xpos 0.2
    ease 0.3 xpos 0.0

transform slam_enemy:
    xalign 1.0
    linear 0.2 xpos 0.8
    ease 0.3 xpos 1.0

transform field:
    xpos 0.355
    ypos 0.07


label enemy_slam:
    if enemy == bunny:
        show bunny at slam_enemy
    elif enemy == iron:
        show iron at slam_enemy
    elif enemy == ginger:
        show ginger at slam_enemy
    elif enemy == magmen:
        show magmen at slam_enemy
    return

label enemy_death_transition:
    if enemy == bunny:
        hide bunny with dissolve
    elif enemy == iron:
        hide iron with dissolve
    elif enemy == ginger:
        hide ginger with dissolve
    elif enemy == magmen:
        hide magmen with dissolve
    return

transform defend_tint:
    matrixcolor TintMatrix((0,0,0,0))
    linear 0.5 matrixcolor TintMatrix((243,194,69))
    ease 1.0 matrixcolor TintMatrix((0,0,0,0))

transform heal_tint:
    matrixcolor TintMatrix((0,0,0,0))
    linear 0.5 matrixcolor TintMatrix((88, 249, 174, 255))
    ease 1.0 matrixcolor TintMatrix((0,0,0,0))
    #Color((88, 249, 174, 255))