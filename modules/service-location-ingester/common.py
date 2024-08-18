
import json
import logging
import os

from kafka import KafkaProducer
from typing import Dict

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("location-ingester-service")

# Create the kafka producer
producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])


def publish_location(location_data):
    print(f"Sent data to Kafka: {location_data}")

    encoded_data = json.dumps(location_data).encode('utf-8')
    print(f"Sent data to Kafka: {encoded_data}")
    producer.send(TOPIC_NAME, encoded_data)
    producer.flush()

    logger.info(f"Published {location_data} to kafka successfully.")
