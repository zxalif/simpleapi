from django.contrib import admin

from .models import (
    Category,
    Game,
    Thread,
    ThreadImage
)

admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Thread)
admin.site.register(ThreadImage)