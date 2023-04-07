from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100, default='John Doe')
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"