from multiprocessing.connection import Client
import paho.mqtt.client as mqtt

def process_messagem (client, userdat, message):
    print("Mensagem recebida", str (message.payload.decode("utf-8"))
    print("message topic=",message.topic)
    print("message qos=",message.retain)
    print("message retain flasg=",mesage.retain)

    client = mqtt.Client(client_id='publish-1')

    client.on_connect = connect_msg
    client.on_publish= publish_msg

    client.conenect("12.0.0.1",8080)

    ret= cliente.subscribe("house/light","on")

    client.loop()