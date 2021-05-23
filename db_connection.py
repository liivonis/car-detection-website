import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="admin", passwd="admin", database="car_detection")

mycursor = mydb.cursor()

#  Varchar string insert in case needed
#  mycursor.execute("INSERT INTO car_count (CarCount) VALUES ('%s')" % (cars));
