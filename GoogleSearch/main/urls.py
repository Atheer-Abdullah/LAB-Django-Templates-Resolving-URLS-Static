from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("terms/", views.terms_view, name="terms"),
    path("ar/", views.home_ar_view, name="home_ar"),
    path("ar/terms/", views.terms_ar_view, name="terms_ar"),
]