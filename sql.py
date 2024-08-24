import sqlite3

## Connect to sqlite
connection = sqlite3.connect("student.db")

## Create a cursor object to inser record, create table, retrieve records etc
cursor = connection.cursor()

## Create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
GRADE VARCHAR(25), MARKS INT);

"""

## Execute table
cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Lara','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sophia','Data Science','A',85)''')
cursor.execute('''Insert Into STUDENT values('Jun','Data Science','B',78)''')
cursor.execute('''Insert Into STUDENT values('James','DevOps','A',80)''')
cursor.execute('''Insert Into STUDENT values('Alex','DevOps','B',75)''')

## Display all the records
print("The inserted records are")

data = cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()