from django import forms
from .models import Tender


class TenderForm(forms.ModelForm):
    class Meta:
        model = Tender
        fields = [
            "title",
            "proposal_description",
            "proposal_date",
            "contractor_company_name",
            "contractor_name",
            "contractor_email",
            "contractor_phone",
            "client_company_name",
            "client_name",
            "client_email",
            "client_phone",
            "finance_amount",
            "finance_currency",
            "planning_phase1_date",
            "planning_phase1_payment",
            "planning_phase2_date",
            "planning_phase2_payment",
            "planning_final_date",
            "planning_final_payment",
            "terms_and_conditions",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "proposal_description": forms.Textarea(attrs={"class": "form-control"}),
            "proposal_date": forms.DateInput(attrs={"class": "form-control"}),
            "contractor_company_name": forms.TextInput(attrs={"class": "form-control"}),
            "contractor_name": forms.TextInput(attrs={"class": "form-control"}),
            "contractor_email": forms.EmailInput(attrs={"class": "form-control"}),
            "contractor_phone": forms.TextInput(attrs={"class": "form-control"}),
            "client_company_name": forms.TextInput(attrs={"class": "form-control"}),
            "client_name": forms.TextInput(attrs={"class": "form-control"}),
            "client_email": forms.EmailInput(attrs={"class": "form-control"}),
            "client_phone": forms.TextInput(attrs={"class": "form-control"}),
            "finance_amount": forms.NumberInput(attrs={"class": "form-control"}),
            "finance_currency": forms.TextInput(attrs={"class": "form-control"}),
            "planning_phase1_date": forms.DateInput(attrs={"class": "form-control"}),
            "planning_phase1_payment": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "planning_phase2_date": forms.DateInput(attrs={"class": "form-control"}),
            "planning_phase2_payment": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "planning_final_date": forms.DateInput(attrs={"class": "form-control"}),
            "planning_final_payment": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "terms_and_conditions": forms.Textarea(attrs={"class": "form-control"}),
        }
