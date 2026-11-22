print("Вибрати піцу - 1\nВихід - 2")

while True:
    user_choice = int(input())
    if user_choice == 1:
        pizza_name = input("Введіть назву піци: ")
        pizza_amount = int(input("Введіть кількість піц: "))
        print(f"Замовлено {pizza_name}, {pizza_amount} шт")
    else:
        break
