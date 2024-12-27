from django.http import JsonResponse, HttpRequest
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout
from users.models import Users
from django.contrib.auth.hashers import make_password, check_password
from .schemas import LoginSchema, RegisterSchema

class AuthenticateController:
    @classmethod
    def register(cls, data: RegisterSchema) -> JsonResponse:
        """
        Register a new user in the database.

        Args:
            data (RegisterSchema): User data to register.

        Returns:
            JsonResponse: Response with the registration status.
        """
        if Users.objects.filter(login=login).exists():
            return JsonResponse({"message": "Login already exists"}, status=400)
        if Users.objects.filter(cpf=data.cpf).exists():
            return JsonResponse({"message": "CPF already exists"}, status=400)
        if Users.objects.filter(email=data.email).exists():
            return JsonResponse({"message": "Email already in use"}, status=400)

        try:
            hashed_password = make_password(data.password)

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
    def login(cls, request: HttpRequest, data: LoginSchema) -> JsonResponse:
        """
        Verify existing user credentials and login.

        Args:
            request (HttpRequest): Request from the user.
            data (LoginSchema): User credentials to login.

        Returns:
            JsonResponse: Response with the login status.
        """
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
    def logout(cls, request) -> JsonResponse:
        """
        Verify if the user is authenticated and logout.

        Args:
            request (HttpRequest): Request from the user.

        Returns:
            JsonResponse: Response with the logout status.
        """
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({"message": "Logout successful"}, status=200)
        else:
            return JsonResponse({"message": "User is not authenticated"}, status=400)
