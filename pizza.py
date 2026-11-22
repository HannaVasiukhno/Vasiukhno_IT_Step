print("Вибрати піцу - 1\nВихід - 2")

while True:
    user_choice = int(input())
    if user_choice == 1:
        print("Маргарита – 150 грн\nПепероні – 180 грн\nЧотири сири – 200 грн")
        pizza_name = input("Введіть назву піци: ")
        if pizza_name not in {"Маргарита", "Пепероні", "Чотири сири"}:
            print("Введена неправильна назва піци")
            continue
        pizza_amount = int(input("Введіть кількість піц: "))
        print(f"Замовлено {pizza_name}, {pizza_amount} шт")
    else:
        break
