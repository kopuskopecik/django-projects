# Generated by Django 2.0 on 2020-01-10 12:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dersler', '0003_auto_20200108_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ranking',
            field=models.IntegerField(default=0, verbose_name='Sıra:'),
        ),
        migrations.AlterField(
            model_name='baslik',
            name='ranking',
            field=models.IntegerField(default=0, verbose_name='Sıra'),
        ),
        migrations.AlterField(
            model_name='baslik',
            name='youtube_urli',
            field=models.URLField(blank=True, verbose_name='Youtube Url Adresi'),
        ),
        migrations.AlterField(
            model_name='ders',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='İçerik:'),
        ),
        migrations.AlterField(
            model_name='ders',
            name='ranking',
            field=models.IntegerField(default=0, verbose_name='Sıra:'),
        ),
        migrations.AlterField(
            model_name='ders',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Dersinizin Başlığı:'),
        ),
        migrations.AlterField(
            model_name='ders',
            name='youtube_urli',
            field=models.URLField(blank=True, verbose_name='Youtube linki:'),
        ),
    ]
