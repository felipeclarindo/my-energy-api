from ninja import Router
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout
from django.http import JsonResponse
from users.models import Users
from .schemas import RegisterSchema, LoginSchema
from django.contrib.auth.hashers import check_password, make_password

authenticate_router = Router(tags=["Authenticate"])

@authenticate_router.post("/register", response={201: dict, 400: dict})
def register(request, data: RegisterSchema):
    if Users.objects.filter(login=data.login).exists():
        return JsonResponse({"message": "Login already exists"}, status=400)
    if Users.objects.filter(cpf=data.cpf).exists():
        return JsonResponse({"message": "CPF already exists"}, status=400)
    if Users.objects.filter(email=data.email).exists():
        return JsonResponse({"message": "Email already in use"}, status=400)

    try:
        hashed_password = make_password(data.senha)

        user = Users(
            login=data.login,
            email=data.email,
            senha=hashed_password,
            cpf=data.cpf,
        )
        user.save()
        return JsonResponse({"message": "User registered successfully"}, status=201)
    except ValidationError as e:
        return JsonResponse({"message": str(e)}, status=400)
    except Exception as e:
        return JsonResponse({"message": f"Error registering user: {str(e)}"}, status=400)

@authenticate_router.post("/login", response={200: dict, 400: dict})
def login(request, data: LoginSchema):
    try:
        user = Users.objects.get(login=data.login)
        checked_password = check_password(data.senha, user.senha)
        if user and checked_password:
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=200)
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=400)
    except Exception as e:
        return JsonResponse({"message": f"Error during login: {str(e)}"}, status=400)

@authenticate_router.get("/logout", response={200: dict, 400: dict})
def logout(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({"message": "Logout successful"}, status=200)
    else:
        return JsonResponse({"message": "User is not authenticated"}, status=400)
