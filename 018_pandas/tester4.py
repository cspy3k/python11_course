import pandas as pd
import mysql.connector
import time
'''
Домашнее задание:
Для опроса на Stack Overflow (https://insights.stackoverflow.com/survey)
Написать программу, которая по выбору пользователя делает следующее:
1. Выводит данные о том сколько программистов является профессионалами и сколько хобби программистами. (столбец 'Hobbyist')
2. Выводит средний, максимальный и минимальный возраст (столбец 'Age') программистов
3. Выводит таблицу со странами (столбец 'Country'). Группирует, считает кол-во и выводит в порядке убывания.
4. Выводит таблицу с валютами (столбец 'CurrencyDesc'). Группирует и выводит в порядке убывания
'''

# https://tproger.ru/digest/data-science-python/#1

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)

df = pd.read_csv('csv_files/survey_results_public.csv')

print(df.shape)
# print(val_min)
# print(val_max)
# print(val_average)
# # print(vmax)
# x = (df['Hobbyist'].value_counts())
# print(x)
# print(x[0])
# print(x[1])
#
# print(df['Country'].value_counts())
# print(df['CurrencyDesc'].value_counts())


# print(df.groupby('Country').value_counts())
print(df.loc[0:64461, 'Country'].value_counts())