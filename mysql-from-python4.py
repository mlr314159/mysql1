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
        cursor.execute('CREATE TABLE IF NOT EXISTS Friends(name char(20), age int, DOB datetime);')
        
finally:
    # Close the connection. regardless of whether the above was successfull
    connection.close()