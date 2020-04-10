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
        row = cursor.executemany('DELETE FROM Friends WHERE name= %s;', ['bob','Jim'])
        connection.commit()
        
finally:
    # Close the connection. regardless of whether the above was successfull
    connection.close()