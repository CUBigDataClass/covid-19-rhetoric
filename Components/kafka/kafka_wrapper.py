from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka import KafkaConsumer
import sys
import time
import threading

# Custom Textblob
sys.path.append('../sentiment_analyzer/')
import sentiment_TextBlob as tb

class Kafka_Wrapper():

    def __init__(self, host="127.0.0.1", port=9092, topic="test5"):
        self.host = host
        self.port = port
        self.topic = topic

    def produce_message(self, message):

        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

        # Asynchronous by default
        future = producer.send(self.topic, message.encode('utf-8'))

        # block until all async messages are sent
        producer.flush()

    def wait_and_consume_messages(self):
        # To consume latest messages and auto-commit offsets
        consumer = KafkaConsumer(self.topic,
                                group_id='my-group',
                                bootstrap_servers=['localhost:9092'])
        consumer2 = KafkaConsumer(self.topic,
                                group_id='my-group2',
                                bootstrap_servers=['localhost:9092'])
        for message in consumer:
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`
            print("********************Consumer 1***************************\n")
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                message.offset, message.key,
                                                message.value))

            print("Sentiment polarity is:",tb.Text_Sentiment().get_sentiment_polarity(str(message.value)))
            print("*********************************************************\n")

        for message in consumer2:
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`
            print("********************Consumer 2***************************\n")
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                message.offset, message.key,
                                                message.value))

            print("Sentiment polarity is:",tb.Text_Sentiment().get_sentiment_polarity(str(message.value)))
            print("*********************************************************\n")
