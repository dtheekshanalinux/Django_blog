from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout



def register(request):
    if request.method == 'POST': #if the form has been submitted
        form = RegisterForm(request.POST) #form bound with post data
        if form.is_valid():
            form.save()
            First_name = form.cleaned_data.get('First_name')
            messages.success(request, f' {First_name}!')
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

