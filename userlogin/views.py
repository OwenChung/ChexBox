from django.shortcuts import render, render_to_response
from userlogin.forms import UserCreationForm
from django.http import HttpResponseRedirect

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('complete')

    else:
        form = UserCreationForm()

    c = {'form': form}
    return render(request,'registration/registration_form.html',
                          {'form':form})

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')
