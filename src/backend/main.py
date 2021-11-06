import re
import time
from flask import Flask
from flask.helpers import flash, url_for
from flask.templating import render_template
from werkzeug.utils import redirect, secure_filename
from flask import request
import os

app = Flask("__name__")

@app.route('/time')
def get_return_time():
    return {'time':time.ctime(time.time())}

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024

ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/',methods = ['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No Image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        flash('Image succesfully uploaded and display below')
        return render_template('index.html',filename=filename)
    else:
        flash('Allowed image types are - png , jpg , jpeg')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static',filename='uploads/'+filename),code=301)


if __name__ == "__main__":
    app.run(debug=True)