import mysql.connector

connection = mysql.connector.connect(host="localhost",
                            user="root",
                            password="aslan",
                            database="cognition")

cur_object = connection.cursor()

# i'm trying to see if i should auto-increment the times this button was pushed here
# or in my actions section. ...i think it will be better in actions but i will try it here
# first
def createNegative():
    table = ("CREATE TABLE negative;
            (primary_key INT(11) AUTO_INCREMENT;
            times_pressed INT(11) AUTO_INCREMENT")
