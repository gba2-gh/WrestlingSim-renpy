
init -2 python:
    quest_todo=[]
    quest_todo_weekday=[]
    quest_todo_turn= []
    quest_todo_display =[]

    all_quests=[]
    class quest(store.object):
        #nombre, fancy name, tipo, descripcion, imagen, precio base, precio real, comerciable, apilable
        def __init__(self, name, fname, label, places_avbl , weekday_avbl , turns_avbl, ):
            global all_quests
            self.name = name
            self.fname = fname
            self.label =label
            self.places_avbl = places_avbl
            self.weekday_avbl = weekday_avbl  #0 = all
            self.turns_avbl = turns_avbl

            if self not in all_quests:
                all_quests.append(self)

    #Encuentra misiones que se pueden realizar dependiendo del DIA
    def calc_quest_todo_weekday():
        del quest_todo_weekday[:] #limpiar lista anterior

        for quest in quest_todo:
            for day in quest.weekday_avbl:
                if day == weekday or day == 0:
                    quest_todo_weekday.append(quest)


    #Cambia el turno a "X" y encuentra misiones que se pueden realizar dependiendo del TURNO
    def set_turn(current_turn,x):
        del quest_todo_turn[:]

        for quest in quest_todo_weekday:
            for turn in quest.turns_avbl:
                if current_turn == turn or turn == 0:
                    quest_todo_turn.append(quest)

        return x


    # def display_quest(current_place):
    #     del quest_todo_display[:]
    #     for quest in quest_todo_turn:
    #         for place in quest.places_avbl:
    #             if current_place == place:
    #                 quest_todo_display.append(quest)
    #
    #
    #     return

    #Despliega los quest disponibles en current_place
    screen display_quest(current_place):
        python:
            del quest_todo_display[:]
            for quest in quest_todo_turn:
                for place in quest.places_avbl:
                    if current_place == place:
                        quest_todo_display.append(quest)

        for quest in quest_todo_display:
            $texto= quest.name
            textbutton "[quest.label]" xpos 1000 action Jump(quest.label)



init python:
    test_quest= quest("test_quest", "Encuentra las llaves",  "test_quest_label",  ["school_main","corridor_1r"], [0], [0])
