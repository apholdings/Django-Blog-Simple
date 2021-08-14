from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings

from .views import HomeView, AboutView, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)