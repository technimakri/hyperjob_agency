from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from vacancy.models import Vacancy
from django.http import HttpResponseForbidden

class VacancyView(TemplateView):
    template_name = 'vacancy/vacancy_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancy_list'] = Vacancy.objects.all()
        return context

class NewVacancy(View):

    def get(self, request, *args, **kwargs):
        return render(request, template_name='vacancy/new_vacancy.html')

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()

        else:
            Vacancy.objects.create(author=request.user, description=request.POST.get('description'))
            return redirect('home')
