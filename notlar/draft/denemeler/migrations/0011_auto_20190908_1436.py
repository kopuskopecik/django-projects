# Generated by Django 2.0 on 2019-09-08 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('denemeler', '0010_place_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateField()),
                ('mod_date', models.DateField()),
                ('n_comments', models.IntegerField()),
                ('n_pingbacks', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='entry',
            name='authors',
            field=models.ManyToManyField(to='denemeler.Author'),
        ),
        migrations.AddField(
            model_name='entry',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denemeler.Blog'),
        ),
    ]