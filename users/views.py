from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from users.forms import LoginForm
from django.views import View
# Create your views here.


class LoginView(View):

    def get(self, request):
        '''
        Render Login view
        '''
        if request.user.is_authenticated():
            return redirect(request.GET.get('next', 'blogs/'))
        error_message = ''
        login_form = LoginForm()
        context = {
            'error': error_message,
            'form': login_form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        '''
        Render Login view Send information to log
        '''
        error_message = ""
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_message = 'Username or password are wrong'
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next', 'blogs/'))
                else:
                    error_message = 'User with inactive account'
        else:
            error_message = 'Username or password are wrong'

        context = {
            'error': error_message,
            'form': login_form
        }
        return render(request, 'users/login.html', context)


class LogoutView(View):

    def get(self, request):
        '''
        Creacion del logout
        '''
        if request.user.is_authenticated():
            django_logout(request)

        return redirect('/login')
