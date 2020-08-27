####LOCATION
############

label school_main:
    scene bg_school at truecenter
    call screen school_main_screen

screen school_main_screen():
    $display_quest("school_main")
    for quest in quest_todo_display:
        $texto= quest.name
        textbutton "[texto]" xpos 1000 action NullAction()

    textbutton "Girl" xpos 300 ypos 300 action [SetVariable("girl_aff", girl_aff + 1), Notify("Girl aff +1"), SetVariable("turn" , turn +1), Jump("room")]
    textbutton "Entrada" xpos 300  ypos 400 action Jump("door_school_main")
    textbutton "Pizarrón" xpos 300  ypos 500 action Jump("board_school_main")
    textbutton "Pasillo Derecha" xpos 500  ypos 400 action Jump("corridor_r_school_main")

    if day == 4:
        textbutton "Heroína" xpos 500  ypos 500 action Jump("Ayuda, ayuda, te veo despuès")


label school_classroom:

    $turn= set_turn(turn, 1)
    scene bg_classroom at truecenter

    python:
        if day==3:
            renpy.jump( 'intro_tres_2')

        if day==4:
            narrator("morra habla conmigo")
            quest_todo.append(test_quest)
            calc_quest_todo_weekday()
            #poner primer quest en lista

    "clase,clase,si o no"


    $turn= set_turn(turn, 2)
    jump school_main


label corridor_1r:
    scene bg_corridor_1r at truecenter
    call screen corridor_1r_screen

screen corridor_1r_screen():
    $display_quest("corridor_1r")
    for quest in quest_todo_display:
        $texto= quest.name
        textbutton "[texto]" xpos 1000 action NullAction()
    textbutton "Classroom" xpos 300  ypos 300 action Jump("school_classroom")
    textbutton "Main Hall" xpos 300  ypos 400 action Jump("school_main")

########## PLAYER INTERACTION
############################

label door_school_main:
    python:
        if turn < 3:
            narrator("Debo ir a clase")
            renpy.jump('school_main')
        else:
            renpy.jump('map')

label board_school_main:
    python:
        if day < 4:
            narrator("Se muestran los salones")
            narrator("Parece que estàn en el 4as98f")
            seen_board=True
            renpy.jump('school_main')
        else:
            narrator("No hay nada nuevo")
            renpy.jump('school_main')


label corridor_r_school_main:
    python:
        if day == 3:
            if seen_board:
                renpy.jump('corridor_1r')
            else:
                narrator("Debería ver el pizarrón")
                renpy.jump('school_main')

        renpy.jump('corridor_1r')
