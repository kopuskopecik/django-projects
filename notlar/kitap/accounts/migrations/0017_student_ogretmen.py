# Generated by Django 2.0 on 2019-06-16 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20190616_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ogretmen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Teacher'),
        ),
    ]
