from django.conf.urls import url, include


urlpatterns = [url(r"^", include("django_zarinpal.urls", namespace="django_zarinpal"))]
