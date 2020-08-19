
define dia =0
define mes=1
define dias_en_mes = [0,13,28,31,30,31,30,31,31,30,31,30,31]

label start:
    #"inicio"
    call screen inicial

    return

screen inicial():
    add "images/background.png"
    textbutton "cama" xpos 200 action [Jump("day_transition")]


label day_transition:
    #"Fuiste a dormir"
    python:
        dia +=1
        if dias_en_mes[mes] < dia:
            mes +=1
            dia = 1

    call screen day_transition_screen

screen day_transition_screen():
    add "images/background.png"
    text "cambiar dia" xpos 500  ypos 500
    text "[dia] / [mes]" xpos 500  ypos 600

    timer 1 repeat False action Jump("start")
