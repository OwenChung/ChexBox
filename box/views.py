from django.shortcuts import render, render_to_response
from .forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, FormView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .models import FileModel
from .forms import UploadForm

# Create your views here.

def index(request):
    if request.user.is_authenticated(): #if already logged in
        return HttpResponseRedirect('home') #redirect to the homepage
    return render_to_response('index.html') #otherwise show them the index page 
                        #(gives option to login)

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


class FileListView(ListView):
    model = FileModel
    context_object_name = "files"
    template_name = "home.html"
    paginate_by = 5
    
    def get_queryset(self):
        if self.request.user.is_authenticated():
            queryset = FileModel.objects.all()
            queryset = queryset.filter(user=self.request.user)
            return queryset.values('f').order_by('-id')
        return FileModel.objects.none()

@login_required
def upload_file(request):
    if request.user.is_authenticated() and request.method == 'POST': 
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newUpload = FileModel(f = request.FILES['f'])
            newUpload.user = request.user
            newUpload.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadForm()
    return render(request, 'add-boring.html', {'form': form})
