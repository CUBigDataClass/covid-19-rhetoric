from flask import Flask
from flask import jsonify 
from flask import request
import Services as serv
from flask_cors import CORS
import time

# [START gae_python37_app]

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
CORS(app)
cors = CORS(app,resources={
    r"/*":{
        "origins":"*"
    }
})

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
    #Start Consumer
    #Start Producer
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

@app.route('/StartProducer', methods=['GET'])
def start_producer():
    backEndServ = serv.Back_End_Sevices()
    return backEndServ.start_producer_service()

@app.route('/StartConsumer', methods=['GET'])
def start_consumer():
    backEndServ = serv.Back_End_Sevices()
    return backEndServ.start_consumer_service()


#########################################################
# Service Check
#########################################################
@app.route('/')
def hello():
    return 'API is running'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]