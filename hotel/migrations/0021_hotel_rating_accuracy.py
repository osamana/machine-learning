# Generated by Django 2.1.7 on 2019-04-05 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0020_remove_hotel_data_membergroup_x_avgrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='rating_accuracy',
            field=models.IntegerField(default=0),
        ),
    ]
