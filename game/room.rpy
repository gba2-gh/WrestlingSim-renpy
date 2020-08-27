
label room:

    python:
        if day == 2:
            renpy.call('intro_dos')
        elif day ==3:
            renpy.call('intro_tres')
        if weekday <=5: #lun a vie, empiezas en lunchtime
            renpy.jump('school_classroom')


    scene bg_room at truecenter
    show screen calendar_gui
    show screen stats
    call screen room_screen


screen room_screen():

    textbutton "cama" xpos 200  ypos 400 action Confirm("Dormir hasta mañana?", Jump("day_transition"), no=None, confirm_selected=False)
    textbutton "Puerta" xpos 300 ypos 400 action Jump("door_room")
    textbutton "Saltar" xpos 300 ypos 500 action  [SetVariable("day", 3 ),SetVariable("weekday", 1 )]


########## PLAYER INTERACTION
############################
label door_room:
    #show bg_room at truecenter
    python:
        if day== 1:
            narrator("Será mejor dormir")

            renpy.jump('room')

        else:
            narrator("Deberìa salir ? (Regresarás hasta tarde)", interact= False)
            result=renpy.display_menu([("Salir", "map") , ("Cancelar" , "room") ])
            renpy.jump(result)
