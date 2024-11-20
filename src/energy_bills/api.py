from ninja import Router
from .models import EnergyBills
from .schemas import CreateEnergyBillsSchema, EnergyBillsSchema
from django.http import JsonResponse

energy_bills_router = Router(tags=["Energy Bills"])

# GET: Retrieve all energy bills
@energy_bills_router.get("/", response={200: list[dict]})
def get_all_energy_bills(request):
    energy_bills = EnergyBills.objects.all().values()  
    return JsonResponse(list(energy_bills), safe=False, status=200)

# GET: Retrieve a single energy bill by ID
@energy_bills_router.get("/{energy_bill_id}", response={200: dict, 404: dict})
def get_energy_bill_by_id(request, energy_bill_id: int):
    energy_bill = EnergyBills.objects.filter(id=energy_bill_id).values().first()  # Get a single energy bill
    if energy_bill:
        return JsonResponse(energy_bill, status=200)
    return JsonResponse({"message": "Energy bill not found"}, status=404)

# GET: Retrieve energy bills by CPF
@energy_bills_router.get("/cpf/{cpf}", response={200: list[dict], 404: dict})
def get_energy_bill_by_cpf(request, cpf: str):
    energy_bills = EnergyBills.objects.filter(cpf=cpf).values()  # Get energy bills by CPF
    if energy_bills.exists():
        return JsonResponse(list(energy_bills), safe=False, status=200)
    return JsonResponse({"message": "No energy bills found for this CPF"}, status=404)

# POST: Create a new energy bill
@energy_bills_router.post("/", response={201: dict, 400: dict})
def post_energy_bill(request, data: CreateEnergyBillsSchema):
    try:
        energy_bill = EnergyBills.objects.create(**data.dict())
        energy_bill.save()
        return JsonResponse({"message": "Energy Bill created successfully"}, status=201)
    except Exception as e:
        return JsonResponse({"message": f"Error creating energy bill: {str(e)}"}, status=400)

# PUT: Update an existing energy bill by ID
@energy_bills_router.put("/{energy_bill_id}", response={200: dict, 404: dict, 400: dict})
def put_energy_bill(request, energy_bill_id: int, data: EnergyBillsSchema):
    energy_bill = EnergyBills.objects.filter(id=energy_bill_id).first()
    if energy_bill:
        try:
            for attr, value in data.dict().items():
                setattr(energy_bill, attr, value)
            energy_bill.save()
            return JsonResponse({"message": "Energy Bill updated successfully", "data": data.dict()}, status=200)
        except Exception as e:
            return JsonResponse({"message": f"Error updating energy bill: {str(e)}"}, status=400)
    return JsonResponse({"message": "Energy bill not found"}, status=404)

# DELETE: Delete an energy bill by ID
@energy_bills_router.delete("/{energy_bill_id}", response={200: dict, 404: dict})
def delete_energy_bill(request, energy_bill_id: int):
    energy_bill = EnergyBills.objects.filter(id=energy_bill_id).first()
    if energy_bill:
        energy_bill.delete()
        return JsonResponse({"message": "Energy Bill deleted successfully"}, status=200)
    return JsonResponse({"message": "Energy bill not found"}, status=404)

# GET: Retrieve summary of energy bills by ID
@energy_bills_router.get("/summary/{energy_bill_id}", response={200: dict})
def summary(request, energy_bill_id: int):
    energy_bills = EnergyBills.objects.filter(id=energy_bill_id)
    total_consumption = sum([bill.consumo for bill in energy_bills])
    total_value = sum([bill.valor for bill in energy_bills])
    return JsonResponse({"total_consumption": total_consumption, "total_value": total_value}, status=200)
