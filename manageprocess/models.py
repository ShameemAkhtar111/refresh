from django.db import models

# Create your models here.
class PGroup(models.Model):
    group_name=models.CharField(max_length=20)

    def __str__(self):
        return self.group_name