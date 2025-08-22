from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Аниме', 'Anime'),
        ('Биография', 'Biography'),
        ('Боевик', 'Action'),
        ('Вестерн', 'Western'),
        ('Военный', 'Military'),
        ('Детектив', 'Detective'),
        ('Детский', 'Children'),
        ('Документальный', 'Documentary'),
        ('Драма', 'Drama'),
        ('Комедия', 'Comedy'),
        ('Криминал', 'Crime'),
        ('Мелодрама', 'Melodrama'),
        ('Мюзикл', 'Musical'),
        ('Ужасы', 'Horrors'),
        ('Триллер', 'Thriller'),
        ('Научная фантастика', 'Science fiction'),
        ('Фэнтези', 'Fantasy'),
        ('Фильм-нуар', 'Film noir'),
        ('Семейный', 'Family'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(choices=GENRE_CHOICES)
    year = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title