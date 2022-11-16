from django.db import models

# Create your models here.

TYPE_CHOICES = [
    ('Em gotas','Em gotas'),
    ('Comprimido','Comprimido'),
]

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.name} {self.email} {self.birth_date}'

class Medicament(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100,choices=TYPE_CHOICES)
    price = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return f'{self.name} {self.type} {self.price}'

class Pharmacy(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Request(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    medicament = models.ManyToManyField(Medicament)
    pharmacy = models.ForeignKey(Pharmacy,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.client.name} {self.medicament.name} {self.pharmacy.name}'