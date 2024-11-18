from ninja import Router
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout
from django.http import JsonResponse
from users.models import Users
from .schemas import RegisterSchema, LoginSchema
from django.contrib.auth.hashers import check_password

authenticate_router = Router(tags=["Authenticate"])

@authenticate_router.post("/register", response={201: dict, 400: dict})
def register(request, data: RegisterSchema):
    if Users.objects.filter(login=data.login).exists():
        return JsonResponse({"success": False, "message": "Login already exists"}, status=400)
    if Users.objects.filter(cpf=data.cpf).exists():
        return JsonResponse({"success": False, "message": "CPF already exists"}, status=400)
    if Users.objects.filter(email=data.email).exists():
        return JsonResponse({"success": False, "message": "Email already in use"}, status=400)

    try:
        user = Users(
            login=data.login,
            senha=data.senha, 
            email=data.email,
            cpf=data.cpf,
        )
        user.save()
        return JsonResponse({"success": True, "message": "User registered successfully"}, status=201)
    except ValidationError as e:
        return JsonResponse({"success": False, "message": str(e)}, status=400)
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Error registering user: {str(e)}"}, status=400)

@authenticate_router.post("/login", response={200: dict, 400: dict})
def login_view(request, data: LoginSchema):
    try:
        user = Users.objects.filter(login=data.login)
        if user and check_password(data.senha, user.senha):
            login(request, user)
            return JsonResponse({"success": True, "message": "Login successful"}, status=200)
        else:
            return JsonResponse({"success": False, "message": "Invalid credentials"}, status=400)
    
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Error during login: {str(e)}"}, status=400)

@authenticate_router.post("/logout", response={200: dict})
def logout_view(request):
    logout(request)
    return JsonResponse({"success": True, "message": "Logout successful"}, status=200)
