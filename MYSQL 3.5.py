import mysql.connector
mydb=mysql.connector.connect(host='local host',
                             user='pooja',
                             password='passwd',
                             database='data_name')
mycursor=mydb.cursor()
mycursor.execute('show database')