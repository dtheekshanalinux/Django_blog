from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout



def register(request):
    if request.method == 'POST': #if the form has been submitted
        form = RegisterForm(request.POST) #form bound with post data
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f' {first_name}!')
            form = authenticate(username=form.cleaned_data['username'],
                        password=form.cleaned_data['password1'],
                        )
            login(request, form)
            return redirect('/')

    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

