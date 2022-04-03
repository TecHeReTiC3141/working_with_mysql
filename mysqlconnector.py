from getpass import getpass
import mysql.connector

accounts = [(1, 500, .25),
            (2, 750, .15),
            (3, 150, 0.2)]
with mysql.connector.connect(host='localhost',
    user='Tec',
    passwd='TecHeres3141',
    database='testconnector') as db:
    assert db.is_connected(), 'problems with connection'
    cursor = db.cursor(buffered=True)
    cursor.execute("""SELECT id FROM users""")
    # db.commit()
    # cursor.execute('SELECT * FROM USERS')
    for x in accounts:
        cursor.execute('''INSERT INTO bank_account (userid, bill, percent)
         VALUES (%s, %s, %s)''', x)
    db.commit()
    cursor.execute('''SELECT * FROM bank_account''')
    print(*cursor, sep='\n')