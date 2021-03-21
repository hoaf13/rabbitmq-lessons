import pika
import sys
import time 

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
#duralbe <- True: tasks do not lost when workder die

product = 100

while True:
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=str(product),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))

    print(" [x] Sent {}".format(product))
    product += 1
    time.sleep(0.1)

connection.close()