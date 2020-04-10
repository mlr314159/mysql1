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
        row=('BOB', 21, '1990-02-06 23:04:56')
        cursor.execute('INSERT INTO Friends VALUES(%s,%s,%s);', row)
        connection.commit()
        
finally:
    # Close the connection. regardless of whether the above was successfull
    connection.close()