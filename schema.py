import mysql.connector

connection = mysql.connector.connect(host="localhost",
                            user="root",
                            password="aslan")

cur_object = connection.cursor()

cur_object.execute("CREATE DATABASE cognitions")
