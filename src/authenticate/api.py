from ninja import Router
from users.models import Users
from django.contrib.auth.hashers import check_password, make_password
from .controller import AuthenticateController
from .schemas import RegisterSchema, LoginSchema

authenticate_router = Router(tags=["Authenticate"])

@authenticate_router.post("/register", response={201: dict, 400: dict})
def register(request, data: RegisterSchema):
    AuthenticateController.register(data.login, data.password, data.email, data.cpf)

@authenticate_router.post("/login", response={200: dict, 400: dict})
def login(request, data: LoginSchema):
    AuthenticateController.login(data.login, data.password)

@authenticate_router.get("/logout", response={200: dict, 400: dict})
def logout(request):
    AuthenticateController.logout(request)