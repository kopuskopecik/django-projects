# Generated by Django 2.0 on 2019-06-14 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190614_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etkinlik',
            name='finishing_date',
            field=models.DateTimeField(auto_now=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='etkinlik',
            name='startting_date',
            field=models.DateTimeField(auto_now_add=True, max_length=30),
        ),
    ]