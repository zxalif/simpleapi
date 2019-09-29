from django.core.management.base import BaseCommand
from django.core.files import File

from tqdm import tqdm

import random
import glob

from game.models import Game


class Command(BaseCommand):
    images = glob.glob('/home/alif/Pictures/*.png')
    def handle(self, **kwargs):
        games = Game.objects.all()
        for game in tqdm(games):
            img = random.choice(self.images)
            name = img.split('/')[-1]
            game.image.save(name, File(open(img, 'rb')))
            game.save()