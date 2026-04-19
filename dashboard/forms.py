from django.forms import ModelForm
from blog.models import Category

class AddCategory(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'