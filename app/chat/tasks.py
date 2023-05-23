# chat/tasks.py

from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings

channel_layer = get_channel_layer()


@shared_task
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
