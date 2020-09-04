# Generated by Django 2.2.15 on 2020-09-04 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0003_waitlistentry_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitlistentry',
            name='level',
            field=models.CharField(choices=[('Entry', 'Entry'), ('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior')], default='Entry', max_length=50, verbose_name='Class Level'),
        ),
    ]