from ninja import Router
from .models import Users
from pydantic import BaseModel

class UsersNotFound(Exception):
    pass

class ParamNotFound(Exception):
    pass

class UserAlreadyExists(Exception):
    pass

class PostModel(BaseModel):
    login: str
    password: str

users_router = Router()

@users_router.get("/{user_id}")
def get_user(request, user_id: int):
    try:
        content = Users.objects.get(id=user_id)
        return {"status": "success", "content": content}, 200
    except Users.DoesNotExist:
        return {"status": "error", "content": "User not found"}, 404
    except Exception as e:
        return {"status": "error", "content": e}, 500

@users_router.get("/")
def get_users(request):
    try:
        content = Users.objects.all()
        print(content)
        if not content:
            raise UsersNotFound("No users found")
        return {"status": "success", "content": content}, 200
    except UsersNotFound as e:
        return {"status": "error", "content": e}, 404
    except Exception as e:
        return {"status": "error", "content": e}, 500
    
@users_router.post("/")
def post_user(request, data: PostModel):
    try:
        if not data:
            raise ParamNotFound("No data found")
        Users.objects.create(**data.dict())
        Users.save()
        return {"status": "success", "message": "Succesfull to create a new user"}, 200
    except ParamNotFound as e:
        return {"status": "error", "content": e}, 404
    except Exception as e:
        return {"status": "error", "content": e}, 500
