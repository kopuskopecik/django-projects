# Generated by Django 2.0 on 2019-06-15 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_etkinlik_odul'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='isim',
        ),
        migrations.RemoveField(
            model_name='student',
            name='soyisim',
        ),
    ]