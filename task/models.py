from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse



class table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task-detail", kwargs={"pk": self.pk})
    