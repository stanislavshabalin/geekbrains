# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
# сохраните в переменные, выведите на экран.

string = input('Введите строку: ')
number = int(input('Введите целое число: '))
float_number = float(input('Введите число с плавающей точкой: '))

print(f'Введенная строка: {string} \nВведенное целое число: {number} \nFloat: {float_number}')
print(f'Произведение чисел: {number*float_number}')