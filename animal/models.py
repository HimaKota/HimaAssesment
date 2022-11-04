from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Breed(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    breed = models.CharField(max_length=40)

    def __str__(self):
        return self.breed

class UserEntry(models.Model):
    
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, blank=True, null=True)
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.CharField(max_length=124)

    def __str__(self):
        return self.date
    class Meta:
        verbose_name = 'UserEntry'
        verbose_name_plural = 'User Entries'