'''
This is not constrained by the limitations of Twitter API... 
'''

from twitterscraper import query_tweets

#Returns list of found tweets as twitterscraper.tweet.Tweet objects 
def query_for_tweets(query,limit,begindate,enddate,lang,loc_near,loc_within_mi):
    tweets = []
    strQuery = query + " near:" + loc_near + " within:" + str(loc_within_mi) + "mi"

    for tweet in query_tweets(query=strQuery, limit=limit, begindate=begindate, enddate=enddate, lang=lang):
        tweets.append(tweet)
    print("Number of found Tweets:", len(tweets))
    return tweets

def sort_tweets_by_popularity(tweets):
    tweets.sort(key=lambda x: (x.likes+x.retweets), reverse=True)

