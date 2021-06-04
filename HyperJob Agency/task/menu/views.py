from django.shortcuts import render
from django.views.generic.base import TemplateView

class MenuView(TemplateView):
    template_name = 'menu/index.html'
