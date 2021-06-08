from django.shortcuts import render
from django.views.generic.base import TemplateView
from resume.models import Resume


class ResumeView(TemplateView):
    template_name = 'resume/resume_list.html'
    resume_list = Resume.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_list'] = self.resume_list
        return context




