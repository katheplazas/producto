from configparser import ConfigParser
from confluent_kafka import Producer, Consumer
import json

config_parser = ConfigParser(interpolation=None)
config_file = open('config.properties', 'r')
config_parser.read_file(config_file)
producer_config = dict(config_parser['kafka_client'])
consumer_config = dict(config_parser['kafka_client'])
consumer_config.update(config_parser['consumer'])
product_producer = Producer(producer_config)


def start_service():
    product_consumer = Consumer(consumer_config)
    product_consumer.subscribe(['store-name'])
    while True:
        msg = product_consumer.poll(0.1)
        if msg is None:
            #print("wait...")
            pass
        elif msg.error():
            pass
        else:
            name_product = json.loads(msg.value())
            print(name_product)
            product_producer.produce('store-product', value=json.dumps(name_product))
