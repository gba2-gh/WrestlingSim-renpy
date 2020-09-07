
    #TURNOS:  0-Early Morning; 1-Morning; 2-Lunch Break; 3-Afternoon ; 4-Evening
    #En ocasiones son puestos directamente, en ocasiones es necesario calcular los quest
label start:
    #"inicio"
    $turn = 4
    jump intro_uno

    return

label day_transition:
    #"Fuiste a dormir"
    python:
        day +=1
        if days_in_month[month] < day:
            month +=1
            day = 1
        turn = 0

        if weekday >= 7:
            weekday = 0

        weekday +=1

        day_of_week= days_of_week[weekday]

        ###Crear lista de posibles misiones del dia
        calc_quest_todo_weekday()


    call screen day_transition_screen

screen day_transition_screen():
    add "images/bg/bg_transition.png"
    text "cambiar dia" xpos 500  ypos 500
    text "[day] / [month]   ([day_of_week])" xpos 500  ypos 600


    timer 1 repeat False action Jump("room")




label test_quest_label:
    scene bg_corridor_1r at truecenter
    "DONDE ESTABAS AAAAH"
    "Haz esto y lo otro"
    jump corridor_1r
