from flask import Flask
from flask import jsonify 
from flask import request
import Services as serv

import time
app = Flask(__name__)

#########################################################
# Testing routes
#########################################################

@app.route('/time')
def get_current_time():
    data = {'time':time.time()}
    return jsonify(data)

#########################################################
# Main Page
#########################################################

@app.route('/GetSentimentHomePage', methods=['GET'])
def get_sentiment_home_page():
    backEndServ = serv.Back_End_Sevices()
    return backEndServ.get_sentiment_home_page_service()

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

#########################################################
# Cron Jobs
#########################################################
@app.route('/tasks/updateUSTweets', methods=['GET'])
def update_US_Tweets():
    backEndServ = serv.Back_End_Sevices()
    return backEndServ.update_US_Tweets_service()

@app.route('/GetTopCovidPosts', methods=['GET'])
def get_Top_Covid_Post():
    backEndServ = serv.Back_End_Sevices()
    return backEndServ.get_top_covid_posts()