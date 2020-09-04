# Generated by Django 2.2.15 on 2020-09-04 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0002_auto_20200904_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitlistentry',
            name='level',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior')], default=1, max_length=50, verbose_name='Class Level'),
            preserve_default=False,
        ),
    ]
