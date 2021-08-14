from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'index.html', context)

class AboutView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'about.html', context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'contact.html', context)