# Generated by Django 3.1.1 on 2021-11-26 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_auto_20211126_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='invite_reason',
            field=models.TextField(),
        ),
    ]
