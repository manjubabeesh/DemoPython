from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from.models import Task
from.forms import TodoForms
from django .views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class Tasklistview(ListView):
    model=Task
    template_name='index.html'
    context_object_name = 'dict1'

class Taskdetailview(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'key1'

class Taskupdateview(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name = 'key1'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvupdate',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url = 'cbvindex'

def add(request):
    task=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
        return redirect('/')
    return render(request,'index.html', {'dict1':task})
def details(request):
     return render(request,'detail.html')
def delete(request,task_id):
    task = Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form1=TodoForms(request.POST or None,instance=task)
    if form1.is_valid():
        form1.save()
        return redirect(('/'))
    return render(request,'edit.html',{'dict2':task,'dict3':form1})