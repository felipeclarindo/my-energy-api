from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout
from users.models import Users

class AuthenticateController:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def register(login: str, password: str, email: str, cpf: str) -> JsonResponse:
        if Users.objects.filter(login=login).exists():
            return JsonResponse({"message": "Login already exists"}, status=400)
        if Users.objects.filter(cpf=cpf).exists():
            return JsonResponse({"message": "CPF already exists"}, status=400)
        if Users.objects.filter(email=email).exists():
            return JsonResponse({"message": "Email already in use"}, status=400)

        try:
            hashed_password = make_password(password)

            user = Users(
                login=data.login,
                email=data.email,
                password=hashed_password,
                cpf=data.cpf,
            )
            user.save()
            return JsonResponse({"message": "User registered successfully"}, status=201)
        except ValidationError as e:
            return JsonResponse({"message": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"message": f"Error registering user: {str(e)}"}, status=400)
    
    @classmethod
    def login(login: str, password: str) -> JsonResponse:
        try:
            user = Users.objects.get(login=data.login)
            checked_password = check_password(data.password, user.password)
            if user and checked_password:
                login(request, user)
                return JsonResponse({"message": "Login successful"}, status=200)
            else:
                return JsonResponse({"message": "Invalid credentials"}, status=400)
        except Exception as e:
            return JsonResponse({"message": f"Error during login: {str(e)}"}, status=400)
    
    @classmethod
    def logout(request) -> JsonResponse:
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({"message": "Logout successful"}, status=200)
        else:
            return JsonResponse({"message": "User is not authenticated"}, status=400)
