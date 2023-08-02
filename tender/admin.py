from django.contrib import admin
from .models import Tender

# Register your models here.
class TenderAdmin(admin.ModelAdmin):
    list_display = ("title", "proposal_date",)

admin.site.register(Tender, TenderAdmin)
