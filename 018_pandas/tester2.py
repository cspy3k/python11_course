import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='gfhjkm12345',
    database='sakila'
)
# conn.autocommit = True
# mycursor = conn.cursor()

df = pd.read_sql_query('SELECT * FROM actor', conn)
print(df)

# df = pd.read_csv('csv_files/2019.csv')

# series/dataframe type

# print(df.iloc[0]) # working with indexes
# print(df.iloc[0:10])
# print(df.iloc[[3, 10, 123]])
# print(df.iloc[0:5, [1, 3]])

# print(df.loc[0:5, 'Country or region':'Freedom to make life choices']) # выборка включительна

# print(df.shape) # выдаёт размерность в кортеже: (строчки, столбцы)
# print(df['Country or region'].value_counts())
