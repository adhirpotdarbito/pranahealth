import pika
from __config import *
from __message_queue import *

class RabbitMq(MessageQueue):
    def __init__(self):
        super(RabbitMq, self).__init__()
        self.host = host
        self.port = port

    def connectServer(self):
        super(RabbitMq, self).connectServer()
        credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
        parameter = pika.ConnectionParameters(host=self.host, port=self.port,heartbeat=0, credentials=credentials)
        self.connection = pika.BlockingConnection(parameter)
        return self.connection
        
    def disconnectServer(self):
        super(RabbitMq, self).disconnectServer()
        return self.connection.close()
           
    def createChannel(self):
        super(RabbitMq, self).createChannel() 
        self.channel = self.connection.channel()

    def publishData(self, data):
        super(RabbitMq, self).publishData(data)
        self.createChannel()
        self.channel.queue_declare(queue=queue_name_blockchain, durable=True)
        self.channel.queue_declare(queue=queue_name_notification, durable=True)
        self.channel.queue_declare(queue=queue_name_db, durable=True)
        self.channel.basic_publish(exchange='', routing_key=queue_name_blockchain, body=data, properties=pika.BasicProperties(delivery_mode=2))
        self.channel.basic_publish(exchange='', routing_key=queue_name_notification, body=data, properties=pika.BasicProperties(delivery_mode=2))
        self.channel.basic_publish(exchange='', routing_key=queue_name_db, body=data, properties=pika.BasicProperties(delivery_mode=2))

    def consumeData(self, callback, queue_name):
        super(RabbitMq, self).consumeData()
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True) 
        self.channel.start_consuming()
    
    def sendHeartBeat(self):
        self.connection.process_data_events() 
