import form as form
from django.http import HttpResponse
from django.shortcuts import render, redirect

from bookapp.models import Books
from . forms import BooksForm

# Create your views here.
def demo(request):
    objct=Books.objects.all()
    return render(request,'index.html',{'dict1':objct})

def brief(request,book_id):
    obj = Books.objects.get(id=book_id)
    return render(request, 'show.html', {'dict2': obj})


def add_book(request):
    if request.method=='POST':
        name = request.POST.get('name', )
        price = request.POST.get('price', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        book=Books(name=name,price=price, year=year,img=img)
        book.save()
    return render(request,'add.html')
def update(request,id):
    book= Books.objects.get(id=id)
    form=BooksForm(request.POST or None,request.FILES,instance= book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render( request,'edit.html', {'dict3':book, 'dict4':form})
def delete(request,id):
    if request.method=='POST':
        book = Books.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request,'delete.html')




































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































