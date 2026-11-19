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
#
# # Метод каунт
# print(f"В реченні \"{user_row}\" символ {user_symbol} зустрічається
# {user_row.count(user_symbol)}р")
#
# # Цикл фор
# for ch in user_row:
#     if ch == user_symbol:
#         count +=1
#
# print(f"В реченні \"{user_row}\" символ {user_symbol} зустрічається {count}р")

# Завдання 2
# Користувач вводить рядок. Виведіть наступну
# інформацію:
# ● кількість символів
# ● чи є там слово python
# ● кількість шиплячих літер – szh

# Введення змінних
user_row = input("Введіть рядок: ")

# Розрахунки
user_symbol_amount = len(user_row)
count_python = user_row.count("python")
count_szh = user_row.count("s") + user_row.count("z") + user_row.count("h")

# Вивід
print("Кількість символів - ", user_symbol_amount)
if count_python:
    print("Слово python є у тексті")
else:
    print("Слова python немає у тексті")

print("Кількість шиплячих літер – szh - ", count_szh)
