from django.forms import ModelForm
from blog.models import Category, Blog

class AddCategory(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class AddPost(ModelForm):
    class Meta:
        model = Blog
        fields = 'title',  'category', 'featured_image', 'is_featured', 'short_description', 'blog_body', 'status', 'blog_body'