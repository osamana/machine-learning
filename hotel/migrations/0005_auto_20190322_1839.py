# Generated by Django 2.1.7 on 2019-03-22 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='review',
            name='nights',
            field=models.SmallIntegerField(default=1, verbose_name='Nights'),
        ),
    ]
