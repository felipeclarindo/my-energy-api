from django.http import JsonResponse
from .models import Users

class UsersController:
    def __init__(self) -> None:
        pass
    
    def get_all() -> JsonResponse:
        return JsonResponse({"message": "Get all users"}, status=200)
    
    def get_by_id(id: int) -> JsonResponse:
        return JsonResponse({"message": f"Get user by id: {id}"}, status=200)
    
    def create() -> JsonResponse:
        return JsonResponse({"message": "Create user"}, status=201)
    
    def patch(id: int) -> JsonResponse:
        return JsonResponse({"message": f"Patch user by id: {id}"}, status=200)
    
    def delete(id: int) -> JsonResponse:
        return JsonResponse({"message": f"Delete user by id: {id}"}, status=200)