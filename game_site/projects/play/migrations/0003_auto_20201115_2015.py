# Generated by Django 3.1.3 on 2020-11-15 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0002_game_game_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_image',
        ),
        migrations.CreateModel(
            name='Game_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.game')),
            ],
        ),
    ]