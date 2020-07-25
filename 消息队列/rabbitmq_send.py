import pika

connection = pika.BlockingConnection(pika.ConnectionParameters())
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='welcome to hello queue.',
    properties=pika.BasicProperties(delivery_mode=2,))
print('message:' + 'welcome to hello queue.')
connection.close()
