# Generated by Django 2.2 on 2019-09-04 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("projects", "0028_auto_20190904_1125")]

    operations = [
        migrations.RemoveField(model_name="project", name="admins"),
        migrations.RemoveField(model_name="project", name="members"),
    ]
