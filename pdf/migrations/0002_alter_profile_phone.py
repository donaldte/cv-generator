# Generated by Django 3.2.7 on 2021-10-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
