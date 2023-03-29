# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Каждое число вводится с новой строки.

a1 = int(input("Enter the first element of the arithmetic progression: "))
d = int(input("Specify difference of the arithmetic progression: "))
n = int(input("Specify elements of the arithmetic progression number to be displayed: "))

a = [a1 + (i-1)*d for i in range(1, n+1)]

print(a)
