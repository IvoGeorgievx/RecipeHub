# Generated by Django 4.1.7 on 2023-03-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0006_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
