style stat_frame:
    background "black"
    yminimum 1.0
    xminimum 1.0
    ypos 0.7
style stat_hbox:
    spacing 50
    xpos 0.1
    ypos 0.05
    
style stat_options:
    xalign 0.0
    yalign 0.0
    xminimum 300
style stat_desc:
    xalign 0.0
    yalign 0.0
    xmaximum 800


screen stats:
    default action_desc = "What will you do?"
    frame:
        style "stat_frame"
        hbox:
            style "stat_hbox"
            vbox:
                align (0.0, 0.0)
                spacing 10
                text "Flux: [player.power]"
                text "Player Polarity: [player.polarity]"
                text "Enemy Polarity: [enemy.polarity]"
                
            vbox:
                style "stat_options"
                textbutton "Quick Attack":
                    hovered SetLocalVariable("action_desc", "A light strike. No cost.")
                    unhovered SetLocalVariable("action_desc", "What are you going to do?")
                    action SetVariable("selected_action", "Quick Attack"), Return()
                textbutton "Skill Attack":
                    hovered  SetLocalVariable("action_desc", "Attack with your magnetic field. Costs 1 Flux."), 
                    unhovered SetLocalVariable("action_desc", "What are you going to do?")
                    action SetVariable("selected_action", "Skill Attack"), ToggleScreen("stats"), Show("skills")
                textbutton "Defend":
                    hovered  SetLocalVariable("action_desc", "Enter a defensive stance and recover 1 Flux."), 
                    unhovered SetLocalVariable("action_desc", "What are you going to do?")
                    action SetVariable("selected_action", "Defend"), Return()
                textbutton "Heal":
                    hovered  SetLocalVariable("action_desc", "Recover some health. Costs 1 Flux."), 
                    unhovered SetLocalVariable("action_desc", "What are you going to do?")
                    action SetVariable("selected_action", "Heal"), Return()
            vbox:
                style "stat_desc"
                text "[action_desc]" 

                
screen skills:
    default skill_desc = ""
    
    frame:
        style "stat_frame"
        
        hbox:
            style "stat_hbox"
            vbox:
                align (0.0, 0.0)
                spacing 10
                text "Flux: [player.power]"
                text "Player Polarity: [player.polarity]"
                text "Enemy Polarity: [enemy.polarity]"
            vbox:
                style "stat_options"
                textbutton "Attack with North pole":
                    hovered SetLocalVariable("skill_desc", "Perform this skill with a North polarity.")
                    unhovered SetLocalVariable("skill_desc", "")
                    action SetVariable("pole", "North"), ToggleScreen("skills"), Return()
                textbutton "Attack with South pole":
                    hovered  SetLocalVariable("skill_desc", "Perform this skill with a South polarity."), 
                    unhovered SetLocalVariable("skill_desc", "")
                    action SetVariable("pole", "South"), ToggleScreen("skills"), Return()
                textbutton "Back":
                    yoffset 20
                    hovered  SetLocalVariable("skill_desc", "Cancel and return to action selection."), 
                    unhovered SetLocalVariable("skill_desc", "")
                    action SetVariable("selected_action", ""), ToggleScreen("skills"), Show("stats")
            vbox:
                style "stat_desc"
                text "[skill_desc]" 