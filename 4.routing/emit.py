# emit station
import pika
import sys
import time 


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
product = 100

while True:    
    channel.basic_publish(
        exchange='direct_logs', routing_key=severity, body=str(product))
    print(" [x] Sent %r:%r" % (severity, product))
    product += 1
    time.sleep(1)
connection.close()
