from django.http import JsonResponse

from .models import EnergyBills
from .schemas import EnergyBillsSchema, CreateEnergyBillSchema

class EnergyBillsController:
    @classmethod
    def get_all(cls) -> JsonResponse:
        """
        Get all energy bills in the database.

        Returns: 
            JsonResponse: Response with all energy bills if it has been found.
        """
        energy_bills = EnergyBills.objects.all().values()  
        if energy_bills.exists():
            return JsonResponse(list(energy_bills), safe=False, status=200)
        return JsonResponse({"message": "No energy bills found"}, status=404)
    
    @classmethod
    def get_by_id(cls, energy_bill_id: int) -> JsonResponse:
        """
        Get energy bill by ID.

        Args:
            energy_bill_id (int): id from the energy bill.

        Returns:
            JsonResponse: Response with energy bill if it has been found.
        """
        energy_bill = EnergyBills.objects.filter(id=energy_bill_id).values()
        if energy_bill.exists():
            return JsonResponse(energy_bill, status=200)
        return JsonResponse({"message": "Energy bill not found"}, status=404)
    
    @classmethod 
    def get_by_cpf(cls, energy_bill_cpf: str) -> JsonResponse:
        """
        Get energy bill by CPF.

        Args:
            energy_bill_cpf (str): CPF from the energy bill.

        Returns:
            JsonResponse: Response with energy bill if it has been found.
        """
        energy_bills = EnergyBills.objects.filter(cpf=energy_bill_cpf).values()
        if energy_bills.exists():
            return JsonResponse(list(energy_bills), safe=False, status=200)
        return JsonResponse({"message": "No energy bills found for this CPF"}, status=404)

    @classmethod
    def create(cls, data: CreateEnergyBillSchema) -> JsonResponse:
        """
        Create an energy bill in the database.

        Args:
            data (CreateEnergyBillSchema): Data to create an energy bill.
            
        Returns:
            JsonResponse: Response with the creation status.
        """
        try:
            energy_bill = EnergyBills.objects.create(**data.dict())
            energy_bill.save()
            return JsonResponse({"message": "Energy Bill created successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"message": f"Error creating energy bill: {str(e)}"}, status=400)

    # Update energy bill by ID
    @classmethod
    def patch(cls, energy_bill_id: int, data: EnergyBillsSchema) -> JsonResponse:
        """
        Patch an existing energy bill by ID.

        Args:
            energy_bill_id (int): ID of the energy bill to update.
            data (EnergyBillsSchema): Data to update the energy bill.

        Returns:
            JsonResponse: Response with the updating status.
        """
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
    
    @classmethod
    def delete(cls, energy_bill_id: int) -> JsonResponse:
        """
        Delete an existing energy bill by ID.

        Args:
            energy_bill_id (int): ID of the energy bill to delete.

        Returns:
            JsonResponse: Response with the deletion status.
        """
        energy_bill = EnergyBills.objects.filter(id=energy_bill_id).first()
        if energy_bill:
            energy_bill.delete()
            return JsonResponse({"message": "Energy Bill deleted successfully"}, status=200)
        return JsonResponse({"message": "Energy bill not found"}, status=404)
    
    @classmethod
    def summary(cls, energy_bill_id: int) -> JsonResponse:
        """
        Get summary of energy bill by ID.

        Args:
            energy_bill_id (int): ID of the energy bill to get summary.

        Returns:
            JsonResponse: Response with the summary of the energy bill.
        """
        energy_bills = EnergyBills.objects.filter(id=energy_bill_id)
        total_consumption = sum([bill.consumption for bill in energy_bills])
        total_value = sum([bill.valor for bill in energy_bills])
        return JsonResponse({"total_consumption": total_consumption, "total_value": total_value}, status=200)