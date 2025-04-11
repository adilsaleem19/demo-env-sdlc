from . import views
from django.urls import path

urlpatterns = [
    path('article/', views.create_article)
]
