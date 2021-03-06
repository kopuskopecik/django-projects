# Generated by Django 2.0 on 2020-01-07 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hesaplar', '0001_initial'),
        ('dersler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='takenquiz',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hesaplar.Student'),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dersler.Answer'),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hesaplar.Student'),
        ),
        migrations.AddField(
            model_name='question',
            name='ders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dersler.Ders'),
        ),
        migrations.AddField(
            model_name='ders',
            name='baslik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dersler.Baslik'),
        ),
        migrations.AddField(
            model_name='baslik',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dersler.Question'),
        ),
    ]
