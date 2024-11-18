from ninja import Router
from .models import EnergyBills
from .schemas import CreateEnergyBillSchema, EnergyBillSchema
from django.shortcuts import get_object_or_404

energy_bills_router = Router(tags=["Energy Bills"])

@energy_bills_router.get("/", response={200: list[EnergyBillSchema]})
def get_all_energy_bills(request):
    energy_bills = EnergyBills.objects.all()
    return list(energy_bills)

@energy_bills_router.get("/{energy_bill_id}", response={200: EnergyBillSchema, 404: dict})
def get_energy_bill_by_id(request, energy_bill_id: int):
    energy_bill = get_object_or_404(EnergyBills, id=energy_bill_id)
    return energy_bill

@energy_bills_router.get("/cpf/{cpf}", response={200: list[EnergyBillSchema], 404: dict})
def get_energy_bill_by_cpf(request, cpf: str):
    energy_bills = EnergyBills.objects.filter(cpf__cpf=cpf)
    if energy_bills.exists():
        return list(energy_bills)
    return {"message": "No energy bills found for this CPF"}, 404

@energy_bills_router.post("/", response={201: EnergyBillSchema, 400: dict})
def post_energy_bill(request, data: CreateEnergyBillSchema):
    try:
        energy_bill = EnergyBills.objects.create(**data.dict())
        return energy_bill
    except Exception as e:
        return {"message": f"Error creating energy bill: {str(e)}"}, 400

@energy_bills_router.put("/{energy_bill_id}", response={200: EnergyBillSchema, 404: dict, 400: dict})
def put_energy_bill(request, energy_bill_id: int, data: CreateEnergyBillSchema):
    energy_bill = get_object_or_404(EnergyBills, id=energy_bill_id)
    try:
        for attr, value in data.dict().items():
            setattr(energy_bill, attr, value)
        energy_bill.save()
        return energy_bill
    except Exception as e:
        return {"message": f"Error updating energy bill: {str(e)}"}, 400

@energy_bills_router.delete("/{energy_bill_id}", response={200: dict, 404: dict})
def delete_energy_bill(request, energy_bill_id: int):
    energy_bill = get_object_or_404(EnergyBills, id=energy_bill_id)
    energy_bill.delete()
    return {"message": "Energy Bill deleted successfully"}, 200
