from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Category, Blog

# Create your views here.
def home(request):
    category = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True)
    posts = Blog.objects.filter(is_featured = True, status =1)
    print(featured_post)
    context = {
        'category': category,
        'featured_post':featured_post,
        'posts': posts
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
            'categories':categories

        }
        return render(request, 'post_by_category.html', context)