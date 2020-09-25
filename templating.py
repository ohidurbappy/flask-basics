from flask import Flask,render_template


app=Flask(__name__)


@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/hello/<name>/')
def welcome(name):
    return render_template('welcome.html',name=name)


@app.route('/show/<int:score>')
def show_score(score):
    return render_template('score.html',marks=score)

@app.route('/show/result')
def show_result():
    marks={
        'math':90,
        'physics':88,
        'chemistry':74
    }

    return render_template('show_result.html',marks=marks)

@app.route('/example/static_files')
def show_static_files_example():
    return render_template('static_files_demo.html')


if __name__ == "__main__":
    app.debug=True
    app.run()