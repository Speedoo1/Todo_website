# Generated by Django 3.2.9 on 2022-09-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_app',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
