import mysql.connector

connection = mysql.connector.connect(host="localhost",
                            user="root",
                            password="aslan",
                            database="cognition")

cur_object = connection.cursor()

# i'm trying to see if i should auto-increment the times this button was pushed here
# or in my actions section. ...i think it will be better in actions but i will try it here
# first
def create_table(name):
    cur_object.execute("DROP TABLE IF EXISTS{}.format(name))"
    table = """CREATE TABLE {}(
    iput_id INT AUTO_INCREMENT PRIMARY KEY,
    times_pushed INT AUTO_INCREMENT
    )
