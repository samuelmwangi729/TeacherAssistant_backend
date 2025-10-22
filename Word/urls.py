from django.urls import path 
from Word.views import WordView
urlpatterns = [
    path('word',WordView.as_view(),name="word")
]
