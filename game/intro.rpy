
label intro_uno:
    "Aquì comienza la historia,serà contada comouna vn"
    "Al final del dìa te encuentras en tu cuarto"
    $turn =2
    jump cuarto

label intro_dos:
    scene bg_room at truecenter
    "Historia del segundo dia"
    "Deberia ir a la zona comercial"

    show bg_commercial_zone at truecenter
    with dissolve
    with Pause(2)
    "Segunda chica"
    "Me voy"
    hide bg_commercial_zone

    show bg_room at truecenter
    with dissolve
    with Pause(2)
    "Irè a dormir"

    jump day_transition


label intro_tres:
    scene bg_room at truecenter
    "Mejor me apresuro a la escuela!"
    "Me acompaña otaku?"

    show bg_school at truecenter
    with dissolve
    with Pause(2)
    "Aqui es "
    "blablablachica 1 y 2, voy a buscar mi clase"
    hide bg_school


    show bg_classroom at truecenter
    with dissolve
    "yada yada clase"

    hide bg_classroom

    show bg_school at truecenter
    with dissolve
    with Pause(2)
    "me vo bye"

    hide bg_school

    "buen dia bla bla"

    jump day_transition
