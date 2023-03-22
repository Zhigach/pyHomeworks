# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

def getNumberList():
    length = int(input("Enter number of list elements: "))
    print("Enter list values separated by newline")
    arr = list()
    for i in range(length):
        arr.append(int(input()))
    print("Finished!")
    return arr

def getIntersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return set1.intersection(set2)


arrayA = getNumberList()
arrayB = getNumberList()

print(getIntersection(arrayA, arrayB))
