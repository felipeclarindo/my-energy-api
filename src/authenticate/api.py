from django.http import JsonResponse, HttpRequest
from ninja import Router
from .controller import AuthenticateController
from .schemas import RegisterSchema, LoginSchema

authenticate_router = Router(tags=["Authenticate"])

@authenticate_router.post("/register", response={201: dict, 400: dict})
def register(request: HttpRequest, data: RegisterSchema) -> JsonResponse:
    """
    Route to register a new user.

    Args:
        request (HttpRequest): Request from the user.
        data (RegisterSchema): User data to register.

    Returns:
        JsonResponse: Response with the registration status.
    """
    return AuthenticateController.register(data)

@authenticate_router.post("/login", response={200: dict, 400: dict})
def login(request: HttpRequest, data: LoginSchema) -> JsonResponse:
    """
    Route to login the user if exists.

    Args:
        request (HttpRequest): Request from the user.
        data (LoginSchema): Credentials to verify and make login

    Returns:
        JsonResponse: Response with the login status.
    """
    return AuthenticateController.login(request, data)

@authenticate_router.get("/logout", response={200: dict, 400: dict})
def logout(request: HttpRequest) -> JsonResponse:
    """
    Route to logout the user.

    Args:
        request (HttpRequest): Request from the user.

    Returns:
        JsonResponse: Response with the logout status.
    """
    return AuthenticateController.logout(request)