import twitterScraper as ts
import us_states_info as stateInfo
from pymongo import MongoClient
import datetime as dt

'''
This script expects that mongoDB is installed and running...

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
def main():
    #Making a connection with MogoClient
    mongoDBclient = MongoClient('localhost', 27017)

    #Getting the DB (creates the DB if DNE)
    mongoDB = mongoDBclient['memeTweets']

    #Getting the collection (creates collection if DNE)
    coTwt = mongoDB['CO']

    week_ago = dt.date.today() - dt.timedelta(days=7)

    tweets = ts.scrape_twitter(query="meme", limit=10000, begindate=dt.date(2015, 6, 12), enddate=week_ago, lang='en', loc_near="Denver,CO", loc_within_mi=300)
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
        coTwt.insert_one(tweetEntry)

if __name__ == '__main__':
    main()
