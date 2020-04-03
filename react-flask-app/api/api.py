from flask import Flask
from flask import jsonify 
from flask import request
import Services as serv

import time
app = Flask(__name__)

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
def get_Top_Post_Month():
    backEndServ = serv.Back_End_Sevices()
    return backEndServ.get_top_post_month_service()

@app.route('/GetTopPost/Week', methods=['GET'])
def get_Top_Post_Week():
    backEndServ = serv.Back_End_Sevices()
    return backEndServ.get_top_post_week_service()

@app.route('/GetTopPost/Day', methods=['GET'])
def get_Top_Post_Day():
    backEndServ = serv.Back_End_Sevices()
    return backEndServ.get_top_post_day_service()

@app.route('/GetTopPost/Hour', methods=['GET'])
def get_Top_Post_hour():
    backEndServ = serv.Back_End_Sevices()
    return backEndServ.get_top_post_hour_service()

#########################################################
# US Map Page
#########################################################

@app.route('/GetTopPostsState/<string:state>', methods=['GET'])
def get_Top_Posts_State(state):
    backEndServ = serv.Back_End_Sevices()
    return backEndServ.get_top_posts_state_service(state)

#########################################################
# Search Page
#########################################################

@app.route('/Search/<string:user_input>', methods=['GET'])
def user_search_query_service(user_input):
    backEndServ = serv.Back_End_Sevices()
    return backEndServ.user_search_query_service(user_input)