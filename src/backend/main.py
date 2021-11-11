import time
from flask import Flask
from flask.helpers import url_for
from werkzeug.utils import redirect, secure_filename
from flask import request,session
import os
import logging
from PIL import Image
import numpy as np
from svd import singular_value_decomposition


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

app = Flask("__name__")

@app.route('/time')
def get_return_time():
    return {'time':time.ctime(time.time())}

UPLOAD_FOLDER = 'static/'

app.secret_key='secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024


@app.route('/upload', methods=['POST'])
def fileUpload():
    target=os.path.join(UPLOAD_FOLDER,'test_docs')
    target_compressed = os.path.join(UPLOAD_FOLDER,'hasil')
    
    if (not os.path.isdir(target)):
        os.mkdir(target)
    if (not os.path.isdir(target_compressed)):
        os.mkdir(target_compressed)
    
    logger.info("welcome to upload")
    
    file = request.files['file']
    compression_rate = int(request.form['compression_rate'])
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination

    image = Image.open(file)
    array_image = np.asarray(image).astype(np.float64) 
    hasil = singular_value_decomposition(array_image,k=compression_rate)
    hasil.save(f'{target_compressed}/compressed_'+filename)
    
    
    response="Whatever you wish too return"
    return response



@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host="0.0.0.0",use_reloader=False)


