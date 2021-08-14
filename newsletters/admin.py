from django.contrib import admin
from .models import NewsletterUser,Newsletter
# Register your models here.

admin.site.register(NewsletterUser)
admin.site.register(Newsletter)
