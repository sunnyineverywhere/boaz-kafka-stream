import csv
import json
import os
import time

from kafka import KafkaConsumer


class Consumer:
    def __init__(self, brokers, topicName):
        self.consumer = KafkaConsumer(
            topicName,
            group_id="boaz-consumer",
            bootstrap_servers=brokers,
            api_version=(0, 11, 5),
        )

    def print(self):
        print("Start state check")
        new_data = []  # 새로운 데이터 저장
        for message in self.consumer:
            print(message.value)


if __name__ == '__main__':
    brokers = ["localhost:9092"]
    topicName = "boaz"
    consumer = Consumer(brokers, topicName)
    consumer.print()