import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue # get name of queue
print("queue_name: {}".format(queue_name))

channel.queue_bind(exchange='logs', queue=queue_name)

print("waiting for logs ... ")


def callback(ch, method, properties, body):
	print("[x]: {}".format(body))

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()