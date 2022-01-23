import random 

# 0 Вывести квадрат числа

# a = int(input()) 
# b = a**2
# print(b)

# 1.По двум заданным числам проверять является ли первое квадратом второго

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = a == b*b
# print(c)
# 2.Даны два числа. Показать большее и меньшее число

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# if a > b:
#     print(f'{a} больше {b}')
# else:
#     print(f'{b} больше {a}')       

# 3.По заданному номеру дня недели вывести его название
# Можно же лучше 
# day_of_week = ['пн','вт','ср','чт','пт','сб','вс']
# day_numb = [1,2,3,4,5,6,7,8]
# day = int(input('Введите число: '))

# if day == day_numb[0]:
#     print(day_of_week[0])
# elif day == day_numb[1]:
#     print(day_of_week[1])    
# elif day == day_numb[2]:
#     print(day_of_week[2])
# elif day == day_numb[3]:
#     print(day_of_week[3])
# elif day == day_numb[4]:
#     print(day_of_week[4])
# elif day == day_numb[5]:
#     print(day_of_week[5])
# elif day == day_numb[6]:
#     print(day_of_week[6])

# 4.Найти максимальное из трех чисел

# def max(a,b,c):
#     mx = a
#     if b > mx:
#         mx = b
#     if c > mx:
#         mx = c
#     print(f'максимальное {mx}')
# max(int(input('первое:')),int(input('второе:')),int(input('третье:')))                  

# 5.Написать программу вычисления значения функции y = f(a)

# import math          

# def sin(a):
#     print(math.sin(a))
# sin(10)

#6.Выяснить является ли число чётным

# a = float(input('Введите число: '))
# def even_numb(numb):
#     res = numb % 2 == 0
#     print(res)
# even_numb(a)

#7. Показать числа от -N до N

# numb_a = int(input('от '))
# numb_b = int(input('до '))
# ran = range(numb_a, numb_b+1)
# numbers = list(ran)
# print(numbers)

#8. Показать четные числа от 1 до N

# numb = int(input('до '))
# ran = range(0, numb+1, 2)
# numbers = list(ran)
# print(numbers)

#9. Показать последнюю цифру трёхзначного числа

# def last_number(a):
#     return a % 10
# print(last_number(145))

#10. Показать вторую цифру трёхзначного числа

# def second_number(a):
#     return a % 100 // 10
# number = int(input('Введите число: '))
# print(second_number(number))

#11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

# numbers = random.randint(10,99+1)
# print(numbers)
# def max_numb(num):
#     if num // 10 > num % 10:
#         return num // 10
#     else:
#         return num  % 10
# print()
# print(max_numb(numbers))   

#12.Удалить вторую цифру трёхзначного числа

# number = int(input('Введите число: '))
# def dell_numb(numb):
#     first = numb // 100
#     last = numb % 10
#     return first * 10 + last
# print(dell_numb(number))

#13.Выяснить, кратно ли число заданному, если нет, вывести остаток.
# number_one = int(input('Введите число: '))
# number_two = int(input('Введите число: '))

# def multip(numb_1, numb_2):
#     if numb_1 % numb_2 == 0:
#         print('Ok')
#     else:
#         print(numb_1 % numb_2)
# multip(number_one, number_two)

#14.Найти третью цифру числа или сообщить, что её нет
number = int(input('Введите число: '))

def find_numb_3(numb):
    if 1000 > numb > 100:
        return print(numb % 10)
    elif numb > 1000:
        return print((numb % 100) // 10)  
    else:
        return print('not found')

find_numb_3(number)
