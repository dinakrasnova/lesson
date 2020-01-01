'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

for i in range(1,6):
  print(i, 0)

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
sum = 0
for i in range(10):
    answer = int(input('Введите любую цифру: '))
    if answer == 5:
        sum += 1

print('Количество цифр 5 равно', sum)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1,101):
     sum+=i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
mult = 1
for i in range(1,101):
     mult*=i
print(mult)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

integer_number = 2129

print(integer_number%10,integer_number//10)
while integer_number>0:
     print(integer_number%10)
     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''

x = 444
print(sum(map(int,str(x))))

'''
Задача 7
Найти произведение цифр числа.
'''
x = 444
y = 1
for i in str(x):
    y *= int(i)
print(y)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
a = 1234
m = a%10
a = a//10
while a > 0:
    if a%10 > m:
        m = a%10
    a = a//10
print(m)

'''
Задача 10
Найти количество цифр 5 в числе
'''
integer_number = 5555666
count = 0
while integer_number>0:
    if integer_number%10 == 5:
        count += 1
    integer_number = integer_number//10
print(count)