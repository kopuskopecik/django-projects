# Generated by Django 2.0 on 2019-09-26 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('denemeler', '0013_auto_20190911_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('pages', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.FloatField()),
                ('pubdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('books', models.ManyToManyField(to='denemeler.Book')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='denemeler.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denemeler.Publisher'),
        ),
    ]
