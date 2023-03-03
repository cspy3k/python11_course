import pandas as pd

# df = pd.read_csv('csv_files/2019.csv', header=None, names=)
# print(df)

# df = pd.read_csv('csv_files/test.csv', header=None, names=['Name', 'DoB', 'City'], nrows=2)
# print(df)
# df.to_csv('csv_files/testcopy.csv', index=False, header=False, columns =['Name','City'])


# pd.set_option('display.max_rows', 160)
# pd.set_option('display.max_columns', 9)


# df = pd.read_csv('csv_files/2019.csv')
# print(df.head(10))
# print(df.tail(10))

df = pd.read_csv('csv_files/2019.csv')

people = {
    "name": ['Bob', 'Mary', 'Sarah'],
    "surname": ['Smith', 'Gold', 'Green'],
    'email':['bob@example.com', 'mary@example.com', 'sarah@example.com']
}

df = pd.DataFrame(people)
print(df['email'])
# print(df.email) # better do not use!!!
print(df['email'][0])

print(df[['name', 'email']])
