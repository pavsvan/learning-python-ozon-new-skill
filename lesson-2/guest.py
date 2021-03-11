guests = []
guest1 = input("Введите имя первого гостя: ")
guests.append(guest1.strip().title())
guest2 = input("Введите имя второго гостя: ")
guests.append(guest2.title().strip())
guests.sort()

print("Приглашаем вас", guests[0])
print("Приглашаем вас", guests[1])
