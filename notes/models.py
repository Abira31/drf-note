from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    author = models.ForeignKey(User,null=True,blank=False,on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-update']
