# dashboard/views.py
from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm

def dashboard(request):
    users = User.objects.all()
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request, 'dashboard.html', {'users': users, 'form': form})