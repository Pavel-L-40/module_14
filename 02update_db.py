import sqlite3
from random import randint

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
# ===> INSERT (ADD) < ===
# cursor.execute('INSERT INTO Users(username, email, age) VALUES (?,?,?)', ('Oleg','oleg@example.ru','24'))
for i in range(1,31):
    cursor.execute('INSERT INTO Users(username, email, age) VALUES (?,?,?)', (f'User{i}', f'user{i}@example.ru', randint(18,60)))

# ===> Update <===
# SET --> то что хотим изменить
# cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (18, 'Oleg'))

# ===> DELETE <===
cursor.execute('DELETE FROM Users WHERE username = ?',('Oleg',))

connection.commit() # <<- Сохраняем состояние
connection.close() #  <<= Закрываем соединение