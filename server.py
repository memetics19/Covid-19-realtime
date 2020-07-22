# Import libraries
import flask
from flask import request, jsonify
import flask_pymongo
# import Pymongo
#print(dir(flask_pymongo))
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

URI = "mongodb://admin:admin@cvt-shard-00-00.xqekr.mongodb.net:27017,cvt-shard-00-01.xqekr.mongodb.net:27017,cvt-shard-00-02.xqekr.mongodb.net:27017/covid19?ssl=true&replicaSet=atlas-vemg8m-shard-0&authSource=admin&retryWrites=true&w=majority"


app = flask.Flask(__name__)
app.config["MONGO_URI"] = URI

mongo = flask_pymongo.PyMongo(app)
##print(mongo.text_type())
print(dir(mongo.init_app(app)))
db = mongo['Covid19']
collection = db['May2020']
"""  class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize(self):
        client = pymongo.MongoClient(self.URI)
        self.DATABASE = client['cvm']

        ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
        '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
        '__module__', '__ne__', '__new__', '__reduce__',
         '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
          'cx', 'db', 'init_app', 'save_file', 'send_file']

    @staticmethod
    def find_sort(self, collection, query, direction, limit):
        return self.DATABASE[collection].find({}).sort(query, direction).limit(limit)"""
@app.route('/', methods=['GET'])

def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for COVID-19 real-time data fetch.</p>'''

@app.route('/home', methods=['GET'])
def api_all():
    total_cases = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
    collection.insert_one(total_cases)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
