# Generated by Django 4.2.4 on 2023-08-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='628284_avatar_male_man_mature_old_icon.png', upload_to='user_images', verbose_name='User photo'),
        ),
    ]
