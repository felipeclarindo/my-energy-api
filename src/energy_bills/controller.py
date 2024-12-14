from django.http import JsonResponse

from .models import EnergyBills

class EnergyBillsController:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def get_all() -> JsonResponse:
        return JsonResponse({"message": "Get all energy bills"}, status=200)
    
    def get_by_id(id: int) -> JsonResponse:
        return JsonResponse({"message": f"Get energy bill by id: {id}"}, status=200)
    
    def create() -> JsonResponse:
        return JsonResponse({"message": "Create energy bill"}, status=201)
    
    def patch(id: int) -> JsonResponse:
        return JsonResponse({"message": f"Patch energy bill by id: {id}"}, status=200)
    
    def delete(id: int) -> JsonResponse:
        return JsonResponse({"message": f"Delete energy bill by id: {id}"}, status=200)
    