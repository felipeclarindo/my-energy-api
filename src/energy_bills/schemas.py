from datetime import date
from ninja import Schema

# Schemas for managing EnergyBills
class EnergyBillsSchema(Schema):
    consumption: float 
    value: float 
    data: date

    def validate(self):
        if self.consumo <= 0:
            raise ValueError("Consumption must be greater than 0.")
        if self.valor <= 0:
            raise ValueError("Value must be greater than 0.")


class CreateEnergyBillsSchema(Schema):
    consumption: float 
    value: float 
    data: date

    def validate(self):
        if self.consumo <= 0:
            raise ValueError("Consumption must be greater than 0.")
        if self.valor <= 0:
            raise ValueError("Value must be greater than 0.")
