from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30,
                            unique=True,
                            verbose_name='Category Name')

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=120,
                            unique=True,
                            verbose_name='Game Name')
    image = models.ImageField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name