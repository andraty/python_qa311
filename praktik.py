# Задача 4.
# Составить функцию для замены всех отрицательных элементов
# одномерного списка их модулями и подсчета числа таких замен.
# Применяя эту функцию, изменить каждый из двух заданных списков
# A(n) и B(m). Вывести сообщение, в каком из списков больше число замен.

# import random
#
# def zapoln():
#     a = []
#
#     for i in range(10):
#         a.append(random.randint(-10, 10))
#     return a
#
# def zamena_negativ_number(a):
#     count = 0
#     for i in range(len(a)):
#         if a[i] < 0:
#             a[i] = abs(a[i])
#             count += 1
#     print(f"Количество замен = {count}.")
#     return a, count
#
# a_n = zapoln()
# b_m = zapoln()
#
# a_n_p = zamena_negativ_number(a_n)
# b_m_p = zamena_negativ_number(b_m)
#
# if a_n_p[1] > b_m_p[1]:
#     print("")

# print(f"Начальный список {a_n}")
# print()


#Задание 3
# Составить функцию, возвращающую True, если все элементы
# одномерного списка упорядочены по убыванию их значений.
# И False в противном случае. Используя эту функцию, вывести заданные
# списки A(n) и B(m), в которых элементы не упорядочены в порядке
# убывания их значений. В противном случае вывести сообщение "Упорядочен"


# a_n = [0, 1, 2, 3, 4, 5, 6, 7]
# b_m = [7, 6, 5, 4, 3, 2, 1, 0]
# sorted(a_n, reverse=True)
# a_n.sort(reverse=True)

import random

def zapoln():
    a = []
    for i in range(10):
        a.append(random.randint(0, 100))
    return a

def sort_proverka(a):
    count = 0
    count_1 = 0
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            count += 1
        elif a[i] > a[i+1]:
            count_1 += 1
    if count == len(a)-1:
        print("False - отсортирован по возрастанию")
    elif count_1 == len(a)-1:
        print("True - отсортирован по убыванию")

a_n = zapoln()
print(a_n)
a_n_s = sorted(a_n, reverse=False)
print(a_n_s)
sort_proverka(a_n_s)

b_m = zapoln()
print(b_m)
b_m_s = sorted(b_m, reverse=True)
print(b_m_s)
sort_proverka(b_m_s)