import time
from pika import BlockingConnection, ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel 

QUEUE_NAME = "basic_channel"

def send_message(channel: BlockingChannel, body: str):
    """
    Send a basic message to the given channel
    
    :param channel: The channel to send to.
    :param body: The body to send.
    """
    print(f"Sending message: {body}")
    channel.basic_publish(
        exchange="",
        routing_key=QUEUE_NAME,
        body=body
    )
    
def run_distributer(connection):
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)


    for counter in range(10000):
        send_message(channel, f"Message number: {counter}")

    connection.close()

if __name__ == "__main__":
    while True:
        try:
            time.sleep(1)
            connection = BlockingConnection(ConnectionParameters('rabbitmq'))
            break
        except Exception:
            print("Rabbitmq is down!")
    
    run_distributer(connection)