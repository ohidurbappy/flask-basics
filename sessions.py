from flask import Flask,session,url_for,redirect,request,render_template,abort,flash


app=Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        username=session.get('username')

        return f'''You are logged in as {username}<br> 
                    <a href="{url_for('logout')}">Click here to logout</a>
                    '''
    else:
        return f'You are not logged in <br><a href="{ url_for("login") }">Click here to login</a>'

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username',None)
    
    return redirect(url_for('index'))

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=='POST':
        username=request.form.get('username')

        session['username']=username

        return redirect(url_for('index'))

    else:
        return f'''
            <html>
                <body>
                <h1>Enter your username</h1>
                    <form method="POST" action="{ url_for('login')  }">
                        Name: <input type="text" name="username"/>
                        <input type="submit" value="submit"/>
                    </form>
                </body>
            </html>
        '''

@app.route('/show')
def show():
    if not 'username' in session:
        flash("Not authorized :(")
        abort(401)



if __name__ == "__main__":
    app.secret_key = 'my_stupid_app_key'
    app.run(debug=True)

