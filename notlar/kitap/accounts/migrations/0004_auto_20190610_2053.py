# Generated by Django 2.0 on 2019-06-10 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190610_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinif',
            name='asistan',
            field=models.ManyToManyField(blank=True, null=True, related_name='asistanlar', to='accounts.Student'),
        ),
        migrations.AlterField(
            model_name='sinif',
            name='ogrenci',
            field=models.ManyToManyField(blank=True, null=True, related_name='ogrenciler', to='accounts.Student'),
        ),
        migrations.AlterField(
            model_name='sinif',
            name='ogretmen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ogretmenler', to='accounts.Teacher'),
        ),
    ]