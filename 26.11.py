# Завдання 1
# Створіть список чисел [1, 8, -5, 9]
# ● Виведіть на екран елементи цього списку
# ● Збільшіть кожне число в 3 рази та виведіть результат
# ● Замініть усі числа більші 10 на 0 та виведіть
# результат

# numbers = [1,8,-5,9]
# print(numbers)
#
# for number in range(len(numbers)):
#     numbers[number] *=3
#
# print(numbers)
#
# for number in range(len(numbers)):
#     if numbers[number] > 10:
#         numbers[number] = 0
#
# print(numbers)

# Завдання 2
# Користувач вводить числа, поки не введе -1.
# Збережіть усі ці числа в список. Виведіть їхню кількість,
# суму, мінімальне, максимальне та середнє.
# Скористайтесь функціями min, max, sum, len

user_list = []

# Ввід
while True:
    temp = int(input(""))
    if temp == -1:
        break

    user_list.append(temp)

# Вивід
print("Введений список: ", user_list)
print("Кількість елементів: ", len(user_list))
print("Сума елементів: ", sum(user_list))
print("Мінімум: ", min(user_list))
print("Міаксимум: ", max(user_list))
print("Середнье: ", sum(user_list) / len(user_list))
