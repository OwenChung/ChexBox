from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
#from django.core.context_processors import csrf
#from django.template import RequestContext

class HomeView(TemplateView):

    template_name = 'index.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()
    
    c = {'form': form}
    return render(request,'registration/registration_form.html',
                          {'form':form})

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')
