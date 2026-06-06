# print('heello')
# Текстовое представление для команды
# txt='(2+3)/0.25-4*2.1'
# Отображение выражения и вычисление результата:
# print(txt,"=", eval(txt))
# Считывание выражения для вычисления:
# res = input('Введите выражение:')
# print("Значение выражения:",eval(res))
# Список из чисел:
# nums = [5,10,1,60,25,3]
# Отображение списка из чисел:
# print('Список из чисел:', nums)
# Первый элемент:
# print('Первый элемент:',nums[0])
# Длина списка:
# print('Длина списка:',len(nums))
# Последний элемент:
# print('Последний элемент:', nums[-1])
# Наибольшее значение
# print('Наибольшее значение:', max(nums))
# Наименьшее значение:
# print('Наименьшее значение:', min(nums))
# Сумма:
# print("Сумма:",sum(nums))
# Список в обратном порядке:
# print('Список в обратном порядке:',list(reversed(nums)))
# Сортировка по возрастанию значений:
# print("По возрастанию значений:", sorted(nums))
# print("По убыванию значений:", sorted(nums, reverse=True))
# print('Исходный список:', nums)
# Изменение значения элемента списка:
# nums [1]='текст'
# print("После внесения изменений:",nums)
# Стр. 52
# Получение среза:
# print('Получение среза:', nums[1:len(nums)-1])
# Замена части элементов:
# nums[1:-1]=['A','B','C']
# print('Измененный список элементов', nums)
# Список чисел от 5 до 10:
# nums=list(range(5,10))
# print('Список чисел от 5 до 10', nums)
#  Удаление элементов из списка.
# nums[2:4]=[]
# print(nums)
# удаление последнег элемента:
# del nums [len(nums)-1]
# print('удален последний элемент', nums)
# Нечетные числа:
# nums = [2*k+1 for k in range(1,6)]
# print('Нечетные числа:', nums )
# nums = [2*k for k in range(1,6)]
# print(nums)
# Список из симоволов создается на основе текста:
# symbs  = list("Python")
# Два первых симовла:
# print('Два первых симовла:', symbs[:2])
# print ('Остальные символы:', symbs [-1:])
# Листинг 1.7 стр 58
# number = int(input("Введите целое число"))
# Если числа - четное:
# if number%2==0:
#    print("Число четное")
# if number==0:
#    print('Вы ввели 0')
# else:
#    print(' Нечетное')
# Листинг 1.8. Вычисление суммы
# Считывание верхней границы суммы:
# n = int(input("Укажите верхнюю границу суммы: "))
# Начальное значение для суммы:
# s=0
# Начальное значение индексной переменнной:
# k=0
# Оператор цикла для вычислений суммы:
# while k<n:
#    # Увеличение значения индексной переменной суммы:
#    k = k+1
# Прибавление слагаемого к сумме:
#    s = s+k
# Отображение результата:
# print("Суммы чисел от 1 до", n ,"равна", s)
# s = int(input('Ввыедите число:'))
# print(sum(list(range(1,s+1))))
# Листинг 1.9. Альтернативыйн способ вычисления
# Считываение количества слагаемых:
# n = input("Укажите количество слагаемых: ")
# Индексная переменная
# txt ='1'
# Индексная переменная:
# k = 1
# Оператор цикла для формирования текста с выражением для суммы натуральных чисел:
# while str(k) != n:
#    k += 1
#   # Добавление фрагмента к тексту с выражением для суммы натуральных чисел:
#  txt = txt+"+"+str(k)
# Отображение результата:
# print(txt,'=',eval(txt))
# Функция для отображения букв из переданного аргументов текста:
# Создаем функцию
# def show(txt):
# преобразование текста в список и его сортировка:
#    symbs = sorted(list(txt)) # list(txt) содержимое переменной txt  преобразуется в список
# Отображение содержимого списка:
#    print((symbs))
# Вызов функции: # стр 64
# show (list(reversed('russia'))
# Функция для вычисления суммы квадратов натуральных чисел:
# def sqsum(n):
#     nums = [k*k for k in range (1,n+1)]
#     return sum(nums)
# bob = str(input('Ввыедите число:'))
# show(bob)
# m=10
# print('Сумма квадратов чисел от 1 до',str(m)+':',sqsum(m))
# Задачи для самопроверки
# Напишите программу, в которой программа запрашивает у пользователя день и месяц а затем выводит сообщение
# о текущем дне и месяце
# day = int(input('Введите день:'))
# month = str(input('Введие месяц:'))
# print("дата:",day,month)
# year = int(input('enter today\'s year: '))
# year_of_birth = int(input('enter year of birth: '))
# print('you age:', year - year_of_birth)
# miles = float(input("Enter Miles: "))
# print(' Kилометры:',miles*1.6)
# n = int(input('Введите количество чисел в спиcке'))
# superlist = [2**k for k in range(0,n+1)]
# print(superlist)
# superlist = [5*k+3 for k in range(0,5)]
# superlis = (list(reversed(superlist)))
# print(superlis)
# print(superlist)
# n = int(input('введите число:'))
# if n % 3 == 0:
#     print('Число делится на 3 без остатка')
# else:
#     print("число не делится без остатка на 3 либо равно 0")
# from gc import disable
import random
from copy import deepcopy
from itertools import count, cycle
from urllib.request import proxy_bypass_registry
from warnings import resetwarnings

#
# n = int(input('число для которого вычисляется факториал:'))
# k = 1
# s = 1
# while k < n:
#     k = k + 1
#     s = s * k
# print(s)
# nums = 10
# a=1
# b=1
# k = 0
# list = [a,b]
# while k < nums:
#     k = k + 1
#     c = a + b
#     a = b
#     b = c
# делал в тачке пока ждал ТО
#  Листинг 2.1. Отображение состава числа
# Вводится число:
# number = int(input('Введите число: '))
# Пока число больше нуля:
# while number>0:
# Последняя цифра в числе:
# digit = number%10
# Отображение цифры:
# print('|'+str(digit),end='')
# Отбрасывается последняя цифра в числе:
# number = number//10
# Отображается последний разделитель:
# print("|")
# Листинг 2.2. Простые числа
# Вводится число:
# number = int(input("Введите число: "))
#  Верхняя граница для делителя:
# num = number//2
# Начальное значение делителя:
# k = 2
# Поиск делиетелей числа:
# while k<num:
# Если число делится на k:
# if number % k == 0:
#     print("Число не является простым")
# Завешение оператора цикла:
# break
# Если условие ложно:
# else:
# Увеличивается значение делителя:
# k = k + 1
# Блок выполняется, если не выполнена инструкция break:
# else:
#     print("Это простое число")
# print("Проверка завершена")

# Листинг 2.3. Поиск делителей числа
# Вводится число:
# number = int(input("Введите число: "))
# Сообщение о первом делителе числа:
# print("Делится на",1)
#  Начальное значение делителя:
# k=1
# Поиск делителей числа:
# while k<number//2:
# Значение делителя увеличивается на единицу
# k+=1
# Если k не является делителем числа:
# if number%k!=0:
# Завершение текущего цикла:
# continue
# Сообщение о делителе числа:
# print("Делится на", k)
# Сообщение о последнем делителе числа:
# print(" Делится на", number)

# Листинг 2.4. Делители числа
# number = int(input("Enter a number: "))
# k = 1
# while k <=number//2:
#     if number % k == 0:
#         print("Делитися на", k)
#     else:
#         print("Не делится на",k)
#     k=k+1
# print("Делится на", number)

# Оператор цикла for (стр. 81)
# Листинг 2.5. Перебор элементов списка
# Список с текстовыми элементами:
# # colors = ['Blue','Yellow','Green']
# Отображение содержимого списка:
# # print(colors)
# Перебор элементов списка:
# # for s in colors:
# #     print(s,'->',len(s))

# Листинг 2.6. Числа Фибоначчи
# # Количество чисел в последовательности:
# n = 15
# # Первые два числа:
# a, b = 1 , 1
# # Отображение первых двух чисел:
# print(a,b,end=' ')
# # За каждый цикл вычисляется одно новое число:
# for k in range(n-2):
#     # Вычисление нового числа в последовательности:
#     a, b = b, a+b
#     # Отображение нового числа:
#     print(b, end=' ')

# Листинг 2.7. Поиск букв в тексте
# Текст для поиска букв:
# mytext=input('Введите текст для проверки:')
# # Буквы для поиска:
# symbs = ['а','у','t']
# print("Ищем такие буквы: ", symbs)
# # Поиск букв:
# for s in symbs:
#     # Если буква найдена:
#     if s in mytext:
#         print("В тексте есть буква '"+s+"'")
#         # Завершение оператора цикла:
#         break
#     # Если буквы нет:
#     else:
#         print("В тексте нет буквы '"+s+"'")
# else:
#     print("Таких букв в тексте нет")
# print("Поиск завершен")

#  Условный оператор if
# Листинг 2.8. Решение линейного уравнения
# Вводятся параметры уравнения:
# a,b = eval(input("Введите через запятую два числа: "))
# Проверка типа введенных параметров:
# if (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float):
#     print("Уравнение "+str(a)+"x="+str(b))
# Если первый параметр ненулевой:
# if a!=0:
#     print("Решение x="+str(b/a))
# else:
#     if b!=0:
#         print("Решений нет!")
#     else:
#         print("Решение Любое число!")
# else:
#     print("Введены некорректные значения!")
#     raise SystemExit(0)
# print("Поиск решения завершен.")

# Листинг 2.9. Еще один способ решить уравнение:
# Вводятся парметры уравнения:
# # a,b = eval(input('Введите через запятую два числа:'))
# Если параметры некорректные:
# if (type(a)==int and type(a)==float) or (type(b)==int and type(b)==float):
#     print("Введены некорректные значения")
#     raise SystemExit(0)
# # Если первый параметр ненулевой:
# elif a!=0:
#     txt = "Решение  x="+str(b/a)
# # Если второй параметр ненулевой (При первом нулевом)
# elif b!=0:
#     txt= "Решений нет"
# else:
#     txt='Решение любое число!'
#
# # Вид уравнения:
# print("Уравнение "+str(a)+"x="+str(b))
# # Результат поиска корня:
# print(txt)
# print("Поиск решения завершен.")

# Листинг 2.10. Идентификация числа
# Текстовая переменная:
# res="Это число "
# # Вводится текст:
# txt = input("Введите название числа: ")
# # Преобразование в нижний регистр:
# txt = txt.lower()
# uptext = txt.upper()
# # Идентификация числа:
# if txt=="один" or txt == "единица" or txt == "раз":
#     res+="1"
# elif txt == "два" or txt == "двойка":
#     res+="2"
# elif txt == "три" or txt == "тройка":
#     res+="3"
# else: res+="Не идентицицировано"
# print(res+uptext)

# _________________________ Тернарный оператор
# Листинг 2.11. Проверка числа не четность/нечетность:
# ВВодится число:
# num = int(input("Введите число:"))
# Использование тернарного оператора:
# res='Четное' if num %2 == 0 else "Нечетное"
# Сообщение:
# print("Это "+res+" число")

# # Листнг 2.12. Значения разных типов и тернарный оператор
# # Вводится выражение:
# val = eval(input("Введите вражение: "))
# # Используется тернырный оператор:
# a, b = (val[0], val[-1]) if type(val) == str else (val, type(val))
# # Значения переменных:
# print(a)
# print(b)

# Обработка исключений
# print("Обработка исключений")
# Контролируемый код:
# try:
#     num = int (input("Введите целое число:"))
#     print("Вы ввели число ", num)
# except:
#     print("Нужно было ввести целое число! ")
# print("конец")
# print("Операции со списком чисел")
# python = [3,3,2,565,766,65]
# Контролируемый код:
# try:
#     nums = eval(input("Введите числовой список: "))
#     print("Получено значение: "+str(nums))
#     a = int(nums[0])
#     b = int(nums[3])
#     print(str(a)+"/"+str(b)+"="+str(a/b))
# Обработка исключений:
# except ValueError:
#     print("ValueError : Ошибка при преобразовании!")
# except ZeroDivisionError:
#     print("ZeroDivisionError: попытка деления на ноль!")
# except TypeError:
#     print('TypeError: недопустимая операция')
# except IndexError:
#     print('IndexError: неверный индекс элемента ')
# except SyntaxError:
#     print("SyntaxError: невозможно вычислить выражение!")
# except NameError:
#     print("NameError: неверный индентификатор")
# print("Завершение программы.")

# Листинг 2.15. Еще один способ обработки ошибок
# print("Операции со списком чисел...")
# try:
#     nums = eval (input("Введите числовой список: "))
#     print("Получено значение: "+str(nums))
#     a = int(nums[0])
#     b = int(nums[3])
#     print(str(a)+"/"+str(b)+"="+str(a/b))
# except ZeroDivisionError:
#     print("Ошибка деления на ноль")
# except IndexError:
#     print(' неверный индекс элемента')
# except:
#     print("Что-то пошло не так")
# print('Завершение программы')

# Задачи стр 122
# № 1
# try:
#     mynumbers = input("Enter a number: ")
#     print("Вы ввели: "+str(mynumbers))
# i = 0
# symbs = [0,1,2,3,4,5,6,7,8,9]
# listok = [int(k) for k in mynumbers]
# print(listok)
# i = 0
# while i < 10:
#     event_count = len([x for x in listok if x == i])
#     if event_count != 0:
#         print("цифра "+str(i)+" повторяется ", str(event_count), " раз")
#     i+=1
# except:
#     print("ошибка")

# Задача 2.
# number =(input("введите целое число "))
# number_list = [int(k) for k in number]
# print('вы ввели'+str(number_list))
# new_num_list = [-(i-9)  for i  in number_list ]
# print(new_num_list)

# Задача 3
# num_list = [123,45,6789]
# i = 0
# while i < len(num_list):
#     print(num_list[i],end='')
#     i+=1

# Задача 4
# list_1 = [2,2]
# list_2 = [2,3]
# i = 0
# if list_1 == list_2:
#     print("равны")
# else:
#     print("не равны")

# Задача 5
# numbers = [100,200,300,25,57,900,24]
# print('Список рандомный: ',numbers)
# uplevel = 25
# numbers_full = [x for x in range(1,uplevel+1)]
# print('Список от 1 до 10: ', numbers_full)
# i = 0
# while i < len(numbers_full):
#     if numbers_full[i] in numbers:
#         del numbers_full[i]
#     else:
#         i+=1
# print(numbers_full)

# Задача 6
# a = 3
# b = 5
# c = 1
# triangle = [a,b,c]
# print(triangle)
# i=0
# if (a < b + c) or (b < a + c) or (c < a + b):
#     print('Это трегульник')
# else:
#     print('Это не трегульник')

# Задача 7. Напишите программу, в которой пользователь вводит три целых чис
# ла, а программа проверяет, являются ли эти числа тремя последователь
# ными элементами арифметической последовательности. В арифметиче
# ской последовательности каждый новый член получается прибавлением
# к предыдущему определенного фиксированного числа
# a = 20
# b = 25
# c = 30
# arifm_posled = 5
# spisok = [a,b,c]
# print("подходит") if ((b == (a+arifm_posled)) and (c == (b+arifm_posled))) else print("no")

# Задача 8
# day = (input("Enter the day: "))
# if day == "1":
#     print("Понедельник")
# elif day == "2":
#     print("вторник")
# elif day == "3":
#     print("среда")
# else:
#     print("неверно")

# Задача 9
# try:
#     a = int(input("Введите число: "))
#     b = int(input("Введите число: "))
#     print(type(a))
#     if a == b:
#         print("числа равны")
#     else:
#         a = str(a)
#         b = str(b)
#         print(a+">"+b) if (a>b and a!=b) else print(a+"<"+b)
# except:
#     print("ok")

# Задача 10
# a = int(input("a: "))
# b = int(input("b: "))
# if a != 0:
#     x = ((b-1)/a)-1
#     print(x)
# elif a == 0 and b != 1:
#         print("решений нет")
# else:
#     if a == 0 and b == 1:
#         print("решение любое число")

# Знакомство с кортежами
# B = "Python",
# A = '1',
# print(B+A)
# print(tuple('re'))
# big = [43,'re']
# print(tuple(big))
# РАЗНЫЕ СПОСОБЫ СОЗДАНИЯ КОРТЕЖЕЙ
# Alpha = (5, 10, 15, 'двадцать')
# Bravo = 100, ['один', 'два', 'три'], 200
# Charlie = tuple([1, 2, 3, (4, 5, 6, 7, 8, 9)])
# Delta = tuple('ABCDEF')
# Echo = tuple(2 ** k for k in range(11))
# # Cчитывание значений элемента и получение среза:
# print('Alpha: ', Alpha)
# print('Элементов', len(Alpha))
# print('Первый: ', Alpha[0])
# print('Последний: ', Alpha[-1])
# print('Bravo: ', Bravo)
# print('Элементов: ', len(Bravo))
# print('Bravo[1]: ', Bravo[1])
# print("Bravo[1][2]: ", Bravo[1][2])
# print('Charlie: ', Charlie)
# print('Элементов: ', len(Charlie))
# print('Charlie[3]:', Charlie[3])
# print('Charlie[3][1:4]: ', Charlie[3][1:4])
# print('Delta: ', Delta)
# print('Элементов: ', len(Delta))
# print('Delta[-3:]: ', Delta[-3:])
# print('Echo: ', Echo)
# Foxtrot = tuple(Echo[k] for k in range(len(Echo)) if k % 2 == 0)
# print("Foxtrot: ", Foxtrot)
# Golf = Echo[2:5]
# print('Golf: ', Golf)
# # Листинг 3.2 Операции со списками
# # Создание списков:
# A = [10, 20, 30]
# print('______________________________________________________________________')
# print('A: ', A)
# B = ['Python', [1, 2]]
# print('B: ', B)
# # Вычисление суммы списков:
# C = A + B
# print("C: ", C)
# # Добавление элемента в конец списка
# C += [100]
# print("C: ", C)
# # Удаление элементов списка:
# C[1:2] = []
# print("C: ", C)
# # Добавление элемента в начало списка:
# C = [200] + C
# print('C: ', C)
# # Замена нескольких элементов в списке:
# C[:3] = ['A', 'B']
# print('C: ', C)
# # Вставка элементов в список:
# C[2:2] = [8, 9]
# print("C: ", C)
# # Присваивание значения элементу списка:
# C[2:3] = []
# print("C: ", C)
# print("--------------------операции с кортежами------------------------------")
# # Листинг 3.3 Операции с кортежами
# # Создание кортежей:
# A = (10, 20, 30)
# print("A: ", A)
# B = ('Python: ', (1, 2))
# print('B: ', B)
# # Вычисление суммы котрежей:
# C = A + B
# print("C: ", C)
# # Добавление элемента в конец кортежа:
# C += (100,)
# print('C: ', C)
# # Удаление элемента кортежа:
# C = C[:1] + C[2:]
# print('C: ', C)
# # Добавление элемента в начало кортежа:
# C = (200,) + C
# print('C: ', C)
# # Замена нескольких элементов в кортеж:
# C = ('A', 'B') + C[:3]
# print('C: ', C)
# # Вставка элементов  в кортеж:
# C = C[:2] + (8, 9) + C[2:]
# print('C: ', C)
# # Присваиваие значения элементу кортежа:
# C = C[:2] + C[3:]
# print('C:', C)
# # Создание выборки на основе списков и кортежей....................................................
# # Кортеж чисел:
# A = tuple(k for k in range(1, 21) if k % 3 != 0)
# print(A)
# # Список чисел:
# B = [2 ** (k // 2) if k % 2 == 0 else 3 ** (k // 2) for k in range(15)]
# print('B', B)
# # Cписок чисел:
# C = [0 if k == 0 or k == 1 else k ** 2 for k in range(13) if not k in [2, 5, 7]]
# print(C)
# # Кортеж в обратном порядке:
# Alpha = A[::-1]  # ?
# print(Alpha)
# # Элементы выбираются "через один", начиная с первого:
# # Bravo = B[::2]
# # print(Bravo)
# # Элементы выбираются через один начиная со второго:
# Charlie = B[1::2]
# print(Charlie)
# # Листинг 3.5. Умножение списков и кортежей на число
# Alpha = 5 * [0]
# print('-----------------', Alpha)
# Bravo = (1,) * 3
# print(Bravo)
# Charlie = [1, 2] * 3
# print(Charlie)
# Delta = [[1, 2]] * 3
# print(Delta)
# Echo = 4 * (1, [2, 3])
# print(Echo)
# Foxtrot = ([1] * 2) * 3
# print(Foxtrot)
# Golf = ([1] * 2,) * 3
# print(Golf)
# *A, B, C = 1, 2, 3, 4, 5, 6
# print(A, B, C)
# # Вложенные списки и кортежи стр 148
# # Листинг 3.6. Создание вложенные списков
# # Импорт функции для генерирования случайных чисел:
# from random import *
#
#
# # Функция для отображения вложенного списка:
# def show(A):
#     for a in A:
#         for s in a:
#             print(s, end=' ')
#         print('')
#
#
# # функция для создания вложенного списка из случайных чисел:
# def rands(m, n):
#     res = [[randint(0, 9) for i in range(n)] for j in range(m)]
#     return res
#
#
# # Функция для создания вложенного списка из букв:
# def symbs(m, n):
#     val = 'A'
#     res = [['' for i in range(n)] for j in range(m)]
#     for i in range(m):
#         for j in range(n):
#             res[i][j] = val
#             val = chr(ord(val) + 1)
#     return res
#
#
# # Создание вложенного списка:
# A = [[(j + 1) * 10 + i + 1 for i in range(5)] for j in range(0, 3)]
# print('Список А:', A)
# show(A)
# seed(2019)
# # Список случайных чисел:
# B = rands(3, 4)
# print("Список B:", B)
# # Отображение вложенного списка:
# show(B)
# # Список определяет количество строк во вложенном списке:
# size = [3, 5, 4, 6]
# # Создание вложенного списка:
# D = [['*' for k in range(s)] for s in size]
# print('Список D: ', D)
# print(show(D))
# # Список с буквами:
# C = symbs(3, 5)
# print("Список C: ", C)
# # Копирование списков и кортежей
# # Листинг 3.7. Присваивание списков
# # Исходный список
# A = [1, 3, 5]
# # Присваивание списков:
# B = A
# # Изменение значений элементов:
# B[1] = 'Python'
# A[2] = (10, 20)
# # Проверка результата:
# print(A)
# print(B)
# # Создание поверхностной копии Листинг 3.8.
# # Исходный список:
# A = [1, 3, [10, 20], 'Python', [40, 50]]
# # Создание поверхностной копии списка:
# B = A[:]
# C = A.copy()
# print("Исходные значения: ")
# print("A: ", A)
# print('B: ',B)
# print('C: ',C)
# # Внесение изменений в исходный список:
# A[0]=[100,200]
# A[2][1]=300
# A[3]='Java'
# A[4]=90
# C[4][1]='C++'
# print("После внесения изменений: ")
# print("A: ", A)
# print('B: ',B)
# print('C: ',C)
# # Листинг 3.9. Создание полной копии
# # Импорт функции для создания полной копии:
# from copy import deepcopy
# # Сисходный список
# A = [1,3,[10,20],'Python',[40,50]]
# # Создание полной копии списка:
# B = deepcopy(A)
# print("Исходные значения: ")
# print('A: ',A)
# print('B: ',B)
# # Внесение изменений в исходный список:
# A[0]=[100,200]
# A[2][1]=300
# A[3]='Java'
# A[4]=90
# print("После внесения изменений: ")
# print("A: ", A)
# print('B: ',B)
# Функции и методы для работы со списками:
# Листинг 3.10. Вставка и удаление элементов
# Размер списка:
# n = 10
# # Начальное значение для списка:
# A = [1, 1]
# # Заполнение списка:
# for k in range(n - 2):
#     A.append(A[-1] + A[-2])
# # проверка содержимого списка:
# print("A: ", A)
# # Пустой список
# # Изменение порядка элементов списка:
# for k in range(len(A) - 1):  # от 0 до 9
#     A.append(A.pop(-k - 2))
# # Проверка содержимого списка:
# print("A: ", A)
# # Удаление наибольшего элемента в списке:
# A.remove(max(A))
# print("A: ", A)
# # Удаление наиманьшего элемента в списке:
# A.remove(min(A))
# print("A: ", A)
# # Добавление эелмента в начало списке:
# A.insert(0, A[0] + A[1])
# print("A: ", A)
# # Пустой список:
# B = []
# # Часть элеентов одного списка переносится в другой:
# for k in range(len(A) // 2):
#     B.insert(0, A.pop(-1))
# print("A*: ", A)
# print("B*: ", B)
# # Добавление элемента в конец списка:
# A.append(B)
# print("A*: ", A)
# # Удаление последнего элемента в списке:
# A.pop(-1)
# print('A:,', A)
# # Добавление элементов в список:
# A.extend(B)
# print("A: ", A)
# # Листинг 3.11. Поиск и подсчет количества элементов
# # Подключение функции для генерирования случайных чисел:
# from random import *
#
# # инициализация генератора случайных чисел:
# seed(2019)
# # создание списка случайных чисел:
# A = [randint(10, 20) for k in range(15)]
# print("A: ", A)
# # Подсчет элементов с разными значениями:
# # for a in range(min(A), max(A)):
# #     print(a, '=', A.count(a))
# # Наибольшее , наименьшее и среднее значение:
# print('Наименьший: ')
# print('A[', A.index(min(A)), "]=", min(A), sep='')
# print("Наибольший:")
# print('A[', A.index(max(A)), "]=", max(A), sep='')
# print("Среднее: ", sum(A)/len(A))
# # сортировка списка
# B = sorted(A)
# A.sort(reverse=True)
# print("A: ", A)
# print("B: ", B)
# # Задача страница 170

# # Задача 1
# text = 'dasd12345678a'
# print(text)
# A = text[::3]
# print(A)

# print(' Следующая задача ------ 2 ___________________стр. 168________________')
# number = tuple(int(d) for d in str(input('ввои')))
# print(number)
# print(number[::-1])

# Задача 3
from random import *

seed(20123)

# 97 - 122 Напишите программу с функцией, которая создает вложенный список.
# Размеры списка указываются аргументами функции. Список заполняется случайными буквами.
# def symbs (m,n):
#     one_symbs = 'a'
#     res = [['' for i in range(n)] for j in range(m)]
#     for i in range(m):
#         for j in range(n):
#             res[i][j] = one_symbs
#             one_symbs=chr(randint(97,122))
#     return res
# print(symbs(3,4))

#
# Задача # 4___________________________________________________________
# Напишите программу, в которой есть функция для заполнения вложенного списка.
# Список заполняется натуральными числами «змейкой»:
# 1) сначала заполняется первая строка,
# 2) затем последний столбец (сверху вниз),
# 3) последняя строка (справа налево),
# 4) первый столбец (снизу вверх),
# 5) вторая строка (слева направо), и так далее
# def snake_matrix(n, m):
#     Создаем пустую матрицу n x m, заполненную нулями


# n, m = 5, 7
# matrix = [[0] * m for k in range(n)]
# print(matrix)
# visual(matrix)
# top, bot = 0, n - 1
# left, right = 0, m - 1
# num = 1
# while num <= n * m:
#     Первая строка
# for i in range(left, right + 1):
#     if num <= n * m:
#         matrix[top][i] = num
#         num += 1
# top += 1
#  последний столбец
# for i in range(top, bot + 1):
#     if num <= n * m:
#         matrix[i][right] = num
#         num += 1
# right -= 1
# нижняя строка
# for i in range(right, left - 1, -1):
#     if num <= n * m:
#         matrix[bot][i] = num
#         num += 1
# bot -= 1
# левый столбец
# for i in range(bot, top - 1, -1):
#     if num <= n * m:
#         matrix[i][left] = num
#         num += 1
# left += 1
# print(matrix)
# visual(matrix)
# n, m = 5, 4
# matrix = [[0] * n for _ in range(m)]
# print(matrix)
# num = 1
# индексы границ
# left, right = 0, n - 1  # n=4
# top, bot = 0, m - 1  # m=4
# while num <= m * n:
#     первая строка
# for i in range(left, right + 1):
#     if n <= n * m:
#         matrix[top][i] = num
#         num += 1
# top += 1
# последний стобец
# for i in range(top, bot + 1):
#     if n <= n * m:
#         matrix[i][right] = num
#         num += 1
# right -= 1
# нижняя строка
# for i in range(right, left-1, -1):
#     if n <= n * m:
#         matrix[bot][i] = num
#         num += 1
# bot -= 1
# первый столбец
# for i in range(bot,top-1, -1):
#     if n <= n * m:
#         matrix[i][left] = num
#         num += 1
# left += 1
# print(matrix)


# def visual(a):
#     for A in a:
#         for s in A:
#             print(s, end="|")
#         print('')
#
#
#
# def matricus(n,m):
#     matrix = [[0]*n for _ in range(m)]
#     num = 1
#     индексы
# left, right = 0, n - 1
# top, bot = 0, m - 1
# while num <= n * m:
#     for i in range(left, right+1):
#         if num <= n*m:
#             matrix[top][i] = num
#             num+=1
#     top+=1
#     for i in range(top,bot+1):
#         if num <= n*m:
#             matrix[i][right]=num
#             num+=1
#     right-=1
#     for i in range(right,left-1,-1):
#         if num <= n*m:
#             matrix[bot][i]=num
#             num+=1
#     bot-=1
#     for i in range(bot,top-1,-1):
#         if num <= n*m:
#             matrix[i][left]=num
#             num+=1
#     left+=1
# print(matrix)
# return matrix
#
# visual(matricus(5,5))

# Задача 5 Удаление стобцов из матрицы
# def visual_of_matrix(a):
#     print("Есть такая матрица: ")
#     for A in a:
#         for f in A:
#             print(f, end="|")
#         print("")


# line = 4
# graph = 4
# matrix = [[randint(1, 100) for i in range(line)] for j in range(graph)]
# visual_of_matrix(matrix)
# del_line = int(input('какую линию удалить?: '))
# del_graph = int(input('Какой столб удалить?: '))
#
# def del_line_and_graph(line, graph):
#     del matrix[line-1]
#     for i in range(len(matrix)):
#             del matrix[i][graph-1]
#     visual_of_matrix(matrix)
#
# del_line_and_graph(del_line, del_graph)
#
# Задача № 6 [3, 6, 4, 9, 7, 10, 3]
import time

# start_time = time.time()
# integers = [6, 0, 4, 100, 2, 1, 0]
# for k in range(len(integers)):
#     for i in range(1, len(integers) - k):
#         if integers[i - 1] > integers[i]:
#             integers[i - 1], integers[i] = integers[i], integers[i - 1]
# print(integers)
# end_time = time.time()
# print(end_time - start_time)
#

# Задача 7_________________________________

# def maxnum_and_index(integers):
#     maxnum_and_index = [max(integers), integers.index(max(integers))]
#     print(maxnum_and_index)
#     return maxnum_and_index
#
#
# numbers = [4, 3, 5, 67, 78, 8, 7, 78]
# maxnum_and_index(numbers)

# Задача 8 ________________________________________
# numbers = [randint(1, 120) for k in range(1, 20)]
# print(numbers)
# even = sorted([x for x in numbers if x % 2 == 0])
# print(even)
# odd = sorted([x for x in numbers if x % 2 == 1],reverse=True)
# print(odd)
# res = even + odd
# print(res)

# Задача 9
# numbers = [randint(1, 20) for k in range(1, 10)]
# print(numbers)
# i = 1
# while i < len(numbers):
#     numbers.insert(i,[(numbers[i-1]+numbers[i])])
#     i+=2
# print(numbers)
#
# Задача № 10
# numbers_one = [randint(1,10) for _ in range(10) ]
# seed = 23
# numbers_two = [randint(1,10) for _ in range(10) ]
# print(numbers_one)
# print(numbers_two)
# numbers_all = []
# for k in range(len(numbers_one)):
#     numbers_all.append(numbers_one[k])
#     numbers_all.append(numbers_two[k])
# print(numbers_all)

