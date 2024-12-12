import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMAPY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')

connection.commit() # <<- Сохраняем состояние
connection.close() #  <<= Закрываем соединение