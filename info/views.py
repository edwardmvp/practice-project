from django.shortcuts import render 
from .models import *



def index(request):
    
    books =  Book.objects.all()

    return render (
        request,
        template_name='index.html',
        context={
            'books': books
            }
    )


def catalog_book(request):
    books = Book.objects.all()
    return render(
        request,
        template_name='catalog_list.html',
        context={'books': books}
    )

def book_detail(request, pk):
    book_id = Book.objects.get(pk=pk)

    return render(
        request,
        template_name='book_detail.html',
        context={'book': book_id}
    )
# Create your views here.
