from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title
