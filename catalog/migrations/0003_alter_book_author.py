# Generated by Django 5.0.2 on 2024-02-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_genre_id_book_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='catalog.author'),
        ),
    ]
