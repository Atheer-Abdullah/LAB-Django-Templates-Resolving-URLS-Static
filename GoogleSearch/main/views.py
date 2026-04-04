from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# ===== Views =====

def home_view(request: HttpRequest):
    return render(request, "main/index.html")


def home_ar_view(request: HttpRequest):
    return render(request, "main/index_ar.html")


def terms_view(request: HttpRequest):
    return render(request, "main/terms.html")

def terms_ar_view(request: HttpRequest):
    return render(request, "main/terms_ar.html")