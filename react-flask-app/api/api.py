from flask import Flask
from flask import jsonify 
from pymongo import MongoClient

import time
app = Flask(__name__)
mongoDBclient = MongoClient('localhost', 27017)

mongoDB = mongoDBclient['memeTweets']
coTwt = mongoDB['CO']

myquery = { "tweetID": "1203753948173094913"}
@app.route('/time')
def get_current_time():
    data = {'time':time.time()}
    mydoc = coTwt.find(myquery)
    for x in mydoc:
        print(x)
    return jsonify(data)
