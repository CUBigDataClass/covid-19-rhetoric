from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from kafka import KafkaProducer
#from kafka.client import SimpleClient
#from kafka.consumer import SimpleConsumer
#from kafka.producer import SimpleProducer
import os
import json

stream = None 

########################################################
# Class TwitterAuthenticator
########################################################
class TwitterAuthenticator():

  def __init__(self):
    #Get the dictionary of twitter OAth keys
    self.this_folder = os.path.dirname(os.path.abspath(__file__))
    self.keys_file = os.path.join(self.this_folder, "twitterKeys.json")

  def authenticate_twitter_app(self):
    try:
      twitterKeyFile = open(self.keys_file)
    except OSError:
      print("Error! Cannot open: ", self.keys_file)

    twitterKeys = json.load(twitterKeyFile)

    #API key & API secret key goes here...
    auth = OAuthHandler(twitterKeys.get("consumer_key"),
                        twitterKeys.get("consumer_secret"))

    #API Access token & secret token
    auth.set_access_token(twitterKeys.get("access_token_key"),
                          twitterKeys.get("access_token_secret"))
    return auth

########################################################
# Class TwitterClient
########################################################
class TwitterClient():
  def __init__(self, twitter_user=None):
    self.auth = TwitterAuthenticator().authenticate_twitter_app()
    self.twitter_client = API(self.auth)
    self.twitter_user = twitter_user

  def get_twitter_client_api(self):
    return self.twitter_client

##########################################################
# Class TwitterStreamer
##########################################################
class TwitterStreamer():

  def __init__(self,producer):
      self.twitter_authenticator = TwitterAuthenticator()
      self.producer = producer

  def stream_tweets(self, track_list):
  
      listener = StdOutListener(self.producer)
      auth = self.twitter_authenticator.authenticate_twitter_app()

      stream = Stream(auth, listener)

      # This line filters Twitter Streams to capture data by the keywords: 
      stream.filter(track=track_list)


class StdOutListener(StreamListener):

  def __init__(self,producer):
    self.producer = producer
    self.topic = "covid"
    self.limit = 100
    self.current_count = 0

  def on_data(self,data): 
    #Python dict
    tweetDict = json.loads(data)

    self.current_count += 1
    if(self.current_count >= self.limit):
      return False

    #Check if data is rate limit statement
    if 'id' not in tweetDict or 'text' not in tweetDict:
      # continue 
      return True

    tweet_data = {
      "id" : tweetDict['id'],
      "text" : tweetDict['text']
    }

    #self.producer.send_messages(self.topic, json.dumps(tweet_data).encode())
    self.producer.send(self.topic, json.dumps(tweet_data).encode())

    #  producer.send('topic', key='key', value=dict(idx=i))

    return True

  def on_error(self, status):
    # Check if we're being rate limited for making too many requests to Twitter
    if status == 420:
        return False
    print(status)

class Kafka_producer():
  def __init__(self):
    self.topic = "covid"

  def start_producer(self):
    #Track List for stream
    track_list = ['covid19','covid','pandemic','virus','cough']

    #Kafka setup
    #client = SimpleClient("34.71.51.51:9092")
    producer = KafkaProducer(bootstrap_servers=['34.71.51.51:9092'])
    

    #Stream starts here...
    streamer = TwitterStreamer(producer)
    streamer.stream_tweets(track_list)

if __name__ == '__main__':
  kafkaP = Kafka_producer()
  kafkaP.start_producer()
    





        
        



