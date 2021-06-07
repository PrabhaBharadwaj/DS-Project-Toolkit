import numpy as np
from flask import Flask
import pickle

#app = Flask(__name__)
app = Flask(__name__)


#@app.route('/hello/<name>')
@app.route('/hello')

def hello(name):
    #return "Hello %s!" % name
    return "Hello edu"


if __name__ == "__main__":
    app.run()