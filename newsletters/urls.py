from django.urls import path
from .views import newsletter_signup, newsletter_unsubscribe

app_name="newsletters"

urlpatterns = [
    path('entrenamiento/', newsletter_signup, name="optin"),
    path('unsubscribe/', newsletter_unsubscribe, name="unsubscribe"),
]
