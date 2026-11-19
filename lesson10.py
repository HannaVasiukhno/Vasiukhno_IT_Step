# Завдання 1
# Користувач вводить рядок та символ. Порахуйте скільки
# разів цей символ зустрічається у рядку.
# Зробіть двома способами:
# ● з методом count
# ● з циклом for
# Приклад:
# В “it is amazing” символ “і” зустрічається 3 рази

# Введення змінних
# user_row = input("Введіть рядок: ")
# user_symbol = input("Введіть символ: ")
# count = 0
# #
# # # Метод каунт
# count_symbol = user_row.count(user_symbol)
# print(f"В реченні \"{user_row}\" символ {user_symbol} зустрічається {count_symbol} р")
# #
# # # Цикл фор
# for ch in user_row:
#     if ch == user_symbol:
#         count +=1
# #
# print(f"В реченні \"{user_row}\" символ {user_symbol} зустрічається {count}р")

# Завдання 2
# Користувач вводить рядок. Виведіть наступну
# інформацію:
# ● кількість символів
# ● чи є там слово python
# ● кількість шиплячих літер – szh

# # Введення змінних
# user_row = input("Введіть рядок: ")
#
# # Розрахунки
# length = len(user_row)
# count_szh = user_row.count("s") + user_row.count("z") + user_row.count("h")
#
# # Вивід
# print("Кількість символів - ",length)
# if "python" in user_row:
#     print("Слово python є у тексті")
# else:
#     print("Слова python немає у тексті")
#
# print("Кількість шиплячих літер – szh - ", count_szh)

# Завдання 3
# Користувач вводить тест. Потрібно замінити всі пробіли
# на дефіси. Виправіть помилку в коді
#
# text = input("Введіть текст: ")
#
# result = text.replace(" ", "-")
# print(f"Змінений текст: {text}") <-- Помилка тут, не та змінна

# виправлений код
# text = input("Введіть текст: ")
# result = text.replace(" ", "-")
# print(f"Змінений текст: {result}")
