print("Введіть число (0 для виходу):")
while True:
    num = input("Ваше число: ") #помилка або тут
    if num == "0": # або тут
        print("Вихід з програми.")
        break
    print(f"Ви ввели: {num}")