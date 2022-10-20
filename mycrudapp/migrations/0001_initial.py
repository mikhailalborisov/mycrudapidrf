# Generated by Django 4.1.2 on 2022-10-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Film",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название фильма",
                        max_length=100,
                        verbose_name="Название фильма",
                    ),
                ),
                (
                    "genre",
                    models.CharField(
                        help_text="Введите жанр фильма",
                        max_length=100,
                        verbose_name="Жанр фильма",
                    ),
                ),
                (
                    "director",
                    models.CharField(
                        help_text="Введите фамилию режиссера",
                        max_length=100,
                        verbose_name="Фамилия режиссера",
                    ),
                ),
                (
                    "release_date",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату выпуска",
                        null=True,
                        verbose_name="Дaтa выпуска",
                    ),
                ),
            ],
        ),
    ]
