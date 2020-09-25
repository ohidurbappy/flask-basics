from flask import Flask,redirect,url_for,request

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello"

# adding route via decorator
@app.route('/hello')
def hello():
    return "Hello User"

# adding trailing slash in the rule supports both /path and /path/
@app.route('/path/')
def show_path():
    return "Both shows the same url"

# adding route using add_url_rule()
def hello_world():
    return "Hello World"
app.add_url_rule('/world','world',hello_world)


# variable rule
@app.route('/hello/<name>')
def hello_name(name):
    return "Hello %s"%name


# int type variable rule
@app.route('/blog/<int:blog_id>')
def show_blog(blog_id):
    return f"Showing blog {blog_id}"

# float type varialbe route
@app.route('/blog/<float:revision>')
def show_revision(revision):
    return f"Revision v{revision}"

# path types var support /
# http://127.0.0.1:5000/blog/12/2020/article -> The blog url is 12/2020/article
@app.route('/blog/<path:blog_url>')
def show_blog_url(blog_url):
    return f"The blog url is {blog_url}"



# url building
@app.route('/admin')
def hello_admin():
    return "Hello Admin"

@app.route('/guest/<name>')
def hello_guest(name):
    return 'Hello %s, Welcome!' % name

@app.route('/user/<name>')
def hello_user(name):
    if name=='bappy':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',name=name))



@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name

# http methods
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['name']
        return redirect(url_for('success',name=user))
    elif request.method=='GET':
        user=request.args.get('name')
        return redirect(url_for('success',name=user))



if __name__ == "__main__":
    app.debug=True
    app.run()