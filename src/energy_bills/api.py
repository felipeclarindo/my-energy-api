from ninja import Router
from .schemas import CreateEnergyBillSchema, EnergyBillsSchema
from .controller import EnergyBillsController
from django.http import HttpRequest, JsonResponse

energy_bills_router = Router(tags=["Energy Bills"])

@energy_bills_router.get("/", response={200: list[dict]})
def get_all_energy_bills(request: HttpRequest) -> JsonResponse:
    """
    Route to get all energy bills.

    Args:
        request (HttpRequest): Request to get all energy bills.

    Returns:
        JsonResponse: Returns a JSON response with all energy bills if it has been found.
    """
    return EnergyBillsController.get_all()

@energy_bills_router.get("/{energy_bill_id}", response={200: dict, 404: dict})
def get_energy_bill_by_id(request: HttpRequest, energy_bill_id: int) -> JsonResponse:
    """
    Route to get an energy bill by ID.

    Args:
        request (HttpRequest): Request to get an energy bill by ID.
        energy_bill_id (int): ID of the energy bill to get.

    Returns:
        JsonResponse: Return a JSON response with the energy bill if it has been found
    """
    return EnergyBillsController.get_by_id(energy_bill_id)
    
@energy_bills_router.get("/cpf/{cpf}", response={200: list[dict], 404: dict})
def get_energy_bill_by_cpf(request: HttpRequest, cpf: str) -> JsonResponse:
    """
    Route to get energy bill by CPF.

    Args:
        request (HttpRequest): Request to get energy bill by CPF.
        cpf (str): CPF of the energy bill to get.

    Returns:
        JsonResponse: Return a JSON response with the energy bill if it has been found.
    """
    return EnergyBillsController.get_by_cpf(cpf)

@energy_bills_router.post("/", response={201: dict, 400: dict})
def post_energy_bill(request: HttpRequest, data: CreateEnergyBillSchema) -> JsonResponse:
    """
    Route to create an energy bill.

    Args:
        request (HttpRequest): Request to create an energy bill.
        data (CreateEnergyBillSchema): Data to create an energy bill.

    Returns:
        JsonResponse: Return a JSON response with status of the creation.
    """
    return EnergyBillsController.create(data)
    
@energy_bills_router.put("/{energy_bill_id}", response={200: dict, 404: dict, 400: dict})
def patch_energy_bill(request: HttpRequest, energy_bill_id: int, data: EnergyBillsSchema) -> JsonResponse:
    """
    Route to update an existing energy bill by ID.

    Args:
        request (HttpRequest): Request to update an existing energy bill.
        energy_bill_id (int): ID of the energy bill to update.
        data (EnergyBillsSchema): Data to update the energy bill.

    Returns:
        JsonResponse: Response with the status of the update.
    """
    return EnergyBillsController.patch(energy_bill_id, data)

@energy_bills_router.delete("/{energy_bill_id}", response={200: dict, 404: dict})
def delete_energy_bill(request: HttpRequest, energy_bill_id: int) -> JsonResponse:
    """
    Route to delete an energy bill by ID.

    Args:
        request (HttpRequest): Request to delete an energy bill.
        energy_bill_id (int): ID of the energy bill to delete.
    Returns:
        JsonResponse: Response with the status of the deletion.
    """
    return EnergyBillsController.delete(energy_bill_id)

@energy_bills_router.get("/summary/", response={200: dict, 404: dict})
def summary(request: HttpRequest) -> JsonResponse:
    """
    Route to get summary of energy bills.

    Args:
        request (HttpRequest): Request to get summary of energy bill.

    Returns:
        JsonResponse: Response with the summary of the energy bill.
    """
    return EnergyBillsController.summary()
