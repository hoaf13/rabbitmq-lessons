import pika, sys, os

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("queue append {}".format(body.decode()))

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print('queue is waiting for messages. To exit press CTRL+C')
channel.start_consuming()
