from django.urls import path
from .views import (
    DashboardHomeView,
    NewslettersDashboardHomeView, 
    NewsletterCreateView, 
    NewsletterDetailView, 
    NewsletterUpdateView,
    NewsletterDeleteView
    )

app_name="dashboard"

urlpatterns = [
    path('',DashboardHomeView.as_view(),name="home"),
    path('list/',NewslettersDashboardHomeView.as_view(),name="list"),
    path('create/',NewsletterCreateView.as_view(),name="create"),
    path('detail/<int:pk>',NewsletterDetailView.as_view(),name="detail"),
    path('update/<int:pk>',NewsletterUpdateView.as_view(),name="update"),
    path('delete/<int:pk>',NewsletterDeleteView.as_view(),name="delete"),
]
