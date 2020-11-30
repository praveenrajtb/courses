from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


def course_directory_path(instance, filename):
    return 'courses/'.format(instance.id, filename)


def user_directory_path(instance, filename):
    return 'users/'.format(instance.id, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_directory_path)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(
        upload_to=course_directory_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    start_date = models.DateTimeField(
          default=timezone.now)
    end_date = models.DateTimeField(
          default=timezone.now)
    slug = models.SlugField(max_length=250)

    def get_absolute_url(self):
        return reverse('course:course-detail', args=[self.slug])
