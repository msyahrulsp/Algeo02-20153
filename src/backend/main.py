from flask import Flask
from flask.helpers import url_for
from werkzeug.utils import redirect, secure_filename
from flask import request,session
import os
import logging
from PIL import Image
import numpy as np
from svd import singular_value_decomposition
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

app = Flask("__name__")
CORS(app)

UPLOAD_FOLDER = '../../test/'
UPLOAD_FOLDER_BE = 'static/'

app.secret_key='secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024


@app.route('/upload', methods=['POST'])
def fileUpload():
    import time
    tstart = time.time()
    target=os.path.join(UPLOAD_FOLDER,'image')
    targetBE=os.path.join(UPLOAD_FOLDER_BE,'test_docs')
    target_compressed = os.path.join(UPLOAD_FOLDER,'hasil')
    target_compressedBE = os.path.join(UPLOAD_FOLDER_BE,'hasil')
    
    if (not os.path.isdir(target)):
        os.mkdir(target)
    if (not os.path.isdir(target_compressed)):
        os.mkdir(target_compressed)
    if (not os.path.isdir(targetBE)):
        os.mkdir(targetBE)
    if (not os.path.isdir(target_compressedBE)):
        os.mkdir(target_compressedBE)
    
    logger.info("welcome to upload")
    
    file = request.files['file']
    compression_rate = float(request.form['compression_rate'])
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    destinationBE="/".join([targetBE, filename])
    file.save(destinationBE)
    # destination = destination.replace("../../", "")
    session['uploadFilePath']=destinationBE

    image = Image.open(file) 
    hasil = singular_value_decomposition(image, p=compression_rate)
    hasil.save(f'{target_compressed}/compressed_'+filename)
    hasil.save(f'{target_compressedBE}/compressed_'+filename)
    tend = time.time()
    c = round(tend - tstart)
    texe = timeToString(c)
    session['texe'] = texe
    
    return redirect(url_for("time"))

def timeToString(t):
    ret = ""
    if (t / 3600 >= 1):
        ret += ("%d jam " % (t / 3600))
        t = t % 3600

    if (t / 60 >= 1):
        ret += ("%d menit " % (t / 60))
        t = t % 60

    ret += ("%d detik" % t)
    return ret

@app.route('/time')
def time():
    texe = session.get('texe', None)
    return {'time': texe}

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host="0.0.0.0",use_reloader=False)