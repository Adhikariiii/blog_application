from .models import Category
from about.models import Socials

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)
def get_socials(request):
    socials = Socials.objects.all()
    return dict(socials=socials)
