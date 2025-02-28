from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable, KafkaError
import json
import time




connection_not_successful = True

while connection_not_successful:
    try:
        consumer = KafkaConsumer(
            'covid-data',  # Topic to subscribe to
            bootstrap_servers='kafka:29092',  # Connect to the Kafka broker
            auto_offset_reset='earliest',  # Start reading at the beginning of the topic
            enable_auto_commit=True,
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Deserialize JSON data
        )

        print("Connection to Kafka broker successful!")

        connection_not_successful = False
        print("Starting Kafka consumer...")
        for message in consumer:
            print(f"Received: {message.value}")
    except (NoBrokersAvailable, KafkaError) as e: 
        print(e)
        time.sleep(2)