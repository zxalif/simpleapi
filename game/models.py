from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Category Name'
    )

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(
        max_length=120,
        unique=True,
        verbose_name='Game Name'
    )
    image = models.ImageField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    description = models.TextField(default='')

    # slug = models.CharField(
    #     max_length=120,
    #     unique=True,
    #     editable=False,
    # )

    def __str__(self):
        return self.name


class Thread(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
    )
    alias_name = models.CharField(
        max_length=120
    )
    email = models.EmailField(
        max_length=70,
        db_index=True,
        null=True,
    )
    anonymous = models.BooleanField(
        default=False,
        verbose_name='Hide details'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    comment = models.TextField()

    def __str__(self):
        return self.alias_name

class ThreadImage(models.Model):
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE
    )
    image = models.ImageField()

    def __str__(self):
        return self.image.name