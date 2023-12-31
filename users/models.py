from django.db import models
from django.contrib.auth.models import User
from PIL import Image

TYPE_CHOICES = (
    ('Full pack', 'full'),
    ('Free pack', 'free')
)

USER_STATUS = (
    ('Only read', 'user'),
    ('Redaction', 'redactor')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('User photo', default='default.jpg', upload_to='user_images')
    account_type = models.CharField(choices=TYPE_CHOICES, default='Free pack', max_length=30)
    user_status = models.CharField(choices=USER_STATUS, default='Only read', max_length=30)

    def __str__(self):
        return f'Profile user {self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)



    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

