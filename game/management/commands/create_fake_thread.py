from django.core.management.base import BaseCommand

from tqdm import tqdm
from faker import Faker

import random

from game.models import Game, Thread


class Command(BaseCommand):
    fake = Faker()

    def add_arguments(self, parser):
        parser.add_argument('-n', '--number', type=int, required=True, help='Number of element')

    def handle(self, **kwargs):
        number = kwargs['number']

        for _ in tqdm(range(number)):
            game = random.choice(Game.objects.all())
            thread = Thread.objects.create(game=game)
            thread.alias_name = self.fake.name()
            thread.email = self.fake.email()
            thread.anonymous = random.choice([True, False])
            thread.comment = self.fake.text()
            thread.save()


