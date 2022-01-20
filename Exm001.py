# 0 Вывести квадрат числа

a = int(input()) 
b = a**2
print(b)

# 1.По двум заданным числам проверять является ли первое квадратом второго

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = a == b*b
print(c)
# 2.Даны два числа. Показать большее и меньшее число

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a > b:
    print(f'{a} больше {b}')
else:
    print(f'{b} больше {a}')       

# 3.По заданному номеру дня недели вывести его название
# Можно же лучше 
day_of_week = ['пн','вт','ср','чт','пт','сб','вс']
day_numb = [1,2,3,4,5,6,7,8]
day = int(input('Введите число: '))

if day == day_numb[0]:
    print(day_of_week[0])
elif day == day_numb[1]:
    print(day_of_week[1])    
elif day == day_numb[2]:
    print(day_of_week[2])
elif day == day_numb[3]:
    print(day_of_week[3])
elif day == day_numb[4]:
    print(day_of_week[4])
elif day == day_numb[5]:
    print(day_of_week[5])
elif day == day_numb[6]:
    print(day_of_week[6])

# 4.Найти максимальное из трех чисел

def max(a,b,c):
    mx = a
    if b > mx:
        mx = b
    if c > mx:
        mx = c
    print(f'максимальное {mx}')
max(int(input('первое:')),int(input('второе:')),int(input('третье:')))                  

# 5.Написать программу вычисления значения функции y = f(a)

import math          

def sin(a):
    print(math.sin(a))
sin(10)

#6.Выяснить является ли число чётным

a = float(input('Введите число: '))
def even_numb(numb):
    res = numb % 2 == 0
    print(res)
even_numb(a)

#7. Показать числа от -N до N

numb_a = int(input('от '))
numb_b = int(input('до '))
ran = range(numb_a, numb_b+1)
numbers = list(ran)
print(numbers)

#8. Показать четные числа от 1 до N

numb = int(input('до '))
ran = range(0, numb+1, 2)
numbers = list(ran)
print(numbers)

