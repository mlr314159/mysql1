import os
import pymysql

# get username
# (modify this variable if runn ing on a different environment)
username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #  Run a query       
     with connection.cursor() as cursor:
        rows=[('Bob', 21, '1990-02-06 23:04:56'),
            ('Jim', 56, '1955-02-06 22:04:56'),
            ('Fred', 100, '1911-02-06 21:04:56')]
        
        cursor.executemany('INSERT INTO Friends VALUES(%s, %s, %s);', rows)
        connection.commit()
        
finally:
    # Close the connection. regardless of whether the above was successfull
    connection.close()