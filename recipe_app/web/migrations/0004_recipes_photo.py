# Generated by Django 4.1.7 on 2023-03-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_recipes_created_at_recipes_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]