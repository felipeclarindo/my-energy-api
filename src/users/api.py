from ninja import Router
from .schemas import UserSchema, CreateUserSchema
from .controller import UsersController
from django.http import JsonResponse, HttpRequest

# Create a router for the users
users_router = Router(tags=["Users"])

@users_router.get("/", response={200: list[UserSchema]})
def get_all_users(request: HttpRequest) -> JsonResponse:
    """
    Route to get all users.
    
    Args:
        request (HttpRequest): Request to get all users.

    Returns:
        JsonResponse: Response with all users if they have been found.
    """
    return UsersController.get_all()

@users_router.get("/{user_id}", response={200: UserSchema, 404: dict})
def get_user_by_id(request: HttpRequest, user_id: int) -> JsonResponse:
    """
    Route to get an user by ID.

    Args:
        request (HttpRequest): Request to get an user by ID.
        user_id (int): ID of the user to get.

    Returns:
        JsonResponse: Response with the user if it has been found.
    """
    return UsersController.get_by_id(user_id)

@users_router.get("/login/{user_login}", response={200: UserSchema, 404: dict})
def get_user_by_login(request: HttpRequest, user_login: str) -> JsonResponse:
    """
    Route to get an user by login.

    Args:
        request (HttpRequest): Request to get an user by login.
        user_login (str): Login of the user to get.

    Returns:
        JsonResponse: Response with the user if it has been found.
    """
    return UsersController.get_by_login(user_login)

@users_router.get("/cpf/{user_cpf}", response={200: UserSchema, 404: dict})
def get_user_by_cpf(request: HttpRequest, user_cpf: str) -> JsonResponse:
    """
    Route to get an user by CPF.

    Args:
        request (HttpRequest): Request to get an user by CPF.
        user_cpf (str): CPF of the user to get.

    Returns:
        JsonResponse: Response with the user if it has been found.
    """
    return UsersController.get_by_cpf(user_cpf)

@users_router.post("/", response={201: UserSchema, 400: dict})
def post_user(request: HttpRequest, data: CreateUserSchema) -> JsonResponse:
    """
    Route to create an user.

    Args:
        request (HttpRequest): Request to create an user.
        data (CreateUserSchema): Data with the user to create.

    Returns:
        JsonResponse: Response with the status of the creation.
    """
    return UsersController.create(data)

@users_router.put("/{user_id}", response={200: UserSchema, 404: dict, 400: dict})
def patch_user(request: HttpRequest, user_id: int, data: CreateUserSchema) -> JsonResponse:
    """
    Route to update an existing user by ID.

    Args:
        request (HttpRequest): Request to update an existing user.
        user_id (int): ID of the user to update.
        data (CreateUserSchema): Data to update the user.

    Returns:
        JsonResponse: Response with the status of the update.
    """
    return UsersController.patch(user_id, data)

@users_router.delete("/{user_id}", response={200: dict, 404: dict})
def delete_user(request: HttpRequest, user_id: int) -> JsonResponse:
    """
    Route to delete an user by ID.

    Args:
        request (HttpRequest): Request to delete an user by ID.
        user_id (int): ID of the user to delete.

    Returns:
        JsonResponse: Response with the status of the deletion.
    """
    return UsersController.delete(user_id)