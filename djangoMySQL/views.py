from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from .models import Book
from django.http import HttpResponse

class BookView(View):
    def get(self, request):
        # Render a form to create a new book
        return render(request, 'add_book.html')

    def post(self, request):
        # Handle form submission to create a new book
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        if title and author and published_date:
            Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('/books/')  # Redirect to the book list page
        else:
            return HttpResponse("All fields are required!", status=400)

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
