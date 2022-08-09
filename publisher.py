import pika
from pika.exchange_type import ExchangeType
# create connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
# create channe from the connection
channel = connection.channel()

# declare the name of the queue
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

message = 'hello this is ali calling '
channel.basic_publish(exchange='pubsub', routing_key='', body=message)
print("message sent...")
channel.close()
