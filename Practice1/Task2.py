# Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n = int(input("Enter a three digit number: "))
initVal = n
sum = 0
while n != 0:
    sum += n % 10
    n = n // 10

print(f"Sum of {initVal} digits is {sum}")
