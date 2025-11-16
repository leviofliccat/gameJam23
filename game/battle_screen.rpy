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
                text "(temp UI)Player HP: [player_hp]"
                
            vbox:
                style "stat_options"
                textbutton "Quick Attack":
                    style "stat_button"
                    hovered [SetLocalVariable("action_desc", "A basic strike and somewhat a gamble. No cost.")]
                    unhovered SetLocalVariable("action_desc", "What are you going to do?")
                    action [SetVariable("selected_action", "Quick Attack"), Return()]
                textbutton "Skill Attack":
                    style "stat_button"
                    hovered  [SetLocalVariable("action_desc", "Attack with your magnetic field. Costs 1 Flux. Select for more options.")]
                    unhovered SetLocalVariable("action_desc", "What are you going to do?")
                    action [SetVariable("selected_action", "Skill Attack"), Hide("stats"), Show("skills")]
                textbutton "Defend":
                    style "stat_button"
                    hovered  [SetLocalVariable("action_desc", "Enter a defensive stance and recover 1 Flux.")]
                    unhovered SetLocalVariable("action_desc", "What are you going to do?")
                    action [SetVariable("selected_action", "Defend"),Return()]
                textbutton "Heal":
                    style "stat_button"
                    hovered  [SetLocalVariable("action_desc", "Recover some health. Costs 1 Flux.")] 
                    unhovered SetLocalVariable("action_desc", "What are you going to do?")
                    action [SetVariable("selected_action", "Heal"),Return()]
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
                    style "stat_button"
                    hovered [SetLocalVariable("skill_desc", "Perform this skill with a North polarity.")]
                    unhovered SetLocalVariable("skill_desc", "")
                    action [SetVariable("pole", "North"), Hide("skills"),Return()]
                textbutton "Attack with South pole":
                    style "stat_button"
                    hovered  [SetLocalVariable("skill_desc", "Perform this skill with a South polarity.")]
                    unhovered SetLocalVariable("skill_desc", "")
                    action [SetVariable("pole", "South"),  Hide("skills"),Return()]
                textbutton "Back":
                    style "stat_button"
                    yoffset 20
                    hovered  [SetLocalVariable("skill_desc", "Cancel and return to action selection.")] 
                    unhovered SetLocalVariable("skill_desc", "")
                    action [SetVariable("selected_action", ""), Hide("skills"),Show("stats")]
            vbox:
                style "stat_desc"
                text "[skill_desc]" 