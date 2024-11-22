from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    



    def purchased_horses(self):
        return ", ".join(horse.name for horse in self.horses.all())
    purchased_horses.short_description = 'Купленные лошади'


class Horse(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    age = models.IntegerField()
    height = models.IntegerField()
    location = models.CharField(max_length=30)
    description = models.TextField()
    cost = models.DecimalField(decimal_places=2 , max_digits=15)
    photo = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    buyer = models.ManyToManyField(Buyer, related_name='horses', blank=True)
