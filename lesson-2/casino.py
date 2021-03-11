import random

guess_number = int(input("Выберете любое число: "))
limit = int(input("Выберете предел рандома: "))
random_number = random.randint(0, limit)
if random_number == guess_number:
    print("Выграйл")
else:
    print("Проиграл, было загаданно", random_number)