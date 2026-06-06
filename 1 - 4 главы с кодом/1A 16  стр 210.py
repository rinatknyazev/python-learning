# # Задача 1: 5 чисел от 1 до 10
# # __________10 чисел от 10 до 30
# from random import *
#
# seed = 202
# count = 15
# nums = set()
#
# while len(nums) < 5:
#     nums.add(randint(1, 10))
# while len(nums) < 15:
#     nums.add(randint(10, 30))
# print(len(nums))
# print(nums)
#
# print('hello')
# Задача 2.
# input_one = (input(f'Введите первое число:'))
# input_two = (input('Введите второе число:'))
# A = set(input_one)
# B = set(input_two)
# C = A&B
# print(C)
#
# Задача №3
# Гласные буквы а.е.ё.и.о.у.ы.э.ю.я.
# glas = 'аеёиоуэюя'
# text = 'иарогв'
# A = {k for k in glas}
# B = {k for k in text}
# C = A&B
# print(f"C = {C}")
# Задача 4
# Делится на 3 и на 4, но не делятся на 3 и на 4 одновременно
# Верхняя граница для чисел:
# n = 50
# Создание множества
# number = set(range(1, n + 1))
# print(f' number = {number}')
# A = {s for s in number if (s % 3 == 0 or s % 4 == 0) and (s % 3 != 0 and s % 4 != 0)}
# B = {s for s in number if s % 3 != 0 and s % 4 != 0}
# print(f' Делится на 3 и на 4 A = {A}')
# print(f' Не делятся на 3 и на 4 одновременно B: {B}')

# Задача 5 (1,3)(3,5)(5,7)
# A = set()
# n = 0
# k = (1, 3)
# while n < 10:
#     A.add(k)
#     n+=1
#     k = (k[1],k[1]+2)
# print(A)

# # Задача 6.
# # num = int(input("Введите число:"))
# A = 5
# numbers = [s for s in range(1,A+1)]
# print(f'numbers: {numbers}')
# # На основе списка создается словарь:
# nums_dict = {numbers[s]: s for s in range(len(numbers))}
# # n - счетчик циклов
# print(f'Исходный словарь: {nums_dict}')
# n=1
# m = -1
# while n<len(nums_dict)+1:
#     nums_dict[n] = numbers[m]
#     m -= 1
#     n+=1
# print(f'nums_dict: {nums_dict}')
# ______________ Задача 7
# text = 'ABBCfffAB'
# dict_of_letters = {symbs: text.count(symbs) for symbs in set(text)}
# print(dict_of_letters)
# print(dict_of_letters)
# __________ Задача 8
# writer_work = dict(Булгаков = "Мастер и Маргарита", Пушкин =  "Евгений Онегин", Достоевский = 'Преступление и наказание')
# bulgakov = input("Кто написал Мастер и Маргарита?:")
# dostoevskiy = input('Кто написал "Преступление и Наказание?:')
# pushkin = input('Кто написал Евгений Онегин?:')
# Счетчик правильных ответов n
# n=0
# myweek = {d: days.index(d) for d in days}
# if bulgakov == 'Булгаков':
#     print('Верно')
#     n+=1
# if dostoevskiy == 'Достоевский':
#     print('Верно')
#     n+=1
# if pushkin == 'Пушкин':
#     print(f'Верно')
#     n+=1
# print(f'Правильных ответов: {n}')
# _______________________Задача 9
# text = 'qwyertyy'
# # Создание пустого словаря для результата:
# result_dict = {}
# for index in range(len(text)):
#     char = text[index] # char каждый элемент 'text'
#     if char not in result_dict:
#         result_dict[char] = text[:index]+text[index+1:]
# print(result_dict)

# # Задача 10
# # animals = {"Leo": 1, "2": 3}
# # human = {"2": 12, "Вова": 14}
# # Создаем пустой словаь для результата:
# # result_dict = {}
# # Находим те ключи, которые есть в обоих словарях
# # для этого используем пересечение множества &
# common_keys = animals.keys() & human.keys()
# # Перебираем общие ключи
# for key in common_keys:
#     # Создаем множество из значений обоих словарей для этого ключа
#     # Фигурные скобки {} через запятую автоматически создают множество (set)
#     result_dict[key] = {animals[key], human[key]}
# print(result_dict)
