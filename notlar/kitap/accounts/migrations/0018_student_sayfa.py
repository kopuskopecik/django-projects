# Generated by Django 2.0 on 2019-06-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_student_ogretmen'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sayfa',
            field=models.PositiveIntegerField(default=0),
        ),
    ]