# Generated by Django 2.2 on 2019-08-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0003_user_last_visit")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        )
    ]