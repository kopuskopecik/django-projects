# Generated by Django 2.0 on 2019-09-03 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denemeler', '0004_auto_20190903_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='model1',
            options={'default_permissions': (), 'ordering': ['number']},
        ),
    ]
