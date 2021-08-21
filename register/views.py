from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST': #if the form has been submitted
        form = RegisterForm(request.POST) #form bound with post data
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f' {first_name}!')
            email = form.cleaned_data.get('email')
            
            send_mail(
                'Welcome to dtblogsite',
                f"Hey {first_name}! \n \n Your dtblgosite account is succesfully created. welcome to the dtblogsite from now log into your account using your username and password.\n\n dtblogsite, your number one source for all things about programming. We're dedicated to providing you the best of knowledge, with a focus on dependability. customer service\n \n Regards.", # message
                'dinindulinux.use@gmail.com', # from email
                [email],
                fail_silently=False, # To Email
			    )

            form = authenticate(username=form.cleaned_data['username'],
                        password=form.cleaned_data['password1'],
                        )
            login(request, form)
            return redirect('/')

    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

