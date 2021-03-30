#queue 1
import pika
import sys 
import time 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
queue = channel.queue_declare(queue='directed_queue1', exclusive=True)

queue_name = queue.method.queue
severities = sys.argv[1:]

if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0]) # routing key
    sys.exit(1) 

for severity in severities:
    channel.queue_bind(queue=queue_name, exchange='direct_logs',routing_key=severity)

print("[x] waiting for logs from Queue 1. Press Ctrl + C to exit ...")

def callback(ch, method, properties, body):
    print("[x] {}: {}".format(method.routing_key, body))

channel.basic_consume(queue=queue_name,on_message_callback=callback,auto_ack=True)
channel.start_consuming()
