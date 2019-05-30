from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    description = models.CharField(max_length=200)
    price = models.FloatField()
    pub_date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
