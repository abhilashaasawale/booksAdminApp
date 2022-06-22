from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def index(request):
    return render(request,"index.html")
    
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/options")
            else:
                return HttpResponse("You are not an admin.")
        else:
            return HttpResponse("Please enter valid credentials.")
    return render(request, "admin_login.html")
    
def options(request): 
    return render(request,"options.html")


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("admin_login")
    template_name = "registration.html"

def creationPage(request):
    return render(request,"creation.html")
    
def create(request):
    if request.method == 'POST':
        bookName = request.POST['bookname']
        authorName = request.POST['author']
        if bookName=='' and authorName=='':
            return HttpResponse("Please enter book name and author name.")
        else:
            bookFilter = Book.objects.filter(name=bookName,author=authorName)
            books = Book.objects.create(name=bookName, author=authorName)
            books.save()
            alert = True
            return redirect("/options",{'alert':alert})
    return render(request,"creation.html")

def retrieve(request):
    books = Book.objects.all()
    return render(request, "retrieveBooks.html", {'books':books})
    
def delete(request):
    if request.method == "POST":
        bookName = request.POST['bookName']
        books = Book.objects.filter(name=bookName)
        books.delete()
        return redirect("/options")
    return render(request,"deleteBook.html")

def update(request):
    if request.method == "POST":
        bookName = request.POST['book_name']
        author = request.POST['author']
        book = Book.objects.get(name=bookName)
        if bookName != '' and author != '':
            book.name = bookName
            book.author = author
            book.save()
        elif bookName == '':
            book.author = author
            book.save()
        elif author == '':
            book.name = bookName
            book.save()
        return redirect("/options")
    return render(request,"update.html")

def Logout(request):
    logout(request)
    return redirect ("/")
        
    