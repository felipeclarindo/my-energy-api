from ninja import Router
from .models import Users
from .schemas import UserSchema, CreateUserSchema
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

users_router = Router(tags=["Users"])

# Recuperar todos os usuários
@users_router.get("/", response={200: list[UserSchema]})
def get_all_users(request):
    users = Users.objects.all()
    if users:
        # Convertendo os objetos User em um dicionário
        users_data = [{"id": user.id, "login": user.login, "email": user.email, "cpf": user.cpf} for user in users]
        return JsonResponse(users_data, status=200, safe=False)
    return JsonResponse({"message": "No users found"}, status=404)


# Recuperar um usuário por ID
@users_router.get("/{user_id}", response={200: UserSchema, 404: dict})
def get_user_by_id(request, user_id: int):
    user = get_object_or_404(Users, id=user_id)
    user_data = {"id": user.id, "login": user.login, "email": user.email, "cpf": user.cpf}
    return JsonResponse(user_data, status=200)


# Recuperar um usuário pelo login
@users_router.get("/login/{user_login}", response={200: UserSchema, 404: dict})
def get_user_by_login(request, user_login: str):
    try: 
        user = get_object_or_404(Users, login=user_login)
        user_data = {"id": user.id, "login": user.login, "email": user.email, "cpf": user.cpf}
        return JsonResponse(user_data, status=200)
    except Users.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)


# Recuperar um usuário pelo CPF
@users_router.get("/cpf/{cpf}", response={200: UserSchema, 404: dict})
def get_user_by_cpf(request, cpf: str):
    user = Users.objects.filter(cpf=cpf).first()
    if user:
        user_data = {"id": user.id, "login": user.login, "email": user.email, "cpf": user.cpf}
        return JsonResponse(user_data, status=200)
    return JsonResponse({"message": "User not found"}, status=404)


# Criar um novo usuário
@users_router.post("/", response={201: UserSchema, 400: dict})
def post_user(request, data: CreateUserSchema):
    try:
        # Verificação de duplicidade
        if Users.objects.filter(login=data.login).exists():
            return JsonResponse({"message": "Login already in use"}, status=400)
        if Users.objects.filter(cpf=data.cpf).exists():
            return JsonResponse({"message": "CPF already in use"}, status=400)
        if Users.objects.filter(email=data.email).exists():
            return JsonResponse({"message": "Email already in use"}, status=400)
        
        # Hash da senha
        hashed_password = make_password(data.senha)

        # Criação do novo usuário
        user = Users.objects.create(
            login=data.login,
            senha=hashed_password,  
            email=data.email,
            cpf=data.cpf
        )

        # Convertendo o usuário criado em um dicionário
        user_data = {"id": user.id, "login": user.login, "email": user.email, "cpf": user.cpf}
        return JsonResponse(user_data, status=201)

    except Exception as e:
        return JsonResponse({"message": f"Error creating user: {str(e)}"}, status=400)


# Atualizar um usuário
@users_router.put("/{user_id}", response={200: UserSchema, 404: dict, 400: dict})
def put_user(request, user_id: int, data: CreateUserSchema):
    user = get_object_or_404(Users, id=user_id)
    try:
        # Atualizando o usuário com os dados enviados
        for attr, value in data.dict().items():
            setattr(user, attr, value)
        
        user.save()
        user_data = {"id": user.id, "login": user.login, "email": user.email, "cpf": user.cpf}
        return JsonResponse(user_data, status=200)

    except Exception as e:
        return JsonResponse({"message": f"Error updating user: {str(e)}"}, status=400)


# Deletar um usuário
@users_router.delete("/{user_id}", response={200: dict, 404: dict})
def delete_user(request, user_id: int):
    user = get_object_or_404(Users, id=user_id)
    if user:
        user.delete()
        return JsonResponse({"message": "User deleted successfully"}, status=200)
    return JsonResponse({"message": "User not found"}, status=404)
