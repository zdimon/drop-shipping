import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class MarketConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)("notifications", self.channel_name)
        

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)

    def send_notify(self, event):
        print(event)
        self.send(text_data=json.dumps({"action": "update_notify", "data": "Update please"}))

