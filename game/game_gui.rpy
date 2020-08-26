screen calendar_gui():

    text "[day] / [month]  ([day_of_week]) "
    text "[turn]" ypos 50

label map:
    #show screen calendar_gui
    scene bg_map at truecenter
    call screen map_screen

screen map_screen():

    textbutton "Dormitory" xpos 300 ypos 100 action Confirm("Regresar sin hacer nada?", [SetVariable("turn" , turn +1), Jump("cuarto") ], no = None,  confirm_selected=False)
    textbutton "Commercial Zone" xpos 300 ypos 200 action [Jump("commercial_zone")]
    textbutton "School" xpos 300 ypos 300 action [Jump("school")]


screen stats():
    text "stats- Girl= [girl_aff]" xpos 1300
