# Generated by Django 3.2.9 on 2022-09-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_todo_app_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo_app',
            name='date_done',
            field=models.DateTimeField(auto_now=True),
        ),
    ]