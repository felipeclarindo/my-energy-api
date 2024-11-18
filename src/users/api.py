from ninja import Router
from .models import Users
from .schemas import UserSchema, CreateUserSchema
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

users_router = Router(tags=["Users"])

@users_router.get("/", response={200: list[UserSchema]})
def get_all_users(request):
    users = Users.objects.all()
    if users:
        return users
    return JsonResponse({"message": "No users found"}, status=404)


@users_router.get("/{user_id}", response={200: UserSchema, 404: dict})
def get_user_by_id(request, user_id: int):
    try:
        user = get_object_or_404(Users, id=user_id)
        return user
    except Exception:
        return JsonResponse({"message": "User not found"}, status=404)

@users_router.get("/cpf/{cpf}", response={200: UserSchema, 404: dict})
def get_user_by_cpf(request, cpf: str):
    user = Users.objects.filter(cpf=cpf).first()
    if user:
        return user
    return JsonResponse({"message": "User not found"}, status=404)


@users_router.post("/", response={201: CreateUserSchema, 400: dict})
def post_user(request, data: CreateUserSchema):
    try:
        if Users.objects.filter(login=data.login).exists():
            return JsonResponse({"message": "Login already exists"}, status=400)
        if Users.objects.filter(cpf=data.cpf).exists():
            return JsonResponse({"message": "CPF already exists"}, status=400)
        user = Users.objects.create(
            login=data.login,
            senha=data.senha,  
            email=data.email,
            cpf=data.cpf
        )
        return user, 201
    except Exception as e:
        return JsonResponse({"message": f"Error creating user: {str(e)}"}, status=400)


@users_router.put("/{user_id}", response={200: UserSchema, 404: dict, 400: dict})
def put_user(request, user_id: int, data: CreateUserSchema):
    user = get_object_or_404(Users, id=user_id)
    try:
        
        for attr, value in data.dict().items():
            setattr(user, attr, value)
        
        user.save()
        return user
    except Exception as e:
        return JsonResponse({"message": f"Error updating user: {str(e)}"}, status=400)


@users_router.delete("/{user_id}", response={200: dict, 404: dict})
def delete_user(request, user_id: int):
    user = get_object_or_404(Users, id=user_id)
    user.delete()
    return JsonResponse({"message": "User deleted successfully"}, status=200)
