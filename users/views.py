from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Отправка приветственного письма
            send_mail(
                'Добро пожаловать на наш сайт!',
                'Спасибо за регистрацию.',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )

            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})
