from django.shortcuts import render, render_to_response
from userlogin.forms import UserCreationForm
from django.http import HttpResponseRedirect

from django.views.generic import ListView, FormView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .models import FilebabyFile
from .forms import FilebabyForm

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

class FileListView(ListView):

    model = FilebabyFile
    queryset = FilebabyFile.objects.order_by('-id')
    context_object_name = "files"
    #template_name = "filebaby/index.html"
    template_name = "index.html"
    paginate_by = 5


class FileAddView(FormView):

    form_class = FilebabyForm
    success_url = reverse_lazy('home')
    #template_name = "filebaby/add.html"
    template_name = "add-boring.html"

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, 'File uploaded!', fail_silently=True)
        return super(FileAddView, self).form_valid(form)

