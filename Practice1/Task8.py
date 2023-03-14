# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

def isMultipleOf(number, divider):
    return number % divider == 0


m = int(input("Введите длину n шоколадки в дольках: "))
n = int(input("Введите ширину m шоколадки в дольках: "))
k = int(input("Введите желаемое число долек шоколада: "))

if k > m*n:
    print("Введены неправильные условия")
    exit(1)

available = ['нельзя отломить', 'можно отломить']

print(f"От шоколадки с рамерами {m}x{n} долек {available[isMultipleOf(k,n) or isMultipleOf(k,m)]} {k} долек одним разломом")
