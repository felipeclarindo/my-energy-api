from ninja import Schema

class LoginSchema(Schema):
    login: str
    password: str

class RegisterSchema(Schema):
    login: str
    password: str
    email: str
    cpf: str