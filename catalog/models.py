from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, null=True)
    author = models.ManyToManyField('Author')
    description = models.TextField(max_length=1000)
    inprint = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    ISBN = models.CharField(max_length=13)

    """Удобно читаемое имя для админки"""
    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.last_name
