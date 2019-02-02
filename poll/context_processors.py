from .forms import AnonUserParamsForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from users.models import Profile

from django.contrib.auth.forms import AuthenticationForm 

def user_data(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user.pk)
        return {'finished_polls': [str(p.pk) for p in profile.finished_polls.all()]}
    else:
        anon_user_data = request.session.get('anon_user_data', {})
        if not anon_user_data:
            request.session['anon_user_data'] = {}
            request.session['anon_user_data']['finished_polls'] = []
    
        
        request.session['anon_user_data']['num_visits'] = anon_user_data.get('num_visits', 0) + 1
        request.session.modified = True
    #print('anon user data', anon_user_data)

    return request.session.get('anon_user_data', {})

# кастомизация стандартной формы
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        
        self.base_fields['username'].widget.attrs['class'] = 'form-control'
        self.base_fields['username'].widget.attrs['placeholder'] = 'Логин'
        
        self.base_fields['password'].widget.attrs['class'] = 'form-control'
        self.base_fields['password'].widget.attrs['placeholder'] = 'Пароль'


def include_login_form(request):
    form = CustomAuthenticationForm() 
    return {'login_form': form} 
    
