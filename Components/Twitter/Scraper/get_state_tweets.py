import twitterScraper as ts
import us_states_info as stateInfo
from pymongo import MongoClient
import datetime as dt
import os
import time

'''
This script expects that mongoDB is installed and running...

Gets tweets for each US state.

Start MongoDB:
$sudo systemctl start mongod

Check MongoDB Status: 
$sudo systemctl status mongod

Start at system reboot:
$sudo systemctl enable mongod

Stop MongoDB:
$sudo systemctl stop mongod

Default port: 27017
'''
start_time = time.time()
track_list = ["funny", "meme", "hilarious", "haha", "LOL"]

def main():
    #Start mongoDB service on host
    os.system("sudo systemctl start mongod")

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

        tweets = ts.scrape_twitter(track_list=track_list, limit=10, poolsize=5, begindate=dt.date(2015, 6, 12), enddate=dt.date.today(),
                                   loc_near=stateDict.get(key).get('city'), radius=stateDict.get(key).get('radius'))

        ts.sort_tweets_by_popularity(tweets)

        #Insert into DB
        for tweet in tweets:
            tweetEntry = {
                "tweetID": tweet.tweet_id,
                "date": tweet.timestamp,
                "text": tweet.text,
                "likes": tweet.likes,
                "rt": tweet.retweets
            }
            mongoCollection.insert_one(tweetEntry)
        
        print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
