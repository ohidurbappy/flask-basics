from flask import Flask,flash,render_template,request,url_for

app=Flask(__name__)



@app.route('/')
def index():
    return render_template('flashing.html')


@app.route('/login',methods=['POST','GET'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username']!='admin' or request.form['password']!='admin':
            error="Invalid username or password"
        
        else:
            flash("You are logged in successfully")
            return render_template('flashing.html')
    return render_template('flashing.login.html')

    

if __name__ == "__main__":
    app.secret_key='app_122323'
    app.run(debug=True)
