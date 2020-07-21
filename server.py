# Import libraries
import flask
from flask import request, jsonify
from flask_pymongo import Pymongo
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

URI = "mongodb://admin:admin@cvt-shard-00-00.xqekr.mongodb.net:27017,cvt-shard-00-01.xqekr.mongodb.net:27017,cvt-shard-00-02.xqekr.mongodb.net:27017/covid19?ssl=true&replicaSet=atlas-vemg8m-shard-0&authSource=admin&retryWrites=true&w=majority"
app = flask.Flask(__name__)
app.config["MONGO_URI"] = URI
mongo = PyMongo(app)

db = mongo['Covid19']
collection = db['May2020']
@app.route('/', methods=['GET'])

def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/home', methods=['GET'])
def api_all():
    total_cases = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
    collection.insert_one(total_cases)
    

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404