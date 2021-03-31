import pika 
import sys
import time 


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

queue = channel.queue_declare(queue='topic_queue2', exclusive=True, durable=True)
queue_name = queue.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(queue=queue_name, exchange='topic_logs', routing_key=binding_key)

print("[x] waiting for logs. Press Ctrl + C to exit")

def callback(ch, method, properties, body):
    print(" [x] from queue: {} -  routing_key: {} -  product: {}".format(queue_name, method.routing_key, body))


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()