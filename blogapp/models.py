from django.db import models

# Create your models here.

class blogtable(models.Model):

    name = models.CharField(max_length=100)
    blogcontent = models.CharField(max_length=100000)

    def __str__(self):
        return self.name + " - " + self.blogcontent