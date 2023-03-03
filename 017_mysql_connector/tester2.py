import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='gfhjkm12345',
    database='sakila'
)
conn.autocommit = True
mycursor = conn.cursor()

mycursor.execute('SELECT * FROM actor')

# result = mycursor.fetchone()
# print(result)
# result = mycursor.fetchone()
# print(result)

result = mycursor.fetchall()
print(result)

result = mycursor.fetchmany(5)
print(result)
