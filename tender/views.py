from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Tender
from .forms import TenderForm

from django.http import Http404
from main import renders

# Create your views here.

class TenderListView(ListView):
    model = Tender
    context_object_name = "tender_list"
    template_name = "tender/tender_list.html"


class TenderDetailView(DetailView):
    model = Tender
    context_object_name = "tender"
    template_name = "tender/tender_detail.html"


class TenderCreateView(CreateView):
    model = Tender
    fields = "__all__"
    template_name = "tender/tender_create.html"


class TenderUpdateView(UpdateView):
    model = Tender
    fields = "__all__"
    context_object_name = "tender"
    template_name = "tender/tender_update.html"


class TenderDeleteView(DeleteView):
    model = Tender
    context_object_name = "tender"
    template_name = "tender/tender_delete.html"
    success_url = reverse_lazy("tender_list")

class TenderPDFView(DetailView):
    model = Tender
    context_object_name = "tender"
    template_name = "tender/tender_detail.html"

    def get(self, request, *args, **kwargs):
        tender = Tender.objects.get(pk=self.kwargs.get("pk"))
        tender_pdf = renders.render_to_pdf("tender/tender_detail.html", {"tender": tender})
        if tender_pdf.status_code == 404:
            raise Http404("Tender not found")
        filename = f"tender{self.kwargs.get('pk')}.pdf"
        content = f"inline; filename={filename}"
        download = request.GET.get("download")
        if download:
            content = f"attachment; filename={filename}"
        tender_pdf["Content-Disposition"] = content
        return tender_pdf