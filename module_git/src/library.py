

while True:
    user_choise = int(input("Отримати книжку - 1\nПовернути книжку - 2\nВихід - 3\n"))
    if user_choise == 1:
        user_name = input("Введіть ім'я: ")
        book_name = input("Введіть назву книжки: ")
        days = int(input("На скількі днів ви берете книжку?: "))
        print(f"Книжку {book_name} видано читачеві {user_name} на {days} д.")
    elif user_choise == 2:
        user_name = input("Введіть ім'я: ")
        book_name = input("Введіть назву книжки: ")
        print(f"Читач {user_name} повернув книжку {book_name}")
    else:
        break