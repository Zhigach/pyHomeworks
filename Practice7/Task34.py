# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
#
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
#
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
#
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


puhPoem = input("Winnie, print your poem: ")
phrases = [x.replace('-', '') for x in puhPoem.split(' ')]
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
countVowels = [sum([phrase.count(vowel) for vowel in vowels]) for phrase in phrases]
isRythmic = len(set(countVowels)) == 1
print(["Пам парам", "Парам пам-пам"][isRythmic])