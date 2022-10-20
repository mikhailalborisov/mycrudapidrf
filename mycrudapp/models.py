from django.db import models

# Create your models here.
class Film(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Введите название фильма",
        verbose_name="Название фильма",
    )
    genre = models.CharField(
        max_length=100,
        help_text="Введите жанр фильма",
        verbose_name="Жанр фильма",
    )
    director = models.CharField(
        max_length=100,
        help_text="Введите фамилию режиссера",
        verbose_name="Фамилия режиссера",
    )
    release_date = models.DateField(
        help_text="Введите дату выпуска",
        verbose_name="Дaтa выпуска",
        null=True,
        blank=True,
    )