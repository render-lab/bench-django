from django.http import JsonResponse
from django.db import connection, DatabaseError
from django.urls import path


def health(_request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
    except DatabaseError:
        return JsonResponse({"status": "unavailable"}, status=503)
    return JsonResponse({"status": "ok"})


def root(_request):
    return JsonResponse({"message": "Seed Django app. Add apps, then ship it."})


urlpatterns = [
    path("", root),
    path("health/", health),
]
