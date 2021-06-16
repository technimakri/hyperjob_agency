from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from resume.models import Resume
from django.views import View
from django.http import HttpResponseForbidden


class ResumeView(TemplateView):
    template_name = 'resume/resume_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_list'] = Resume.objects.all()
        return context


class NewResume(View):

    def get(self, request, *args, **kwargs):
        return render(request, template_name='resume/new_resume.html')

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated or request.user.is_staff:
            return HttpResponseForbidden()

        else:
            Resume.objects.create(author=request.user, description=request.POST.get('description'))
            return redirect('/home')
