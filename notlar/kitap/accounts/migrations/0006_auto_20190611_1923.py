# Generated by Django 2.0 on 2019-06-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190610_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='kitap',
            field=models.ManyToManyField(blank=True, null=True, related_name='kitaplar', to='accounts.Kitap'),
        ),
        migrations.AlterField(
            model_name='student',
            name='takim',
            field=models.CharField(blank=True, choices=[('t', 'Turuncu'), ('m', 'Mavi'), ('k', 'Kırmızı'), ('s', 'Sarı'), ('y', 'Yeşil')], max_length=1),
        ),
    ]
