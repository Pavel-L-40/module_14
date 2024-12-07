import sqlite3
import random

connection= sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
# ----------------------------------------------------------------------------------------

#            ===>>> Создайте таблицу Users, если она ещё не создана <<<===

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')
# ----------------------------------------------------------------------------------------

#                    ===>>> Заполните её 10 записями <<<===
# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, age, email, balance) VALUES (?,?,?,?)', (f'User{i}', str(random.randrange(10, 80, 10)), f'example{i}@gmail.com', str(random.choice([500, 1000, 1500]))))
# ----------------------------------------------------------------------------------------

#        ===>>> Обновите balance у каждой 2ой записи начиная с 1ой на 500 <<<===
# for i in range(1,11,2):
#     cursor.execute('UPDATE Users SET balance = 500 WHERE username = ?', (f'User{i}',))
# ----------------------------------------------------------------------------------------

#            ===>>> Удалите каждую 3ую запись в таблице начиная с 1ой <<<===
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))
# ----------------------------------------------------------------------------------------

# cursor.execute('UPDATE Users SET age = 60 WHERE username = ?', ('User3',))

#     ===>>> Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль <<<===
cursor.execute('SELECT username, email, age, balance From Users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')
# ----------------------------------------------------------------------------------------

connection.commit()
connection.close()

# ============================================ END =======================================
