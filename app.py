from flask import Flask, render_template,request 
import sqlite3   
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/submit',methods=['POST'])
def submit():
    FULLNAME=request.form.get('fullname')
    USN=request.form.get('usn')
    CONTACT=request.form.get('contact')
    EMAIL=request.form.get('email')
    MESSAGE=request.form.get('message')
    connection=sqlite3.connect('feedback.db')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO feedback(fullname,usn,contact,email,message) VALUES (?,?,?,?,?)",(FULLNAME,USN,CONTACT,EMAIL,MESSAGE))
    connection.commit()
    feedback=cursor.execute("SELECT fullname,message from feedback").fetchall()
    connection.close()
    return render_template('success.html',feedback=feedback,name=FULLNAME)
if __name__ == '__main__':
    app.run(debug=True)