# Generated by Django 2.2.5 on 2019-09-30 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_game_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threadimage',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_image', to='game.Thread'),
        ),
    ]
