from django.db import models

# Create your models here.
class Contact(models.Model):
    name                      = models.CharField(max_length=200)
    email                     = models.EmailField()
    phone                     = models.CharField(max_length=120,blank=True,null=True)#not required
    content                   = models.TextField()

    class Meta:
        verbose_name          = 'Contact Message'
        verbose_name_plural   = 'Contact Messages'
