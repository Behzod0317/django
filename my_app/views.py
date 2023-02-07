
from django.shortcuts import render
from .models import *
from django.http import HttpResponse ,request
from django.views.generic import ListView,TemplateView

def menu(request):
    menu_items = MenuItem.objects.all()
    return HttpResponse(request, 'menu.html', {'menu_items': menu_items})

class MenuView(TemplateView):
    template_name = 'menu.html'