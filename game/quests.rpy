
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
            self.weekday_avbl = weekday_avbl  #0 : all
            self.turns_avbl = turns_avbl

            if self not in all_quests:
                all_quests.append(self)


    def display_quest(current_place):
        del quest_todo_display[:]
        for quest in quest_todo_turn:
            for place in quest.places_avbl:
                if current_place == place:
                    quest_todo_display.append(quest)


        return


    def calc_quest_todo_weekday():
        del quest_todo_weekday[:] #limpiar lista anterior

        for quest in quest_todo:
            for day in quest.weekday_avbl:
                if day == weekday or day == 0:
                    quest_todo_weekday.append(quest)
        # for quest in quest_todo:
        #     if quest.weekday_avbl[0] == 0:
        #         quest_todo_weekday.append(quest)



    def set_turn(current_turn,x):
        #crear lista de posibles acciones por turno
        del quest_todo_turn[:]

        for quest in quest_todo_weekday:
            for turn in quest.turns_avbl:
                if current_turn == turn or turn == 0:
                    quest_todo_turn.append(quest)

        return x




init python:
    test_quest= quest("test_quest", "Encuentra las llaves",  "test_quest_label",  ["corridor_1r"], [0], [0])



label test_quest_label:

    "not much"
