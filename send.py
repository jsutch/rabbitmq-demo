#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

message='Hello World, I am Home!'
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(f" [x] Sent {message}")
connection.close()
