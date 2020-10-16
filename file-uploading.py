from flask import render_template, Flask, request

from werkzeug.utils import secure_filename

app=Flask(__name__)


@app.route('/upload')
def upload():
    return render_template('fileuploader.html')

@app.route('/uploader',methods=['GET','POST'])
def uploader():
    if request.method=='POST':
        f=request.files['file']
        f.save(secure_filename(f.filename))
        return "File saved successfully"


if __name__ == "__main__":
    app.run()
