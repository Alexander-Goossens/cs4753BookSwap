from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from home.forms import UserForm
from home.forms import BookForm
from home.models import Book
from django.db.models import Q
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView


def search(request):
    query = request.GET.get('q')
    if query:
        results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(isbn__icontains=query) | Q(course__icontains=query)).order_by('price')
    else:
        results = Book.objects.all()
    return render(request, 'search_result.html', {'results':results})

def homepage(request):
	return render(request, 'home/homepage.html')


def index(request):
	return render(request, 'home/index.html')
@login_required	
def about(request):
    return render(request, 'home/about.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Your account is disabled!")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
            
    else:
        return render(request, 'home/login.html', {})

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(user_form.errors)
	else:
		user_form = UserForm()

	return render(request, 'home/register.html', {'user_form': user_form, 'registered': registered})

@login_required
def user_logout(request): 
    logout(request)
    return HttpResponseRedirect('/home/')

def view_books(request):
    books_list = Book.objects.filter(booker=request.user)
    context = {'books_list': books_list}
    return render(request, 'home/viewbooks.html', context)

def viewallbooks(request):
    allbooks_list = Book.objects.all()
    context = {'allbooks_list': allbooks_list}
    return render(request, 'home/viewbooks.html', context)
@login_required
def view_book(request, book_name_url):
    book = get_object_or_404(Book, id=book_name_url)
    return render(request, 'home/viewbook.html', {'book': book})

@login_required
def edit_book(request, book_pk):
    inst = get_object_or_404(Book, pk=book_pk)
    rpk = book_pk
    editing = True
    book_form = BookForm(request.POST or None, instance=inst)
    if book_form.is_valid():
        book_form.save()
        return HttpResponseRedirect('/home/viewbooks/')
    return render(request, 'home/filebook.html', {'book_form': book_form, 'editing': editing, 'rpk': rpk})

@login_required
def file_book(request):
    if request.method == 'POST':
        book_form = BookForm(data=request.POST)

        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.booker = request.user
            book.save()
            return HttpResponseRedirect('/home/')

    else:
        book_form = BookForm()

    return render(request, 'home/filebook.html', {'book_form': book_form})