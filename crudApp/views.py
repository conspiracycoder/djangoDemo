from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, UpdateRecordForm
from .models import CustomUser
def home(request):
    records = CustomUser.objects.all()
    # Check to see if logging in
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in!!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials. Please try again.')
            return redirect('home')
    else:
        records = CustomUser.objects.exclude(id=request.user.id)
        return render(request, 'home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out!!')
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)
            login(request, user)
            messages.success(request, 'You are now registered!! Welcome.')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})

def user_record(request, pk):
    if request.user.is_authenticated:
        users_record = CustomUser.objects.get(id=pk)
        return render(request, 'records.html', {'user_record': users_record})
    else:
        messages.success(request, 'You are not logged in!!')
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete = CustomUser.objects.get(id=pk)
        delete.delete()
        messages.success(request, 'The record has been deleted!!')
        return redirect('home')
    else:
        messages.success(request, 'You are not logged in!!')
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        update = CustomUser.objects.get(id=pk)
        form = UpdateRecordForm(request.POST or None, instance=update)
        if form.is_valid():
            form.save()
            messages.success(request, 'The record has been updated!!')
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, 'You are not logged in!!')
        return redirect('home')