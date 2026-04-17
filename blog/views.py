from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
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

        blog = get_object_or_404(Blog,  slug=slug)
        context = {
            'blog': blog
                }
        return render(request, 'blog.html', context )

def search(request):
    keyword = request.GET.get('keyword')
    blog = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status=1)

    context = {
          'blog': blog,
          'keyword': keyword
    }
    return render(request, 'search.html', context)