#Задача 1. Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.

for i in range (1, 6):
    print(i, 0, sep=".")

#Задача 2. Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.

a = 0
for i in range (10):
    s = int(input("Введите число: "))
    if s == 5:
        a += 1
print(a)

#Задача 3. Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
sum = 0
for i in range(1,101):
    sum += i
print("Сумма равна", sum)

#Задача 4. Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

a = 1
for i in range(1, 11):
    a *= i
print("Произведение чисел:", a)

#Задача 5. Вывести цифры числа на каждой строчке.
integer_number = 589134
print(integer_number%10,integer_number//10)

while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10

#Задача 6. Найти сумму цифр числа.

integer_number = 24468743
sum = 0
while integer_number>0:
    sum += integer_number%10
    integer_number = integer_number//10
print(sum)

#Задача 7. Найти произведение цифр числа.

integer_number = 24468743
a = 1
while integer_number>0:
    a *= integer_number%10
    integer_number = integer_number//10
print(a)

#Зачада 8. Дать ответ на вопрос: есть ли среди цифр числа 5?
integer_number = 215413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

#Задача 9. Найти максимальную цифру в числе

integer_number = int(input("Введите большое число: "))
max = 0
while integer_number > 0:
    if integer_number%10 > max:
        max = integer_number%10
    integer_number = integer_number//10
print(max)

#Задача 10. Найти количество цифр 5 в числе

integer_number = int(input("Введите несколько цифр: "))
sum = 0
while integer_number>0:
    if integer_number%10 == 5:
        sum += 1
    integer_number = integer_number//10
print(sum)