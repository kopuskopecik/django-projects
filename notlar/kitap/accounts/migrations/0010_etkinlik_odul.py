# Generated by Django 2.0 on 2019-06-15 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20190614_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='etkinlik',
            name='odul',
            field=models.CharField(blank=True, choices=[('b', 'Birinci Ödül'), ('i', 'İkinci Ödül'), ('ü', 'Üçüncü Ödül'), ('d', 'Dördüncü Ödül')], max_length=1),
        ),
    ]