pip install mysql-connector-python
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), city VARCHAR(25),")
mycursor = mydb.cursor()
sql = "INSERT INTO Employee (id,name, city) VALUES (%s,%s,%s)"
val = [
  ('12','sneha', 'bangalore'),
  ('14','suntheya', 'Apple st','chennai'),
  ('10','shahini', 'mysore'),
  ('13','Mickey', 'mumbai'),
  ('15','Santhosh', 'chennai')
]
mycursor.executemany(sql, val)
mydb.commit()
mycursor = mydb.cursor()
mycursor.execute("SELECT name FROM Employee")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)