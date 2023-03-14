# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

def findSumOfDigits(number):
    sum = 0
    while number != 0:
        sum += number % 10
        number = number // 10
    return sum


n = int(input("Enter a six digit number: "))

firstPart = n // 1000
secondPart = n % 1000
lucky = ['not lucky', 'Lucky!']

print(f"Your ticket is {lucky[findSumOfDigits(firstPart) == findSumOfDigits(secondPart)]}")
