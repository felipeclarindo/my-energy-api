from ninja import NinjaAPI
from users.api import users_router
from authenticate.api import authenticate_router
from energy_bills.api import energy_bills_router

api = NinjaAPI()
api.add_router('users', users_router)
api.add_router('energy-bills', energy_bills_router)
api.add_router('authenticate', authenticate_router)

@api.get("/")
def index(request):
    return {
    "name": "Api para controle de usuários e contas",
    "description": "Api desenvolvida para uma melhoria na",
    "version": "1.0",
    "endpoints": [
        {
        "route": "/api/energy-bills",
        "methods":[
            "GET",
            "POST",
        ],
        "description": "Endpoint para manipulação de contas de energia."
        },
        {
        "route": "/api/energy-bills/{id}",
        "methods":[
            "GET",
            "PATCH",
            "DELETE"
        ],
        "description": "Endpoint para manipulação de uma unica conta."
        },
        {
        "route": "/api/users",
        "method": [
            "GET",
            "POST"
        ],
        "description": "Endpoint para manipulação de usuarios."
        },
        {
        "route": "/api/users/{id}",
        "method": [
            "GET",
            "PATCH",
            "DELETE"
        ],
        "description": "Manipulação de um usuario especifico."
        }
    ],
    "contact": {
        "github": "https://github.com/felipeclarindo",
        "email": "contato.felipeclarindo@gmail.com",
    },
}