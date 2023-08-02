from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
import uuid

# Create your models here.
class Tender(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=150)
    proposal_description = models.TextField(max_length=1000)
    proposal_date = models.DateField()

    contractor_company_name = models.CharField(max_length=200)
    contractor_name = models.CharField(max_length=150)
    contractor_email = models.EmailField(max_length=200)
    contractor_phone = PhoneNumberField(region="IN", max_length=13)

    client_company_name = models.CharField(max_length=200)
    client_name = models.CharField(max_length=150)
    client_email = models.EmailField(max_length=200)
    client_phone = PhoneNumberField(region="IN", max_length=13)

    finance_amount = models.DecimalField(max_digits=9, decimal_places=2)
    finance_currency = models.CharField(max_length=15)
    
    planning_phase1_date = models.DateField()
    planning_phase1_payment = models.IntegerField()
    planning_phase2_date = models.DateField()
    planning_phase2_payment = models.IntegerField()
    planning_final_date = models.DateField()
    planning_final_payment = models.IntegerField()
    
    terms_and_conditions = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tender_detail", args=[str(self.id)])