import json
import sys
from kafka import KafkaConsumer
import redis
import sentiment_TextBlob as sT

def start_consumer():
    covid_tweets = list()
    max_tweets = 80
    tweet_counter = 0

    #Connect to Kafka (VM) as a Consumer
    consumer = KafkaConsumer('covid',
                            bootstrap_servers=['34.71.51.51:9092'])

    #Connect to Redis (VM)
    redisObject = redis.Redis(host = "34.71.51.51", db = 1)
    for msg in consumer:
        blob = sT.Text_Sentiment()
        tweet_dict = json.loads(msg.value)
        tweet_id = tweet_dict['id']
        tweet_text = tweet_dict['text']
        tweet_text = blob.clean_text(tweet_text)
        polarity = round(blob.get_sentiment_polarity(tweet_text),2)
        
        redisObject.set(tweet_id, polarity)
        tweet_counter += 1

        if(tweet_counter >= max_tweets):
            return
