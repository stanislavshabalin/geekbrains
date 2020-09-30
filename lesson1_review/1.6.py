# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

start_distance = int(input('Введите начальную дистанцию: '))
target_distance = int(input('Введите дистанцию, которую необходимо достичь: '))
current_distance = start_distance
day_number = 1

while current_distance < target_distance:
    current_distance = current_distance * 1.1
    day_number += 1
print('Количество дней, необходимых для достижения результата', day_number)