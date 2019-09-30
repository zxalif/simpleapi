from django.core.management.base import BaseCommand
from django.core.files import File

from tqdm import tqdm

import glob
import random

from game.models import Game, Thread, ThreadImage


class Command(BaseCommand):

    images = glob.glob('/home/alif/Pictures/*.png')

    def handle(self, **kwargs):
        for obj in tqdm(Thread.objects.all()):
            for i in range(0, random.randint(2, 5)):
                thread_image = ThreadImage.objects.create(thread=obj)
                img = random.choice(self.images)
                name = img.split('/')[-1]
                thread_image.image.save(name, File(open(img, 'rb')))
                thread_image.save()