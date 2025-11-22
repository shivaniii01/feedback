import sqlite3
connection=sqlite3.connect('feedback.db')
cursor=connection.cursor()
cmd="""
    CREATE TABLE IF NOT EXISTS feedback(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Fullname text NOT NULL,
    usn varchar(10) NOT NULL,
    contact varchar(10) NOT NULL,
    email text NOT NULL,
    message text NOT NULL
)
"""
cursor.execute(cmd)
connection.commit()
cmd="INSERT INTO feedback (Fullname, usn, contact, email, message) VALUES (?, ?, ?, ?,?)"
#cursor.execute(cmd, ('Shivani', '4mw23ad042','7021026606','shivani.23ad042@sode-edu.in','Great course!'))
connection.commit()
f=cursor.execute("SELECT * FROM feedback").fetchall()
print(f)
connection.close()