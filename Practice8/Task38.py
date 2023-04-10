# Задача 38. Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

fields = ["id","Фамилия", "Имя", "Телефон", "Описание"]

def showMenu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить/удалить запись в книге\n"
          "4. Найти абонента по номеру телефона\n"
          "5. Добавить абонента в справочник\n"
          "6. Закончить работу")
    choice = int(input())
    return choice


def editMenu():
    print("Выберите необходимое действие:\n"          
          "1. Изменить Фамилию\n"
          "2. Изменить Имя\n"
          "3. Изменить Номер телефона\n"
          "4. Изменить Описание\n"
          "5. Удалить запись. ВНИМАНИЕ! Имзенения будут необратимы\n"
          "6. Завершить редактирование")
    choice = int(input())
    return choice


def removeRecord(data, index):
    data.remove(data[index])


def readCSV(filename: str):
    data = list()
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def printPhonebook(data: list):
    for record in data:
        print(',\t\t'.join("{}: {}".format(k, v) for k, v in record.items()))
    input("Для продолжения нажмите клавишу Enter ")


def findByLastName(data):
    family = input("Введите фамилию абонента: ")
    foundList = list()
    for record in data:
        if family in record['Фамилия']:
            foundList.append(record)
            print(',\t\t'.join("{}: {}".format(k, v) for k, v in record.items()))

    if len(foundList) == 0:
        print("Указанная фамилия не найдена\n")
        input("Для продолжения нажмите клавишу Enter ")
        return
    elif len(foundList) == 1:
        index = 0
    elif len(foundList) > 1:
        print("Найдено несколько абонентов")


def editRecord(data):
    index = int(input("Введите ID записи, которую необходимо изменить: ")) - 1
    choise = 0
    while choise != 6:
        choise = editMenu()
        if choise == 1:
            data[index]['Фамилия'] = input("Введите новую Фамилию: ")
            print("Изменения приняты\n")
        if choise == 2:
            data[index]['Имя'] = input("Введите новое Имя: ")
            print("Изменения приняты\n")
        if choise == 3:
            data[index]['Телефон'] = input("Введите новый Номер телефона: ")
            print("Изменения приняты\n")
        if choise == 4:
            data[index]['Описание'] = input("Введите Описание для абонента: ")
            print("Изменения приняты\n")
        if choise == 5:
            removeRecord(data, index)
    savePhonebook(data)


def findByNumber(data):
    number = input("Введите телефон абонента: ")
    flag = True
    for record in data:
        if record['Телефон'] == number:
            flag = False
            print(',\t\t'.join("{}: {}".format(k, v) for k, v in record.items()))
    if flag:
        print("Указанный номер не найден\n")
    input("Для продолжения нажмите клавишу Enter ")


def addRecord(data):
    newData = list()
    newData.append(str(int(data[-1]["id"])+1))
    for i in range(1, len(fields)):
        newData.append(input(f"Введите {fields[i]} абонента: "))
    newRecord = dict(zip(fields, newData))
    data.append(newRecord)

    print(',\t\t'.join("{}: {}".format(k, v) for k, v in newRecord.items()))
    input("Для продолжения нажмите клавишу Enter")
    print("Новая запись добавлена: ")
    savePhonebook(data)


def savePhonebook(data):
    with open('phonebook.csv', 'w', encoding='utf-8') as new_file:
        for record in data:
            new_file.write(','.join(record.values())+'\n')
    print("Телефонный справочник сохранен")


phonebook = readCSV("phonebook.csv")

choise = 0
while choise != 6:
    choise = showMenu()
    if choise == 1:
        printPhonebook(phonebook)
    if choise == 2:
        findByLastName(phonebook)
    if choise == 3:
        editRecord(phonebook)
    if choise == 4:
        findByNumber(phonebook)
    if choise == 5:
        addRecord(phonebook)

