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
    def get_context_data(self, **kwargs):
        context = super(FileListView, self).get_context_data(**kwargs)
        context['file_list'] = FileModel.objects.all()
        context['favorites_list'] = FileModel.objects.filter(isfavorite = True)
        return context    
    
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
