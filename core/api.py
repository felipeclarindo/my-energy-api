from ninja import NinjaAPI
from users.api import users_router

api = NinjaAPI()

@api.get("/")
def Details(request):
   return {
            "name": "Users Manager API",
            "endpoints": {
               "api/docs": "API documentation",
                "api/users": {
                    "GET": "List all users",
                    "POST": "Create a new user",
                },
                "api/users/{user_id}": {
                    "GET": "Get user by id",
                    "DELETE": "Delete user by id",
                    "UPDATE": "Update user by id",
            },
            "libraries": ["django", "django-ninja"],
            "developer": "felipeclarindo",
            "github": "https://github.com/felipeclarindo",
        }
   }

api.add_router('users', users_router)