import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="car_detection")

mycursor = mydb.cursor(buffered=True)
