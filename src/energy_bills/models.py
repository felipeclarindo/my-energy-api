from django.db import models
from users.models import Users
# Create your models here.
class EnergyBills(models.Model):
    id = models.AutoField(primary_key=True)
    consumption = models.FloatField()
    value = models.FloatField()
    data = models.DateField()
    
    def __str__(self):
        return f"Bills for {self.cpf} on {self.data}"
    
    class Meta:
        db_table = 'energy_bills'