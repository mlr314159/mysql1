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
        names = ['jim','bob']
        row = cursor.execute("DELETE FROM Friends WHERE name in (%s,%s)", names)
        connection.commit()
        
finally:
    # Close the connection. regardless of whether the above was successfull
    connection.close()