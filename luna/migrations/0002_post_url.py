# Generated by Django 4.2 on 2023-05-01 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("luna", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="url",
            field=models.URLField(blank=True, verbose_name="Ссылка"),
        ),
    ]
