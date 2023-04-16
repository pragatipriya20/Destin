# Generated by Django 4.2 on 2023-04-15 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_userprofile_interests"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interests",
            name="Anime",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.animeprofile",
            ),
        ),
        migrations.AlterField(
            model_name="interests",
            name="movies",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.moviesprofile",
            ),
        ),
        migrations.AlterField(
            model_name="interests",
            name="music",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.musicprofile",
            ),
        ),
        migrations.AlterField(
            model_name="interests",
            name="reading",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.readingprofile",
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="interests",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="users.interests"
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="matches",
            field=models.ManyToManyField(
                related_name="matched_user", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="pending",
            field=models.ManyToManyField(
                related_name="pending_users", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]