# Generated by Django 3.1.1 on 2020-09-21 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20200921_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentrelationship',
            name='liked_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]