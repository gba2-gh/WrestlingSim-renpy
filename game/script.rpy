#init:
    #    $ memo = Character(None, kind=narrator, window_xpos=0.5, window_ypos=0.5,window_xanchor=0.5,window_yanchor=0.5,window_background= None, what_xalign=0.5, what_yalign=0.5, window_ymaximum=50,   window_yminimum=35, window_xpadding =15, window_top_padding=10, window_bottom_padding=15, window_xmargin =50,window_ymargin =0,)

label start:
    #"inicio"
    jump intro_uno

    return

label cuarto:

    python:
        if day == 2:
            renpy.call('intro_dos')
        elif day ==3:
            renpy.call('intro_tres')


    scene bg_room at truecenter
    show screen calendar_gui
    show screen stats
    call screen cuarto_screen


screen cuarto_screen():

    textbutton "cama" xpos 200  ypos 400action Confirm("Dormir hasta mañana?", Jump("day_transition"), no=None, confirm_selected=False)
    textbutton "Salir de la habitación" xpos 300 ypos 400 action If( turn ==  2, Call("door_closed"), Call("door_open")) #Confirm("Quieres salir", Show("general_map") , no=None, confirm_selected=True


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

    call screen day_transition_screen

screen day_transition_screen():
    add "images/bg/bg_transition.png"
    text "cambiar dia" xpos 500  ypos 500
    text "[day] / [month]   ([day_of_week])" xpos 500  ypos 600


    timer 1 repeat False action Jump("cuarto")


label commercial_zone:
    scene bg_map at truecenter
    "Cerrado"
    jump map

label school:
    scene school at truecenter
    call screen school_screen

screen school_screen():
    textbutton "Girl" xpos 300 ypos 300 action [SetVariable("girl_aff", girl_aff + 1), Notify("Girl aff +1"), SetVariable("turn" , turn +1), Jump("cuarto")]
    textbutton "Regresar  a Mapa" xpos 300  ypos 400 action Jump("map")
    textbutton "Pizarrón" xpos 300  ypos 400 action Jump("")
