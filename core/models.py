from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE
    )
    nickname = models.CharField(max_length=55)
    description=models.TextField(null=True,blank=True)

class Post(models.Model):
    name=models.CharField('Заголовок', max_length=100, null=True, blank=True)
    description=models.TextField(null=True,blank=True)
    photo=models.ImageField(null=True,blank=True)
    status=models.Choices("Опубликован","Не опубликован")
    likes=models.PositiveIntegerField(default=0)
    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
    def __str__(self):
            return self.name

class Category(models.Model):
    l = ((1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    name=models.CharField('Наименование столбца', max_length=50, null=True)
    rating=models.PositiveSmallIntegerField(choices=l)
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
    def __str__(self):
        return self.name

class Short(models.Model):
     user = models.ManyToManyField(
          to=User,
          null=True,
          blank=False,
          verbose_name='Автор',
          related_name='short'
     )
     video = models.FileField(upload_to='video_post/',null=True,blank=True)
     data = models.DateField(auto_now_add=True)
     views = models.PositiveIntegerField(default=0)

class SavedPost(models.Model):
     user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE
    )
     post = models.ManyToManyField(
        to=Post,
     )
