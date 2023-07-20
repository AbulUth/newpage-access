# users/views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with the name of your success URL
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})
