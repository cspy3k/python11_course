import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='gfhjkm12345',
    database='sakila'
)
# conn.autocommit = True
mycursor = conn.cursor()

# mycursor.execute('CREATE TABLE student (name VARCHAR(100), age INTEGER(10))')
student1 =('Jack', 20)
mycursor.execute('INSERT INTO student (name, age) VALUES (%s, %s)', student1)
conn.commit()

