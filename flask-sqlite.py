import sqlite3
from sqlite3.dbapi2 import Cursor
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('sqlite.index.html')


@app.route('/create_db')
def create_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE students (name TEXT, address TEXT, city TEXT, phone TEXT)')
    conn.close()
    return "Database created"

@app.route('/add_record')
def add_record():
    return render_template('sqlite.add.html')

@app.route('/show_record')
def show_record():
    try:
        con=sqlite3.connect('database.db')
        con.row_factory=sqlite3.Row

        cursor=con.cursor()

        cursor.execute('select * from students')

        rows=cursor.fetchall()

        return render_template('sqlite.show.html',rows=rows)

    except:
        return "something went wrong!"
        

@app.route('/new_entry',methods=['POST'])
def add_new_entry():
    try:
        con=sqlite3.connect('database.db')
        name=request.form['name']
        address=request.form['address']
        city=request.form['city']
        phone=request.form['phone']

        cursor=con.cursor()
        cursor.execute("INSERT INTO students (name,address,city,phone) values (?,?,?,?)",(name,address,city,phone))
        con.commit()
        msg="Record added successfully"
    except:
        con.rollback()
        msg="ERROR: Record could not be added"
    finally:
        con.close()
        return render_template('sqlite.result.html',msg=msg)



if __name__ == "__main__":
    app.run(debug=True)