from django.shortcuts import render,redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.

def index(request):
    photos = Photo.objects.all()
    
    context ={
        'photos':photos,
    }
    return render(request,'pic/index.html',context)

def load(request):
    form=PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Index')

    context = {
        'form':form
    }
    
    return render(request,'pic/load.html',context)