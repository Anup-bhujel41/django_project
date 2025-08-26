from django.db import models

class Biodata(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()   
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.name + str(self.age)
