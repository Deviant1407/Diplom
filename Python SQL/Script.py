import sqlite3

def Connect_DB ():
    conn = sqlite3.connect("DB.db")

    return conn

def Use_DB (db : sqlite3.Connection, qwery):
    cursor = db.cursor()

    cursor.execute(qwery)

    return cursor.fetchall()

def Close_DB (db : sqlite3.Connection):
    db.close()


DB = Connect_DB()

List = Use_DB(DB, "SELECT * FROM `User`;")

Name1 = List[0][1]
Name2 = List[1][1]
Name3 = List[2][1]

print(f'Первое имя: {Name1}')
print(f'Второе имя: {Name2}')
print(f'Третье имя: {Name3}')

Close_DB(DB)