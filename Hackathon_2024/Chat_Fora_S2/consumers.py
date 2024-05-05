from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.channel_name = self.channel_name


    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        recipient_channel_name = data['recipient_channel_name']
        
        # Envoyer le message au client spécifique
        self.send(text_data=json.dumps({'message': message}), channel=recipient_channel_name)
