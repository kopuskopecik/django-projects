# Generated by Django 2.0 on 2019-06-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_student_sayfa'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='no',
            field=models.PositiveIntegerField(default=0),
        ),
    ]