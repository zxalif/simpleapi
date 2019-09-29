from django.core.management.base import BaseCommand

from game.models import Category, Game

from tqdm import tqdm
import random

from faker import Faker


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-n', '--number', type=int, required=True, help='Number of element')

    def handle(self, **kwargs):
        fake = Faker()
        number = kwargs['number']
        tmp = []
        for _ in tqdm(range(number)):
            cat = Category.objects.create(name=fake.name())
            cat.save()
            tmp.append(cat)
            game = Game.objects.create(category=random.choice(tmp))
            game.name = fake.name()
            game.image = 'https://i.ytimg.com/vi/uODKrZnGk7g/maxresdefault.jpg'
            game.description = fake.text()
            game.save()