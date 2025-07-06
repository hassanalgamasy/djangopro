from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.
def register_view(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,'Doneeeeeeeeee')
            return redirect('login')
        else:
            messages.error(request, "threr is a wrong in your data")
    else:
        form= CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})