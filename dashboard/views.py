from django.shortcuts import redirect, render
from blog.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import AddCategory, AddPost, RegistrationForm, UserEditForm
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count =  Blog.objects.all().count()
    context = {
        'category_count' : category_count,
        'blog_count':  blog_count

    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='login')
def categories(request):
   categories = Category.objects.all()
   context = {
       'categories': categories
   }
   return render(request, 'dashboard/categories.html', context)

def add_category(request):
    if request.method == 'POST':
        form = AddCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = AddCategory()
    context = {
        'form': form 
    }

    return render(request, 'dashboard/add_category.html', context)

@login_required(login_url='login')
def edit_category(request, pk ):
    category_edit = Category.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddCategory(request.POST, instance=category_edit)
        if form.is_valid():
            form.save()
            return redirect('categories')           
    form = AddCategory(instance=category_edit)
    context = {
        'category_edit': category_edit,
        'form': form
    }
    return render(request, 'dashboard/edit_category.html', context)

@login_required(login_url='login')
def delete_category(request, pk):
    category_delete = Category.objects.get(pk=pk)
    category_delete.delete()
    return redirect('categories')


def posts(request):
    posts = Blog.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)
@login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            print('error')
            return redirect('posts')
    form = AddPost()
    context ={
        'form':form
    }
    return render(request, 'dashboard/add_post.html', context)

def edit_post(request, pk):
        post = Blog.objects.get(pk=pk)
        form = AddPost(instance=post)
        if request.method == 'POST':
            form = AddPost(request.POST, request.FILES, instance=post)
            if form.is_valid():
             post = form.save()
             title = form.cleaned_data['title']
             post.slug = slugify(title) + '-' + str(pk)
             post.save()
             return redirect('posts')


        context = {
            'form': form,
            'post': post
        }
        return render(request, 'dashboard/edit_post.html', context)
@login_required(login_url='login')
def delete_post(request, pk ):
    post = Blog.objects.get(pk=pk)

    post.delete()
    messages.info(request, 'successfully deleted')

    return redirect('posts')


def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/users.html', context)

@login_required(login_url='login')
def add_user(request):
    form = RegistrationForm()

    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            messages.info(request, 'something went wrong')
            return redirect('add_user')

    context = {
        'form': form,
    }

    return render(request, 'dashboard/add_user.html', context)

def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    form = UserEditForm(instance=user) 
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user) 

        if form.is_valid:
            form.save()
            messages.info(request, 'user successfully edited!')
            return redirect('users')
        else:
            messages.info(request, 'something went wrong!')
            print(form.errors)
            return render('edit_user')
            
    context = {
        'user': user,
        'form' : form
    }

    return render(request, 'dashboard/edit_user.html', context)

def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    messages.info(request, 'user deleted successfully')
    return redirect('users')