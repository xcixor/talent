import os
from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer


class Command(BaseCommand):
    help = "Training the chatbot"

    def handle(self, *args, **options):
        chatterbot = ChatBot(**settings.CHATTERBOT)
        trainer = ListTrainer(chatterbot)
        __location__ = os.path.realpath(os.path.join(
            os.getcwd(), os.path.dirname(__file__)))
        training_data = open(os.path.join(
            __location__, 'data/initial.txt'),
            encoding='utf-8').read().splitlines()
        trainer.train(training_data)

        self.stdout.write(self.style.SUCCESS("Successfull!"))
