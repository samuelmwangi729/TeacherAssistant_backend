from django.urls import path
from Excel.views import ExcelFile
urlpatterns = [
    path('excel',ExcelFile.as_view(),name="excel")
]
