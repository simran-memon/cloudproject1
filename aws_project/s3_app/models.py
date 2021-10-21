from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class s3Object(models.Model):
    #author = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    s3_storage_object = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    def delete(self, *args, **kwargs):
        self.s3_storage_object.delete()
        super().delete(*args, **kwargs)

