
#Згідно з завданням починаємо цикл
while True:
    #Введення вибору користувача
    user_choise = int(input("Отримати книжку - 1\nПовернути книжку - 2\nВихід - 3\n"))

    #одразу перевірка чи не хоче користувач вийти
    if user_choise == 3:
        break

    #якщо не хоче - збираємо додаткові дані
    user_name = input("Введіть ім'я: ")
    book_name = input("Введіть назву книжки: ")

    #одразу їх перевіряємо
    if user_name =="" or book_name == "":
        print("Ім'я або назва книжки не можуть бути порожні")
        continue

    if user_choise == 1:
        days = int(input("На скількі днів ви берете книжку?: "))

        #Перевіряємо чи правильна кількість днів
        if days <= 0:
            print ("Кількість днів не може бути від'ємна!")
            continue
        elif days > 30:
            print("Кількість днів не може більше 30!")
            continue
        else:
            print(f"Книжку {book_name} видано читачеві {user_name} на {days} д.")
    elif user_choise == 2:
        print(f"Читач {user_name} повернув книжку {book_name}")
    else:
        break