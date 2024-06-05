from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Gallery(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(Brand, related_name='cars', on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE)
    rentedBy = models.ForeignKey(Gallery, related_name='cars', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.brand} | {self.model}'
