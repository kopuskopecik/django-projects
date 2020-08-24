# Generated by Django 2.0 on 2020-01-14 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hesaplar', '0001_initial'),
        ('dersler', '0006_baslik_begenilme_sayisi'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentBaslikAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dersler.Answer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hesaplar.Student')),
            ],
        ),
    ]
