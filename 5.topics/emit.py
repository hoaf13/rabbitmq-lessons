import pika 
import sys 
import time 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

product = 100
while True:
    channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=str(product))
    print('[x] send product: {} to routing_key: {}'.format(product, routing_key))
    product += 1
    time.sleep(1)


connection.close()
