from ninja import Schema

class LoginSchema(Schema):
    login: str
    senha: str

class RegisterSchema(Schema):
    login: str
    senha: str
    email: str
    cpf: str