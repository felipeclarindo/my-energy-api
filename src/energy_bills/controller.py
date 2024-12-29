from django.db.models import Sum
from django.http import JsonResponse
from django.db.models.functions import TruncMonth
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
                for attr, value in data.dict(exclude_unset=True).items():
                    if value is not None and value:
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
    def summary(cls) -> JsonResponse:
        """
        Get summary of energy bills.

        Returns:
            JsonResponse: Response with the total consumption and total value of the energy bills.
        """ 
        
        energy_bills = EnergyBills.objects.all()

        if not energy_bills.exists():
            return JsonResponse({"message": "No energy bills found."}, status=404)

        total_consumption = energy_bills.aggregate(total_consumption=Sum('consumption'))['total_consumption']
        total_value = energy_bills.aggregate(total_value=Sum('value'))['total_value']

        monthly_summary = (
            energy_bills
            .annotate(month=TruncMonth('data')) 
            .values('month')
            .annotate(monthly_consumption=Sum('consumption'), monthly_value=Sum('value'))
            .order_by('month')
        )

        monthly_summary_list = [
            {
                "month": entry['month'].strftime("%Y-%m"),
                "consumption": entry['monthly_consumption'],
                "value": entry['monthly_value']
            }
            for entry in monthly_summary
        ]

        return JsonResponse({
            "total_consumption": total_consumption,
            "total_value": total_value,
            "monthly_summary": monthly_summary_list
        }, status=200)