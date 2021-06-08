from django.shortcuts import render
from django.views.generic.base import TemplateView
from vacancy.models import Vacancy


class VacancyView(TemplateView):
    template_name = 'vacancy/vacancy_list.html'
    vacancy_list = Vacancy.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancy_list'] = self.vacancy_list
        return context
