# chat/consumers.py

import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from chatterbot import ChatBot


channel_layer = get_channel_layer()

# from .tasks import get_response


def get_response(channel_name, input_data):
    chatterbot = ChatBot(
        'Charlie',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.90
            }
        ]
    )

    response = chatterbot.get_response(input_data)
    response_data = response.serialize()

    async_to_sync(channel_layer.send)(
        channel_name,
        {
            "type": "chat.message",
            "text": {"msg": response_data["text"], "source": "bot"},
        },
    )


class ChatConsumer(WebsocketConsumer):
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        async_to_sync(self.channel_layer.send)(
            self.channel_name,
            {
                "type": "chat_message",
                "text": {"msg": text_data_json["text"], "source": "user"},
            },
        )
        get_response(self.channel_name, text_data_json)

    def chat_message(self, event):
        text = event["text"]
        text_data = json.dumps({"text": text})
        self.send(text_data)
