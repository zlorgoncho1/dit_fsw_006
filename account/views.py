from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', context={'form': form})