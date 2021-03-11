import random

players = ["Алексей", "Сергей", "Димон", "Алена", "Катя"]

# for player in players: # не корректно - запускать цикл с одновременно редактированием списка
for player in range(5):
    random.shuffle(players)
    loose = players.pop(0)
    print("Выбыл", loose)
    if len(players) == 1:
        print("Победитель", players[0])
        # break # остановка цикла - будем рассматривать позже