import sqlite3

connection  = sqlite3.connect("student.db")

cursor = connection.cursor()

table = """
create table STUDENT(NAME Varchar(25),CLASS Varchar(25),SECTION varchar(25),MARKS INT);

"""

cursor.execute(table)

cursor.execute('''Insert Into STUDENT values('Soumalla','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Saumyadeep','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Antara','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()