#Create a connection for DB and print the version using a python program
import sqlite3
try:
   sqlite_Connection = sqlite3.connect('temp.db')
   conn = sqlite_Connection.cursor()
   print("\nDatabase created and connected to SQLite.")
   sqlite_select_Query = "select sqlite_version();"
   conn.execute(sqlite_select_Query)
   record = conn.fetchall()
   print("SQLite Database Version is: ", record)
   conn.close()
except sqlite3.Error as error:
   print("Error while connecting to sqlite.", error)
finally:
   if (sqlite_Connection):
       sqlite_Connection.close()
       print("The SQLite connection is closed.")


#Create a multiple tables & insert data in table
import  sqlite3
conn  =  sqlite3 . connect ( 'mydatabase.db' )
cursor  =  conn.cursor ()
cursor.execute("CREATE TABLE Salesman12(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
s_id = input('\n\nSalesman ID:')
s_name = input('Name:')
s_city = input('City:')
s_commision = input('Commission:')
cursor.execute("""INSERT INTO salesman(salesman_id, name, city, commission)VALUES (?,?,?,?)""", (s_id, s_name, s_city, s_commision))
conn.commit ()
print ( 'Data entered successfully.' )
conn . close ()
if (conn):
  conn.close()
  print("The SQLite connection is closed.")