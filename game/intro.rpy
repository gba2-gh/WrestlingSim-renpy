
label intro_uno:
    "Aquì comienza la historia,serà contada comouna vn"
    "Al final del dìa te encuentras en tu cuarto"

    jump room

label intro_dos:###encuentro con dos
    $turn= 1
    scene bg_room at truecenter
    "Historia del segundo dia"
    "Deberia ir a la zona comercial"

    show bg_commercial_zone at truecenter
    with dissolve
    with Pause(2)
    "Segunda chica"
    "Me voy"
    hide bg_commercial_zone

    $turn=3
    show bg_room at truecenter
    with dissolve
    with Pause(2)
    "Irè a dormir"

    jump day_transition


label intro_tres: ###primer dia de escuela
    scene bg_room at truecenter
    "Mejor me apresuro a la escuela!"
    "Me acompaña otaku?"
    hide bg_room

    show bg_school at truecenter
    with dissolve
    with Pause(2)
    "Aqui es "
    "blablabla chica 1 y 2, voy a buscar mi clase"
    hide bg_school
    jump school_main

label intro_tres_2: ###en salon de clases
    show bg_classroom at truecenter
    with dissolve
    "yada yada clase"

    hide bg_classroom

    $turn=3
    show bg_school at truecenter
    with dissolve
    with Pause(2)
    "me vo bye"

    hide bg_school

    show bg_room at truecenter
    $turn =4
    "buen dia bla bla"

    call day_transition

label intro_4: ###te pide
