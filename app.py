from flask import Flask,render_template,request
from twilio.rest import Client
import sqlite3
app=Flask(__name__)
app.secret_key='jshadvuwv1234213'
sid="AC91140158090b3fa0081f9bdfcb3000fd"
token="5150cec51646fb71d7811a0e9aaddd9f"
mynum="+16812026274"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/after10th')
def after10th():
    return render_template('after10th.html')


@app.route('/after12th')
def after12th():
    return render_template('after12th.html')


@app.route('/afterUG')
def afterUG():
    return render_template('afterUG.html')


@app.route('/exams')
def exams():
    return render_template('exams.html')


@app.route('/more')
def more():
    return render_template('more.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')

 
def create_connection():
    conn=sqlite3.connect('whatnext.db')
    return conn

def create_table():
    conn=create_connection()
    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS USER(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            usrnm TEXT NOT NULL,
                            email TEXT NOT NULL,
                            phno  TEXT NOT NULL,
                            qualification TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        user=request.form['usrnm']
        email=request.form['email']
        phone=request.form['phno']
        qualification=request.form['qualification']
        print(user)
        print(email)
        print(phone)
        print(qualification)
        conn=create_connection()
        conn.cursor().execute('''INSERT INTO  USER(usrnm,email,phno,qualification) VALUES(?,?,?,?)''',(user,email,phone,qualification))
        conn.commit()
        conn.close()
        client=Client(sid,token)
        message=client.messages.create(
        body="Registration Successfull.Choose the right course with 'WHAT NEXT'",
        from_=mynum,
        to="+91" +phone)

        print(message)

        return render_template('index.html')
    return render_template('register.html')
    
    
if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=8080)
