import sqlite3

# >>> INITIAL FILE <<<
connection = sqlite3.connect('database.db')
cursor = connection.cursor()


# ===> CREATE TABLE <===
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')
#=======================================================================================================================

# cursor.execute('SELECT * FROM Users') # Все столбики / Все пользователи

# cursor.execute('SELECT username, age FROM Users WHERE age>?',(45,)) # Выборка пользователей по параметрам

cursor.execute('SELECT username, age FROM Users ORDER BY age')

users = cursor.fetchall()
for i in range(len(users)):
    print(i,users[i])

connection.commit() # <<- Сохраняем состояние
connection.close() #  <<= Закрываем соединение