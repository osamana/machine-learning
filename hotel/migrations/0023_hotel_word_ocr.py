# Generated by Django 2.1.7 on 2019-04-16 17:11

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0022_hotelmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='word_ocr',
            field=picklefield.fields.PickledObjectField(blank=True, editable=False, null=True),
        ),
    ]