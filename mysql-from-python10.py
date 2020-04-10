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
        rows = [(23,'Bob'), (24,'Jim'), (25,'Fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
        connection.commit()
        
finally:
    # Close the connection. regardless of whether the above was successfull
    connection.close()