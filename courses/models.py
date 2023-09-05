from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(default='default.jpg', upload_to='course_images')
    free = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})

class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    number = models.IntegerField(default=1)
    video_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})


class Comments(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course_exactly = models.ForeignKey(Course, on_delete=models.CASCADE)
