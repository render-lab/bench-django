from django.http import JsonResponse
from django.urls import path


def health(_request):
    return JsonResponse({"status": "ok"})


def root(_request):
    return JsonResponse({"message": "Seed Django app. Add apps, then ship it."})


urlpatterns = [
    path("", root),
    path("health/", health),
]
