from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import book


def book_list(request):
    allBooks = book.objects.all().values()
    template = loader.get_template('book_list.html')
    context = {
        'allBooks': allBooks
    }
 
    return HttpResponse(template.render(context, request))

def book_detail(request, id):
        bookDetail = book.objects.get(id=id)

        template = loader.get_template('book_detail.html')

        context = {
            'bookDetail': bookDetail
        }
        return HttpResponse(template.render(context, request))

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        published_date = request.POST.get('published_date')

        template = loader.get_template('add_book.html')
        newdata = book(
            title=title,
            author=author,
            description= description,
            published_date= published_date
        )

        newdata.save()

        return HttpResponse(template.render())
       
def update_book(request):
     if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        published_date = request.POST.get('published_date')
        update = book.objects.get(title = title)

        template = loader.get_template('update_book.html')
        if update:
            update.title=title
            update.author=author
            update.description= description
            update.published_date= published_date
        
            update.save()

        return HttpResponse(template.render()) 
def delete_book(request):
     if (request.POST):
        title = request.POST.get('title')

        template = loader.get_template('delete_book.html')

        deleteBook =  book.objects.filter(title = title)
        if deleteBook:
            deleteBook.delete()
        return HttpResponse(template.render())
