from django.db import models

class Profile(models.Model):

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)


class Balance(models.Model):
    class BalanceStatus(models.TextChoices):
        Activating = 'Activating'
        Activ = 'Activ'

    number = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='balance')
    status = models.CharField(max_length=100, choices=BalanceStatus.choices, default=BalanceStatus.Activating)




# Create your models here.
