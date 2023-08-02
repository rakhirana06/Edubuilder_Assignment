from django.urls import path
from .views import (
    TenderListView,
    TenderDetailView,
    TenderCreateView,
    TenderUpdateView,
    TenderDeleteView,
    TenderPDFView,
)

urlpatterns = [
    path("", TenderListView.as_view(), name="tender_list"),
    path("<uuid:pk>/", TenderDetailView.as_view(), name="tender_detail"),
    path("new-tender/", TenderCreateView.as_view(), name="tender_create"),
    path("update-tender/<uuid:pk>/", TenderUpdateView.as_view(), name="tender_update"),
    path("delete-tender/<uuid:pk>/", TenderDeleteView.as_view(), name="tender_delete"),
    path("pdf/<uuid:pk>/", TenderPDFView.as_view(), name="tender_pdf"),
]
