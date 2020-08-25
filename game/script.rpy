
define dia =0
define mes=1
define dias_en_mes = [0,13,28,31,30,31,30,31,31,30,31,30,31]

label start:
    #"inicio"
    call screen cuarto_screen

    return

screen cuarto_screen():
    add "images/bg_cuarto.png"
    textbutton "cama" xpos 200 action [Jump("day_transition")]
    textbutton "Salir de la habitación" xpos 300 action [Show("map")]


label day_transition:
    #"Fuiste a dormir"
    python:
        dia +=1
        if dias_en_mes[mes] < dia:
            mes +=1
            dia = 1

    call screen day_transition_screen

screen day_transition_screen():
    add "images/bg_transition.png"
    text "cambiar dia" xpos 500  ypos 500
    text "[dia] / [mes]" xpos 500  ypos 600

    timer 1 repeat False action Jump("start")

screen map():
    add "images/bg_mapa.png"
    textbutton "Dormitory" xpos 200 ypos 100 action [Jump("start")]
    textbutton "Commercial Zone" xpos 200 ypos 200 action [Jump("day_transition")]
    textbutton "School" xpos 200 ypos 300 action [Jump("school")]

label school:
    call screen school_screen

screen school_screen():
    add "images/bg_escuela.png"
    textbutton "Girl" xpos 200 action []
