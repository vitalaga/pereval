# Generated by Django 4.2.2 on 2023-07-05 21:28

from django.db import migrations, models
import perevalapp.services


class Migration(migrations.Migration):

    dependencies = [
        ('perevalapp', '0002_alter_users_email_alter_users_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=perevalapp.services.get_path_upload_photos, verbose_name='Изображение'),
        ),
    ]