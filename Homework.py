# Первя задача
#square
length = int(input('Введите длинну стороны квадрта:'))

print("Вывод:")
square_perimetre = 4 * length
square_area = length * length
print(f'Периметр: {square_perimetre}')
print(f'Площадь: {square_area}')

#rectangle
length = int(input("Введите длину прямоугольника:"))
width = int(input("Введите ширину прямоугольника:"))

print("Вывод:")
rectangle_perimetre = 2 * (length + width)
rectangle_area = length * width

print(f'Периметр: {rectangle_perimetre}')
print(f'Площадь: {rectangle_area}')

# Вторая здача
salary = int(input('Введите заработную плату в месяц:'))
mortgage = int(
    input('Введите какой процент (%) от зарплаты уходит на ипотеку:'))
Life = int(input('Введите какой процент (%) от зарплаты уходит на жизнь:'))
print("\n")
print("Вывод:")
spent_mortgage = salary * (mortgage / 100) * 12
capital = (salary - (salary *  (mortgage + Life) / 100)) * 12
print(f'На ипотеку было потрачено: {spent_mortgage}')
print(f'Было накоплено: {capital }')

# Третья задача
#square
length = int(input('Введите длинну стороны квадрта:'))

print("Вывод:")
square_perimetre = 4 * length
square_area = length * length
print(f'Периметр: {square_perimetre}')
print(f'Площадь: {square_area}')

#rectangle
length = int(input("Введите длину прямоугольника:"))
width = int(input("Введите ширину прямоугольника:"))

print("Вывод:")
rectangle_perimetre = 2 * (length + width)
rectangle_area = length * width

print(f'Периметр: {rectangle_perimetre}')
print(f'Площадь: {rectangle_area}')

sign = input('Введите знак:')
print("Вывод:")
string_length = square_perimetre + rectangle_area
print(f'{sign * string_length}')


salary = int(input('Введите заработную плату в месяц:'))
mortgage = int(input('Введите какой процент (%) от зарплаты уходит на ипотеку:'))
Life = int(input('Введите какой процент (%) от зарплаты уходит на жизнь:'))
print("\n")
print("Вывод:")
spent_mortgage = salary * (mortgage / 100) * 12
capital = (salary - (salary *  (mortgage + Life) / 100)) * 12
print(f'На ипотеку было потрачено: {spent_mortgage}')
print(f'Было накоплено: {capital }')