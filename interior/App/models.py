from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=150)
    mail = models.CharField(max_length=200)
    psw = models.CharField(max_length=10)
    pswr = models.CharField(max_length=10)

    def __str__(self):
        return self.name