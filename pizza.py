print("Вибрати піцу - 1\nПоказати все замовлення - 2\nВихід - 3")

margarita_amount = 0
peperoni_amount = 0
fourcheese_amount = 0

margarita_total = 0
peperoni_total = 0
fourcheese_total = 0

while True:
    user_choice = int(input())
    if user_choice == 1:
        print("Маргарита – 150 грн\nПепероні – 180 грн\nЧотири сири – 200 грн")
        pizza_name = input("Введіть назву піци: ")

        if pizza_name not in {"Маргарита", "Пепероні", "Чотири сири"}:
            print("Введена неправильна назва піци")
            continue

        pizza_amount = int(input("Введіть кількість піц: "))

        if pizza_name == "Маргарита":
            margarita_amount += pizza_amount
            margarita_total += pizza_amount * 150
        elif pizza_name == "Пепероні":
            peperoni_amount += pizza_amount
            peperoni_total += pizza_amount * 180
        elif pizza_name == "Чотири сири":
            fourcheese_amount += pizza_amount
            fourcheese_total += pizza_amount * 200

        print(f"Замовлено {pizza_name}, {pizza_amount} шт")
    elif user_choice == 2:
        print("\n========== ВАШЕ ЗАМОВЛЕННЯ ==========")
        print("Піца            Кількість  Вартість")
        print("-" * 38)
        if margarita_amount > 0:
            print(f"{'Маргарита':<15} {margarita_amount:<10} {margarita_total} грн")
        if peperoni_amount > 0:
            print(f"{'Пепероні':<15} {peperoni_amount:<10} {peperoni_total} грн")
        if fourcheese_amount > 0:
            print(f"{'Чотири сири':<15} {fourcheese_amount:<10} {fourcheese_total} грн")
        print("-" * 38)
        total = margarita_total + peperoni_total + fourcheese_total
        print("Загальна вартість: ", total, " грн")
        print("======================================")
        print("Дякуємо за замовлення!")

    else:
        break
