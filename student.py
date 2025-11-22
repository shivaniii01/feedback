import sqlite3
connection=sqlite3.connect('student.db')
cursor=connection.cursor()
cmd="""
    CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch text NOT NULL,
    usn varchar(10) NOT NULL,
    cgpa double NOT NULL,
    sem integer NOT NULL
)
"""
cursor.execute(cmd)
connection.commit()
cmd="INSERT INTO student (branch, usn, cgpa, sem) VALUES (?, ?, ?, ?)"
cursor.execute(cmd, ('AIDS', '4mw23ad042',8.0,5))
connection.commit()
f=cursor.execute("SELECT * FROM student").fetchall()
print(f)
r=cursor.execute("SELECT * FROM student WHERE branch=? & usn=?",('AIDS','4mw23ad027')).fetchall()
print(r)
connection.close()