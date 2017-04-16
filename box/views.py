from django.shortcuts import render, render_to_response, redirect
from .forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.views.generic import ListView, FormView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .models import FileModel
from .forms import UploadForm, ShareForm

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

    def get_context_data(self, **kwargs):
        context = super(FileListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            #print(self.request.user.username)
            files = FileModel.objects.filter(user=self.request.user) | FileModel.objects.filter(shared_with__contains=[self.request.user.username])
        else:
            files = FileModel.objects.none()
        context['file_list'] = files
        #print(FileModel.objects.all().values('f'))
        context['favorites_list'] = files.filter(isfavorite = True)
        return context    
    
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

@login_required(login_url='/login/')
def delete_file(request, pk):
    indiv_file = FileModel.objects.get(id = pk)
    indiv_file.delete()
    return redirect(reverse('box:home'))

@login_required(login_url='/login/')
def favorite_file(request, pk):
    indiv_file = FileModel.objects.get(id = pk)
    indiv_file.isfavorite = True
    indiv_file.save()
    return redirect(reverse('box:home'))

@login_required(login_url='/login/')
def unfavorite_file(request, pk):
    indiv_file = FileModel.objects.get(id = pk)
    indiv_file.isfavorite = False
    indiv_file.save()
    return redirect(reverse('box:home'))

@login_required(login_url='/login/')
def share_file(request, pk):
    #print(request.method)
    if request.method == 'POST':
        form = ShareForm(request.POST)
        #print(form)
        if form.is_valid():
            indiv_file = FileModel.objects.get(id = pk)
            #indiv_file.shared_with.add(form.to_username)        
            indiv_file.shared_with = [indiv_file.shared_with, (form.cleaned_data['to_username'])]
            indiv_file.save()
            return redirect(reverse('box:home'))
    else:
        form = ShareForm()
    return render(request, 'share.html', {'form': form}) 
