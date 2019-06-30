from django.shortcuts import render
from catalog.models import Genre,Language,Book,BookInstance,Author
from django.views import generic

def index(request):
    no_books=Book.objects.all().count()
    no_instances=BookInstance.objects.all().count()
    no_avail=BookInstance.objects.filter(status__exact='a').count()
    no_auth=Author.objects.count()

    context={
    'no_books':no_books,
    'no_instances':no_instances,
    'no_avail':no_avail,
    'no_auth':no_auth,
    }


    return render(request,'index.html',context=context)

class BookListView(generic.ListView):
    model=Book
    paginate_by=2

class BookDetailView(generic.DetailView):
    model=Book

class AuthorListView(generic.ListView):
    model=Author

class AuthorDetailView(generic.DetailView):
    model=Author
