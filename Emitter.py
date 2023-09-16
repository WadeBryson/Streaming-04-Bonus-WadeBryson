"""
    This program sends a message to a queue on the RabbitMQ server.
    Make tasks harder/longer-running by adding dots at the end of the message.

    Author: Wade Bryson
    Date: September 16, 2023

"""

import pika
import sys
import webbrowser
import csv
import time


# Configure logging
from util_logger import setup_logger
logger, logname = setup_logger(__file__)

Show_Offer = True

def offer_rabbitmq_admin_site():
    """Offer to open the RabbitMQ Admin website"""
    ans = input("Would you like to monitor RabbitMQ queues? y or n ")
    print()
    if ans.lower() == "y":
        webbrowser.open_new("http://localhost:15672/#/queues")
        print()

def send_message(host: str, queue1_name: str, queue2_name: str, input_file: str):
    """
    Creates and sends a message to the queue each execution.
    This process runs and finishes.

    Parameters:
        host (str): the host name or IP address of the RabbitMQ server
        queue1_name (str): the name of the first queue
        queue2_name (str): the name of the second queue
        input_file (str): the CSV file to be read
    """

    try:
        # create a blocking connection to the RabbitMQ server
        conn = pika.BlockingConnection(pika.ConnectionParameters(host))
        # use the connection to create a communication channel
        ch = conn.channel()
        # use the channel to declare a durable queue
        # a durable queue will survive a RabbitMQ server restart
        # and help ensure messages are processed in order
        # messages will not be deleted until the consumer acknowledges
        ch.queue_declare(queue=queue1_name, durable=True)
        ch.queue_declare(queue=queue2_name, durable=True)

        # read CSV
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            # skip header row
            header = next(reader)
            for row in reader:
                # separate row into variables by column
                Square Side Length  = row
                # define first and second messages
                first_message = str(country)
                second_message = stars
                # use the channel to publish first message to first queue
                # every message passes through an exchange
                ch.basic_publish(exchange="", routing_key=first_queue_name, body=first_message)
                # print a message to the console for the user
                logger.info(f" [x] Sent {first_message} to {first_queue_name}")
                # publish second message to second queue
                ch.basic_publish(exchange="", routing_key=second_queue_name, body=second_message)
                # print a message to the console for the user
                logger.info(f"[x] Sent {second_message} to {second_queue_name}")
                # wait 3 seconds before sending the next message to the queue
                time.sleep(3)