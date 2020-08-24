# Generated by Django 2.0 on 2020-01-14 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hesaplar', '0001_initial'),
        ('dersler', '0007_studentbaslikanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakenBaslikQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('baslik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dersler.Baslik')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hesaplar.Student')),
            ],
        ),
    ]