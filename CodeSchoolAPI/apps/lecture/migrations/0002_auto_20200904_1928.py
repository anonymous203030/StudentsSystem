# Generated by Django 2.2.15 on 2020-09-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='lecturer_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='slides_url',
            field=models.CharField(max_length=255),
        ),
    ]