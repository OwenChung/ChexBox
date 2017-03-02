from django.shortcuts import render
from userlogin.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.Post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('accounts/register/complete')

    else:
        form = UserCreationForm()

    c = {'form': form}
    return render(request,'registration/registration_form.html',
                          {'form':form})

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')
