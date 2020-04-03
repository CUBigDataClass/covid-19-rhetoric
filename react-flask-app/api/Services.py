from pymongo import MongoClient
from flask import jsonify 
import json
import sys

# Custom class with US state information
sys.path.append('../../Components/Twitter/Scraper/')
import us_states_info as stateInfo
# Twitter API wrapper (using tweepy)
sys.path.append('../../Components/Twitter/Twitter-api/')
import pythonTwitterAPI as twitterapi

class Back_End_Sevices():

    def __init__(self,port=27017,host="127.0.0.1"):
        self.port = int(port)
        self.mongoDBClient = MongoClient(host, port)

        #MongoDB databases
        self.funnyAccountTweets_db = self.mongoDBClient['FunnyAccountTweets']
        self.state_Tweets_db = self.mongoDBClient['State_Tweets']

    def get_top_post_hour_service(self):
        return jsonify({
            "function:" : "get_top_post_hour",
        }), 200 #OK

    def get_top_post_day_service(self):
        return jsonify({
            "function:" : "get_top_post_day",
        }), 200 #OK

    def get_top_post_week_service(self):
        return jsonify({
            "function:" : "get_top_post_week",
        }), 200 #OK

    def get_top_post_month_service(self):
        return jsonify({
            "function:" : "get_top_post_month",
        }), 200 #OK

    #/GetTopPostsState
    def get_top_posts_state_service(self,state):
        stateAbbr = stateInfo.US_States_Info().get_state_abbreviations()
        if (state in stateAbbr):
            collection = self.state_Tweets_db
            documents = collection[state]

            tweetIDs = []
            for document in documents.find({}):
                tweetIDs.append(document["tweetID"])
            #tweetIDs = [tweetIDs for document["tweetIDs"] in documents.find({})]

            return jsonify(tweetIDs), 200
        else:
            return "NOT A VALID STATE\n", 404 #NOT FOUND

        def get_top_post_month_service():
            pass

    #/Search/<string:user_input>
    def user_search_query_service(self, user_input):
        if len(user_input) > 500:
            return "BAD REQUEST\n", 400 
        else:
            twitterClient = twitterapi.TwitterClient()
            tweets = twitterClient.search_for_tweet(user_input,100)

            tweetIds = self.makeListOfTweetIds(tweets)
            if(len(tweetIds) == 0):
                return "NOT FOUND\n", 404
            else:
               return jsonify(tweetIds), 200

    def makeListOfTweetIds(self, tweets):
        tweetIds = []
        for tweet in tweets:
            tweetIds.append(str(tweet.id))
        return tweetIds