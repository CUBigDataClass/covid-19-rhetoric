import twitterScraper as ts
import us_states_info as stateInfo
from pymongo import MongoClient
import datetime as dt
import os
import time

'''
This script expects that mongoDB is installed and running...
'''

track_list = ["funny", "meme", "hilarious", "haha", "LOL"]

def create_tweet_entry(tweet):
    tweetEntry = {
                "tweetID": tweet.tweet_id,
                "date": tweet.timestamp,
                "text": tweet.text,
                "likes": tweet.likes,
                "rt": tweet.retweets
                }
    return tweetEntry

def main():
    start_time = time.time()

    #Making a connection with MogoClient
    mongoDBclient = MongoClient('localhost', 27017)

    #Getting the DB (creates the DB if DNE)
    mongoDB = mongoDBclient['State_Tweets']

    #Gets state query info (cities and radii per state)
    stateDict = stateInfo.US_States_Info().get_US_cities_with_radius()

    for key in stateDict.keys():
        print("Scraping for:",key,"...")

        #Getting the collection (creates collection if DNE)
        mongoCollection = mongoDB[key]

        #For more tweets, change limit and poolsize
        tweets = ts.scrape_twitter(track_list=track_list, limit=5, poolsize=2, begindate=dt.date(2015, 6, 12), enddate=dt.date.today(),
                                   loc_near=stateDict.get(key).get('city'), radius=stateDict.get(key).get('radius'))

        ts.sort_tweets_by_popularity(tweets)

        mongoCollection.insert_many(map(create_tweet_entry,tweets))
        
        print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
