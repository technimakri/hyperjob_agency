from django.shortcuts import render, redirect
from django.views import View


class ProfileView(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login')

        context_dict = {}

        if request.user.is_staff:
            context_dict['link'] = 'vacancy/new'
        else:
            context_dict['link'] = 'resume/new'

        return render(request, 'profiles/profile.html', context=context_dict)

