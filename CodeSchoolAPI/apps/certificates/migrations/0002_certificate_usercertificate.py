# Generated by Django 2.2.15 on 2020-09-04 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='UserCertificate',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='UserCertificate', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]