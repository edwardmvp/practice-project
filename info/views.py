from django.shortcuts import render, redirect 
from .models import *
from .form import addProjectForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout

@login_required
def index(request):

    return render (
        request,
        template_name='index.html',
        context={}
    )

@login_required
def catalog_book(request):
    books = Book.objects.all()
    return render(
        request,
        template_name='catalog_list.html',
        context={'books': books}
    )

@login_required
def book_detail(request, pk):
    book_id = Book.objects.get(pk=pk)

    return render(
        request,
        template_name='book_detail.html',
        context={'book': book_id}
    )

@login_required
def info(request):
    

    return render(
        request,
        template_name='info.html',
        context={}
    )

@login_required
def project(request):

    project = Project.objects.all()

    return render(
        request,
        template_name='project.html',
        context={'project': project}
    )

@login_required
def add_project(request):

    if request.method == 'POST':
        form = addProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = addProjectForm()

    return render(
        request,
        template_name="add_project.html",
        context={"form": form}
    )




def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        return redirect(index)

# @login_required(login_url="/accounts/login/")
# def addCat(request):
#     if request.method == "POST":
#         form = AddInfoCatModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(
#                 "index"
#             )
#         else:
#             form = AddInfoCatModelForm()
#         return render(request, template_name="addcat.html", context=("form": form))