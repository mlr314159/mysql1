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
        list_of_names = ['fred','bob','Jim']
        #prepare for SQL
        
        format_strings = ','.join(['%s']*len(list_of_names))

        str = ("DELETE FROM Friends WHERE name in ({});".format(format_strings) , list_of_names)
        print(str)
        row = cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings) , list_of_names)
        connection.commit()
        
finally:
    # Close the connection. regardless of whether the above was successfull
    connection.close()