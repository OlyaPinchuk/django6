# Generated by Django 3.1.7 on 2021-04-04 22:29

from django.db import migrations, models
import user_profile.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_profilemodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='avatar',
            field=models.ImageField(upload_to=user_profile.models.to_upload),
        ),
    ]
