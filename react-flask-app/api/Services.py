from pymongo import MongoClient
from flask import jsonify 
import json
import sys
import redis


# Custom class with US state information
sys.path.append('../../Components/Twitter/Scraper/')
import us_states_info as stateInfo
# Twitter API wrapper (using tweepy)
sys.path.append('../../Components/Twitter/Twitter-api/')
import pythonTwitterAPI as twitterapi

sys.path.append('../../Components/kafka/')
import twitter_producer

sys.path.append('../../Components/sentiment_analyzer/')
import sentiment_TextBlob as sT

class Back_End_Sevices():

    def __init__(self):
        self.host = "mongodb+srv://app:bigdata@cluster0-vejky.gcp.mongodb.net/test?retryWrites=true&w=majority"
        self.mongoDBClient = MongoClient(self.host)

        #MongoDB databases
        self.funnyAccountTweets_db = self.mongoDBClient['FunnyAccountTweets']
        self.state_Tweets_db = self.mongoDBClient['State_Tweets']

    #########################################################
    # Main Page
    #########################################################

    #/GetTopCovidPosts
    def get_top_covid_posts(self):
        #Start Twitter Streamer 
        twitter_producer.start_producer()
        
        return jsonify({
            "function:" : "get_top_covid_posts",
        }), 200 #OK

    #/GetSentimentHomePage
    def get_sentiment_home_page_service(self):
        # tweet_dict = {}
        tweet_list = list()
        redisObject = redis.Redis(host = "34.71.51.51", db = 1)
        for key in redisObject.scan_iter("*"):
            sentiment = redisObject.get(key)
            # print(key,sentiment)
            # tweet_dict[str(key)] = sentiment
            tweet_dict = {
                'key' : key.decode("utf-8"),
                'sentiment' : sentiment.decode("utf-8")
            }
            tweet_list.append(tweet_dict)

        return jsonify(tweet_list), 200 #OK

    #########################################################
    # US Map
    #########################################################

    #/GetTopPostsState
    def get_top_posts_state_service(self,state):
        stateAbbr = stateInfo.US_States_Info().get_state_abbreviations()
        if (state in stateAbbr):
            collection = self.state_Tweets_db
            documents = collection[state]

            tweets = []
            for document in documents.find({}):
                tweetDict = {
                    "key" : document["key"],
                    "sentiment" : document["sentiment"]
                }

                tweets.append(tweetDict)
            #tweetIDs = [tweetIDs for document["tweetIDs"] in documents.find({})]

            return jsonify(tweets), 200
        else:
            return "NOT A VALID STATE\n", 404 #NOT FOUND

        def get_top_post_month_service():
            pass

    #########################################################
    # Search
    #########################################################

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

    #/Search/<string:user_input>
    # def user_search_query_service(self, user_input):

    #     new_input = user_input + " covid-19 " + " CDC "
    #     if len(new_input) > 500:
    #         return "BAD REQUEST\n", 400 
    #     else:
    #         twitterClient = twitterapi.TwitterClient()
    #         tweets = twitterClient.search_for_tweet(new_input,100)
            
    #         tweetDicts = self.makeListOfTweets(tweets)
    #         if(len(tweetDicts) == 0):
    #             return "NOT FOUND\n", 404
    #         else:
    #            return jsonify(tweetDicts), 200

    # def makeListOfTweets(self, tweets):
    #     blob = sT.Text_Sentiment()
    #     tweetsDict = []
    #     for tweet in tweets:
    #         polarity = blob.get_sentiment_polarity(tweet.text)
    #         tweetEntry = {
    #             "key": tweet.id,
    #             "sentiment": polarity
    #         }
    #         tweetsDict.append(tweetEntry)
    #     return tweetsDict