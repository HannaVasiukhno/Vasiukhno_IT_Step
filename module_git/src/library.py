

while True:
    user_choise = int(input("Отримати книжку - 1\nВихід - 2\n"))
    if user_choise == 1:
        user_name = input("Введіть ім'я: ")
        book_name = input("Введіть назву книжки: ")
        print(f"Книжку {book_name} видано читачеві {user_name}")
    else:
        break