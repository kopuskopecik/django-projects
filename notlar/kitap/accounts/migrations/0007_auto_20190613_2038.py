# Generated by Django 2.0 on 2019-06-13 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190611_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etkinlikler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(blank=True, choices=[('k', 'Kitap Okuma Etkinlikleri'), ('a', 'Anlamayı Geliştirme Turnuvası'), ('b', 'Birinci Sınıf Okuma Etkinliği'), ('o', 'Okul Öncesi Masal Etkinliği'), ('l', 'Lise "Kitap Koçum" Etkinliği')], max_length=1)),
                ('hedef', models.PositiveIntegerField(blank=True)),
                ('startting_date', models.DateTimeField(blank=True, max_length=30)),
                ('finishing_date', models.DateTimeField(blank=True, max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='sinif',
            name='hedef',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='isim',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='soyisim',
        ),
        migrations.AddField(
            model_name='sinif',
            name='okunan',
            field=models.PositiveIntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='bireysel_odulu',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='takim_odulu',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='sinif',
            name='asistan',
            field=models.ManyToManyField(blank=True, related_name='asistanlar', to='accounts.Student'),
        ),
        migrations.AlterField(
            model_name='sinif',
            name='ogrenci',
            field=models.ManyToManyField(blank=True, related_name='ogrenciler', to='accounts.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='kitap',
            field=models.ManyToManyField(blank=True, related_name='kitaplar', to='accounts.Kitap'),
        ),
        migrations.AddField(
            model_name='etkinlikler',
            name='ogretmen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Teacher'),
        ),
        migrations.AddField(
            model_name='etkinlikler',
            name='sinif',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='siniflar', to='accounts.Sinif'),
        ),
    ]
