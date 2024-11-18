from decimal import Decimal
from datetime import date
from ninja import Schema

# Schemas for managing EnergyBills
class EnergyBillSchema(Schema):
    id: int
    cpf: int
    consumo: Decimal 
    valor: Decimal 
    data: date

    def validate(self):
        if self.consumo <= 0:
            raise ValueError("Consumption must be greater than 0.")
        if self.valor <= 0:
            raise ValueError("Value must be greater than 0.")


class CreateEnergyBillSchema(Schema):
    cpf: int
    consumo: Decimal 
    valor: Decimal 
    data: date

    def validate(self):
        if self.consumo <= 0:
            raise ValueError("Consumption must be greater than 0.")
        if self.valor <= 0:
            raise ValueError("Value must be greater than 0.")
