# Generated by Django 3.1.1 on 2021-11-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_auto_20211124_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='bio',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Students history'),
        ),
    ]
