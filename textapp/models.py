from django.db import models

# Create your models here.
class Inquire(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.IntegerField()
    query=models.TextField()

    def __str__(self):
        return self.name

