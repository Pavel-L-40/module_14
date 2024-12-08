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
# cursor.execute('SELECT username, email, age, balance From Users WHERE age != ?', (60,))
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')
# ----------------------------------------------------------------------------------------


# ========================================================================================
# ================================ task 14_2 =============================================

# cursor.execute('SELECT username, email, age, balance From Users')
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')
print('-----------------------------------------------------------------------------------')

#      ===>>> Удалите из базы данных not_telegram.db запись с id = 6 <<<===
# cursor.execute('DELETE FROM Users WHERE id = 6')
# ----------------------------------------------------------------------------------------

cursor.execute('SELECT username, email, age, balance From Users')
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')
print('-----------------------------------------------------------------------------------')

#                ===>>> Подсчитать общее количество записей <<<===
cursor.execute('SELECT COUNT(*) FROM Users')
total_count = cursor.fetchone()[0]
print(f'Общее количество строк составляет: {total_count}')
print('-----------------------------------------------------------------------------------')

#                   ===>>> Посчитать сумму всех балансов <<<===
cursor.execute('SELECT SUM(balance) FROM Users')
print(f'Сумма балансов всех пользователей составляет: {cursor.fetchone()[0]}')
print('-----------------------------------------------------------------------------------')

#          ===>>> Вывести в консоль средний баланс всех пользователей <<<===
cursor.execute('SELECT AVG(balance) FROM Users')
print(f'Средний баланс всех пользователей: {cursor.fetchone()[0]}')



connection.commit()
connection.close()

# ============================================ END =======================================
