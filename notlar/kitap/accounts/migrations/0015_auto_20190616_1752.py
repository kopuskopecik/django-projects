# Generated by Django 2.0 on 2019-06-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20190616_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etkinlik',
            name='isim',
            field=models.CharField(choices=[('k', 'Kitap Okuma Turnuvası'), ('p', 'Kitap Okuma Etkinlikleri'), ('a', 'Anlamayı Geliştirme Turnuvası'), ('b', 'Birinci Sınıf Okuma Etkinliği'), ('o', 'Okul Öncesi Masal Etkinliği'), ('l', 'Lise "Kitap Koçum" Etkinliği')], max_length=1),
        ),
    ]