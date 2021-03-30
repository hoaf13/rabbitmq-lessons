import pika 
import time 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
product = 100 


while True:
	channel.basic_publish(exchange='logs', routing_key='', body= str(product))
	print('[x] send {}'.format(product))
	product += 1
	time.sleep(0.5)

connection.close()