from django.db import models


class ClientsList(models.Model):
    # Creates a model that will contain the entire list of customers
    name = models.CharField('Name', max_length=500)
    full_name = models.CharField('Full name', max_length=500)
    email = models.CharField('Email', max_length=500)
    password = models.IntegerField('Passwords')
    reg_date = models.DateTimeField('Data')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "client"
        verbose_name_plural= "clients"
