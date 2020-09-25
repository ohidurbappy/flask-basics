from flask import Flask,render_template,request,make_response


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('cookies.html')


@app.route('/setcookie',methods=['POST','GET'])
def setcookie():
    if request.method=='POST':
        name=request.form.get('name')
        response=make_response(render_template('readcookies.html'))
        response.set_cookie('username',name)

        return response
    

@app.route('/getcookie',methods=['POST','GET'])
def getcookie():
    nm=request.cookies.get('username')
    return f"<html><body><h1>Welcome , {nm}</h1></body></html>"

if __name__ == "__main__":
    app.run(debug=True)