# Generated by Django 3.1 on 2021-11-23 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='tot_marks',
            field=models.IntegerField(default=0),
        ),
    ]
