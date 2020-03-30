from twitterscraper import query_tweets

def scrape_twitter(track_list,limit,begindate,enddate,loc_near,radius):
    """ 
        Parameters
        ----------
        track_list : list of strings

        limit : integer

        begindate : date object

        enddate : date object
            
        loc_near : string
            The location from which the tweets should come. This has to be a city name
            followed by the abbreviate state of the of the form "The City,ST"
            ex) "Grand Junction,CO" or "New York,NY" or "Colorado Springs,CO"

        radius : int
            The radius (in miles) around the location from which the tweets should come
        
        Returns
        -------
        tweets : twitterscraper.tweet.Tweet objects
    """
    tweets = []
    string_query = make_string_query(track_list=track_list, loc_near=loc_near, loc_within_mi=radius)

    for tweet in query_tweets(query=string_query, limit=limit, begindate=begindate, enddate=enddate, lang="en"):
        tweets.append(tweet)
    print("Number of Tweets fround for " + loc_near + ": ", len(tweets))
    return tweets

def make_string_query(track_list, loc_near, loc_within_mi):
    """
    Turns a combination of name, location, and a radius around that location into a string query
    to be given to the twitterscraper.query_tweets() method
    Queries can be tested here: https://twitter.com/search-home
    Result for: biden near:"Atlanta,GA" within:300mi lang:en
    https://twitter.com/search?q=%20biden%20near%3A%22Atlanta%2CGA%22%20within%3A300mi%20lang%3Aen&src=typed_query
        
        Parameters
        ----------
        name : string
            The name of the query's subject
        loc_near : string
            The location from which the tweets should come. This has to be a city name
            followed by the abbreviate state of the of the form "The City,ST"
            ex) "Grand Junction,CO" or "New York,NY" or "Colorado Springs,CO"
        loc_within_mi : int
            The radius (in miles) around the location from which the tweets should come
        
        Returns
        -------
        query : string
            A concatenated string query containing the given parameters
            ex) trump near:"Colorado Springs,CO" within:50mi
            ex) biden near:"Atlanta,GA" within:300mi
    """
    #Costruct track_list string with " OR " between terms
    track_str = ""
    for i in range(len(track_list)):
        track_str += track_list[i]
        if i != len(track_list)-1:
            track_str += " OR "

    #Cities consisting of two words need to be enclosed in quotes
    return track_str + " near:" + "\"" + loc_near + "\"" + " within:" + str(loc_within_mi) + "mi"

def sort_tweets_by_popularity(tweets):
    """
        Sorts lists of tweets in-place where (likes + retweets) consist of key
            
            Parameters
            ----------
            tweets : list of tweets
            
            Returns
            -------
            none :
                Sorts tweets in place
        """
    tweets.sort(key=lambda x: (x.likes+x.retweets), reverse=True)
