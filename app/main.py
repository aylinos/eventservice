# import pika
from fastapi import FastAPI
from mangum import Mangum  # Amazon Lambda handler

from .routers import eventrouter, typerouter

# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()
#
# channel.queue_declare(queue='hello')
#
#
# def callback(ch, method, properties, body):
#     print(" [x] Received %r" % body)
#
#
# channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
#
# print(' [*] Waiting for messages. To exit press CTRL+C')
# channel.start_consuming()

app = FastAPI()

app.include_router(eventrouter.router)
app.include_router(typerouter.router)


# Index route
@app.get("/")
def read_root():
    return {"Eventor": "Welcome to EVENTS service"}


handler = Mangum(app=app)  # <----------- wrap the API with Mangum
