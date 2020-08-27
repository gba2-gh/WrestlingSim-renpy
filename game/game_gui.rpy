screen calendar_gui():

    text "[day] / [month]  ([day_of_week]) "
    text "[turn]" ypos 50

label map:
    #show screen calendar_gui
    scene bg_map at truecenter
    call screen map_screen

screen map_screen():

    textbutton "Dormitory" xpos 300 ypos 100 action Confirm("Regresar sin hacer nada?", [SetVariable("turn" , turn +1), Jump("room") ], no = None,  confirm_selected=False)
    textbutton "Commercial Zone" xpos 300 ypos 200 action [Jump("commercial_zone")]
    textbutton "School" xpos 300 ypos 300 action [Jump("school_main")]


screen stats():
    #text "stats- Girl= [girl_aff]" xpos 1300

    for quest in quest_todo_weekday :
        $q_uno=quest_todo_weekday[0].fname
    for quest in quest_todo_turn :
        $q_dos=quest_todo_turn[0].fname
    text "[q_uno]" xpos 1500 ypos 300
    text "[q_dos]" xpos 1500 ypos 400
