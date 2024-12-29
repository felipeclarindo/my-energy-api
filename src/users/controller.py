from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from .models import Users
from .schemas import CreateUserSchema

class UsersController:
    @classmethod
    def get_all(cls) -> JsonResponse:
        """
        Get all users from the database.

        Returns:
            JsonResponse: Response with all users data.
        """
        users = Users.objects.all()
        if users:
            users_data = [{"id": user.id, "login": user.login, "email": user.email, "cpf": user.cpf} for user in users]
            return JsonResponse(users_data, status=200, safe=False)
        return JsonResponse({"message": "No users found"}, status=404)
        
    @classmethod
    def get_by_id(cls, user_id: int) -> JsonResponse:
        """
        Get user by ID.

        Args:
            user_id (int): ID of the user to get.

        Returns:
            JsonResponse: Response with the user data if it has been found.
        """
        user = get_object_or_404(Users, id=user_id)
        user_data = {"id": user.id, "login": user.login, "email": user.email, "cpf": user.cpf}
        return JsonResponse(user_data, status=200)
    
    @classmethod
    def get_by_login(cls, user_login: str) -> JsonResponse:
        """
        Get user by login.

        Args:
            user_login (str): Login of the user to get.

        Returns:
            JsonResponse: Response with the user data if it has been found.
        """
        try: 
            user = get_object_or_404(Users, login=user_login)
            user_data = {"id": user.id, "login": user.login, "email": user.email, "cpf": user.cpf}
            return JsonResponse(user_data, status=200)
        except Users.DoesNotExist:
            return JsonResponse({"message": "User not found"}, status=404)
        
    @classmethod 
    def get_by_cpf(cls, user_cpf: str) -> JsonResponse:
        """
        Get user by CPF.

        Args:
            user_cpf (str): CPF of the user to get.

        Returns:
            JsonResponse: Response with the user data if it has been found.
        """
        user = Users.objects.filter(cpf=user_cpf).first()
        if user:
            user_data = {"id": user.id, "login": user.login, "email": user.email, "cpf": user.cpf}
            return JsonResponse(user_data, status=200)
        return JsonResponse({"message": "User not found"}, status=404)

    @classmethod
    def create(cls, data: CreateUserSchema) -> JsonResponse:
        """
        Create a new user in the database.

        Args:
            data (CreateUserSchema): Data to create a new user.

        Returns:
            JsonResponse: Response with the status of the creation.
        """
        try:
            # Validate if login, cpf and email are already in use
            if Users.objects.filter(login=data.login).exists():
                return JsonResponse({"message": "Login already in use"}, status=400)
            if Users.objects.filter(cpf=data.cpf).exists():
                return JsonResponse({"message": "CPF already in use"}, status=400)
            if Users.objects.filter(email=data.email).exists():
                return JsonResponse({"message": "Email already in use"}, status=400)
            
            # Hash the password before saving it
            hashed_password = make_password(data.password)

            user = Users.objects.create(
                login=data.login,
                password=hashed_password,  
                email=data.email,
                cpf=data.cpf
            )

            user_data = {"id": user.id, "login": user.login, "email": user.email, "cpf": user.cpf}
            return JsonResponse(user_data, status=201)

        except Exception as e:
            return JsonResponse({"message": f"Error creating user: {str(e)}"}, status=400)
        

    @classmethod
    def patch(cls, user_id: int, data: CreateUserSchema) -> JsonResponse:
        """
        Update an existing user by ID.

        Args:
            user_id (int): ID of the user to update.
            data (CreateUserSchema): Data to update the user.

        Returns:
            JsonResponse: Response with the status of the update.
        """
        user = get_object_or_404(Users, id=user_id)
        try:
            for attr, value in data.dict(exclude_unset=True).items():
                if value is not None and value:
                    setattr(user, attr, value)
            user.save()
            return JsonResponse({"message": f"Success to update user from id {id}", "data": data.dict()}, status=200)

        except Exception as e:
            return JsonResponse({"message": f"Error updating user: {str(e)}"}, status=400)
        
    @classmethod
    def delete(cls, user_id: int) -> JsonResponse:
        """
        Delete an existing user by ID.

        Args:
            user_id (int): ID of the user to delete.

        Returns:
            JsonResponse: Response with the status of the deletion.
        """
        user = get_object_or_404(Users, id=user_id)
        if user:
            user.delete()
            return JsonResponse({"message": "User deleted successfully"}, status=200)
        return JsonResponse({"message": "User not found"}, status=404)
    
