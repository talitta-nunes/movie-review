# Generated by Django 4.1 on 2022-08-20 18:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="user",
            new_name="critic",
        ),
        migrations.AlterField(
            model_name="review",
            name="stars",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(10),
                    django.core.validators.MinValueValidator(1),
                ]
            ),
        ),
    ]
