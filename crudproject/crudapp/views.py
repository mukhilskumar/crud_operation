from django.shortcuts import render,redirect
from .models import Data
from django.views.generic import ListView

# Create your views here.


class ItemList(ListView):
    model = Data
    template_name='itemlist.html'

def home(request):
    obj=Data.objects.all()
    if request.method=='POST':
        slno=request.POST.get('SLNO','')
        name=request.POST.get('itemname','')
        description=request.POST.get('description','')
        data=Data(slno=slno,name=name,description=description)
        data.save()
    return render(request,'home.html',{'res':obj})

def update(request,id):
    obj1=Data.objects.get(id=id)
    if request.method=='POST':
        slno=request.POST.get('SLNO','')
        name=request.POST.get('itemname','')
        description=request.POST.get('description','')
        

        obj1.slno = slno
        obj1.name =name
        obj1.description=description
        obj1.save()
        return redirect('/')
    return render(request,'update.html',{'obj1':obj1})

def delete(request,id):
    task=Data.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')




