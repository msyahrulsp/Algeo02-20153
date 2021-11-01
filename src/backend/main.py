import time
from flask import Flask

app = Flask("__main__")

@app.route('/time')

def get_return_time():
    return {'time':time.ctime(time.time())}

app.run(debug=True)