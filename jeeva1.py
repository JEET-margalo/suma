import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="MySQL@123", auth_plugin='mysql_native_password',database="mypythondb")
mycursor = mydb.cursor()
mycursor.execute("show tables")
for x in mycursor:
    print(x)