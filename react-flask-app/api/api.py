from flask import Flask
from flask import jsonify 
from flask import request
from pymongo import MongoClient
import sys

# Custom class with US state information
sys.path.append('../../Components/Twitter/Scraper/')
import us_states_info as stateInfo

import time
app = Flask(__name__)
mongoDBclient = MongoClient('localhost', 27017)

mongoDB = mongoDBclient['memeTweets']
coTwt = mongoDB['CO']

#########################################################
# Testing routes
#########################################################

myquery = { "tweetID": "1203753948173094913"}
@app.route('/time')
def get_current_time():
    data = {'time':time.time()}
    mydoc = coTwt.find(myquery)
    for x in mydoc:
        print(x)
    return jsonify(data)

#########################################################
# Main Page
#########################################################

@app.route('/GetTopPost/Month', methods=['GET'])
def get_top_post_month():
    return jsonify({
        "function:" : "get_top_post_month",
    }), 200 #OK

@app.route('/GetTopPost/Week', methods=['GET'])
def get_top_post_week():
    return jsonify({
        "function:" : "get_top_post_week",
    }), 200 #OK

@app.route('/GetTopPost/Day', methods=['GET'])
def get_top_post_day():
    return jsonify({
        "function:" : "get_top_post_day",
    }), 200 #OK

@app.route('/GetTopPost/Hour', methods=['GET'])
def get_top_post_hour():
    return jsonify({
        "function:" : "get_top_post_hour",
    }), 200 #OK
    
#########################################################
# US Map Page
#########################################################

@app.route('/GetTopPostsState/<string:state>', methods=['GET'])
def get_top_posts_state(state):
    stateAbbr = stateInfo.US_States_Info().get_state_abbreviations()
    if (state in stateAbbr):
        return jsonify({
            "function:" : "get_top_posts_state",
            "input:" : state
        }), 200 #OK
    else:
        return "NOT A VALID STATE\n", 404 #NOT FOUND

#########################################################
# Search Page
#########################################################

@app.route('/Search/<string:user_input>', methods=['GET'])
def user_search_query(user_input):
    return jsonify({
        "function:" : "user_search_query",
        "input" : user_input
    }), 200 #OK
   