import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port=23306,
  user="root",
  password="p455w0rd",
  database="garden"
)

#print(mydb)

db = mydb.cursor()
