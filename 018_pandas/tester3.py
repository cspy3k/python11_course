import pandas as pd
import mysql.connector

# conn = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='gfhjkm12345',
#     database='sakila'
# )
# # conn.autocommit = True
# # mycursor = conn.cursor()
#
# df = pd.read_sql_query('SELECT * FROM actor', conn)
# print(df)

# df = pd.read_csv('csv_files/2019.csv')

# for index, row in df.iterrows():    # iterator
#     print(index, row)
#     print(row)
#     print(row['Country or region'])

# print(df.loc[df['Country or region'] == 'Estonia'])
# print(df.loc[df['GDP per capita'] > 1])

# print(df.loc[df['GDP per capita'] > 1])
# print(df.describe())
#
# print(df.memory_usage(deep=True))
# print(df.dtypes)
# print(type(df.loc[1, 'GDP per capita']))

pd.set_option('display.max_rows', 160)
pd.set_option('display.max_columns', 9)

df = pd.read_csv('csv_files/2019.csv')


# print(df.sort_values('Country or region', ascending=False))
# print(df.sort_values(['GDP per capita', 'Social support'],  ascending=False))
### print(df.sort_values(['Country or region', 'GDP per capita'],  ascending=[True, False])['Country or region', 'GDP per capita'])

#####?????? df['Total'] = df['GDP per capita'] + df['Generosity]' * 1000
# print(df)

# df.insert(loc=3, column='NEW COLUMN', value=(df['GDP per capita'] * 10000))
# print(df)
#
# df = df.drop(columns=['NEW COLUMN'])
# print(df)

# print(df.loc[df['Country or region'].str.contains('on')])

# print(df.groupby('Country or region').count())

a = df.nlargest(5, 'Overall rank')
b = df.nsmallest(5, 'Overall rank')

df2 = pd.read_csv('csv_files/test.csv')
# print(a)
# print(b)

print(pd.concat([a, b, df2]))

