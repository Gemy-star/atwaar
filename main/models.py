from django.db import models

class Contact(models.Model):
    name = models.CharField(null=True ,max_length=255 , verbose_name='Name')
    email = models.EmailField(null=True , verbose_name='Email Address')
    phone = models.CharField(null=True ,max_length=255 , verbose_name='Phone')
    def __str__(self):
        return self.name
