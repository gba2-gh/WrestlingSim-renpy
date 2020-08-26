
label door_closed:
    #show bg_room at truecenter
    "Será mejor dormir"

    jump cuarto

label door_open:

    menu:
        "Deberìa salir ? (Regresarás hasta tarde)"

        "Salir":

            jump map

        "Cancelar":

            jump cuarto
