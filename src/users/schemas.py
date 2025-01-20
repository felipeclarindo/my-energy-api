from decimal import Decimal
from datetime import datetime
from ninja import Schema

# Schemas for managing Users
class UserSchema(Schema):
    id: int
    cpf: str
    login: str
    email: str

class CreateUserSchema(Schema):
    cpf: str
    login: str
    password: str
    email: str
