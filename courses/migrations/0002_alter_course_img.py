# Generated by Django 4.2.4 on 2023-08-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='course_images'),
        ),
    ]