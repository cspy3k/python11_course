import pandas as pd
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


while True:
    print('\n\n\n\n'
          '1. Professionals/Hobbyists number\n'
          '2. Mean/Max/Min age\n'
          '3. Countries\n'
          '4. Currencies\n')
    x = input('Choose the option 1-4,"Q" or "q" to stop program executing >>> ').lower()
    if x in '1234q' and x != '':
        print('\n')
        if x == 'q':
            quit()
        if x == '1':
            data = (df['Hobbyist'].value_counts())
            print(f' Hobbyists: {data[0]}')
            print(f' Professionals: {data[1]}')
        if x == '2':
            print(' Age average: ', round((df['Age'].mean()), 1))
            print(' Age max: ', df['Age'].max())
            print(' Age min: ', df['Age'].min())
        if x == '3':
            print(df['Country'].value_counts().to_string())
        if x == '4':
            print(df['CurrencyDesc'].value_counts().to_string())
        input('\nPress <Enter> to continue...')
        continue
    else:
        print('\ninput error!')
        time.sleep(1)
        continue
