from random import choice
import sqlite3
# >>> connect
connection = sqlite3.connect('not_telegram.db')
cursor= connection.cursor()
# >>> create table
# !!!important!!! |id INTEGER PRIMARY KEY| <<<== not INT
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INT,
balance INT NOT NULL)
''')
# >>> delete id = 6 ====================================================================================================
cursor.execute('DELETE FROM Users WHERE id=?', (6,))
# >>> count all row >>> ================================================================================================
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print(total_users)
# >>> sum all balances >>> =============================================================================================
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(all_balances)
# >>> average balance >>> ==============================================================================================
cursor.execute('SELECT AVG(balance) FROM Users')
average = cursor.fetchone()
print(*average)
# ======================== Согласно ТЗ: ======================
print('print(all_balances / total_users)')
print(all_balances/total_users)
# >>> review param =====================================================================================================
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    print(user)
# >>> close connection >>> =============================================================================================
connection.commit() # <<- Сохраняем состояние
connection.close() #  <<= Закрываем соединение
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> END MODULE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
