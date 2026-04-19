from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as log_out
from django.contrib import messages
from .models import Category, Blog
from about.models import About, Socials
from django.db.models import Q



# Create your views here.
def home(request):
    category = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True)
    posts = Blog.objects.filter(is_featured = True, status =1)
    about = About.objects.all()
    social = Socials.objects.all()

    context = {
        'category': category,
        'featured_post':featured_post,
        'posts': posts,
         'about':  about,
         'social':  social,
    }
    return render(request, 'home.html',  context)

def post_by_category(request, category_id):
        post_by_category = Blog.objects.filter(status =1, category_id=category_id)

        try:
            single_categorry = Category.objects.get(pk=category_id)
            categories = Category.objects.all()
        except:
             return render(request, 'error_page.html')
        context = {
            'post_by_category': post_by_category,
            'single_categorry': single_categorry,
            'categories':categories,
           

        }
        return render(request, 'post_by_category.html', context)

def blog(request, slug):
        try:
            blog = get_object_or_404(Blog,  slug=slug)
            context = {
                'blog': blog
                    }
            return render(request, 'blog.html', context )
        except:
             return render(request, 'error_page.html')

def search(request):
    keyword = request.GET.get('keyword')
    blog = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status=1)

    context = {
          'blog': blog,
          'keyword': keyword
    }
    return render(request, 'search.html', context)

def register(request):
    if request.method == 'POST':
        #  register user
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2: 
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists try another one')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                    messages.info(request, 'Email already exists try another one')
                    return redirect('register')
            else:
                 user = User.objects.create_user(username=username, password=password1, email=email)
                 user.save()
                 messages.info(request, 'user registered successfully')
                 return redirect('home')
        else: 
               messages.info(request, 'Email already exists try another one')
               return redirect('register')
    else:
         return render(request, 'register.html')

def login(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']

          user = authenticate(username=username, password=password)
          if user is not None:
            auth_login(request, user)
            messages.info(request, 'Welcome to the site')
            return redirect('home')
          else:
            messages.info(request, 'username or password did not match')
            return redirect('login')
     return render(request, 'login.html')

def logout(request):
    log_out(request)
    messages.info(request, 'You are logged out')
    return redirect('home')
