import pymysql
'''db = pymysql.connect("localhost", "User","password","dnname")'''
db = pymysql.connect("localhost","root","redhat","TESTDB")
cursor = db.cursor()
cursor.execute("SELECT * from test;")
data = cursor.fetchall()
print(data)
db.close()
