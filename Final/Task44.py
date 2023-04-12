# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

print(data.head(n=20))

fields = list(set(data['whoAmI']))

one_hot_data = pd.DataFrame(columns=fields)

for i in range(len(data['whoAmI'])):
    # print([data['whoAmI'][i] == f for f in fields])
    one_hot_data.loc[i] = [[0, 1][data['whoAmI'][i] == f] for f in fields]

print('\nSource dataset in one hot format:')
print(one_hot_data.head(n=20))
