from django.forms import ModelForm
from blog.models import Category, Blog, User
from django.contrib.auth.forms import UserCreationForm


class AddCategory(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class AddPost(ModelForm):
    class Meta:
        model = Blog
        fields = 'title',  'category', 'featured_image', 'is_featured', 'short_description', 'blog_body', 'status', 'blog_body'

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'is_superuser', 'groups', 'is_active', 'user_permissions' )

class UserEditForm(ModelForm):
        class Meta:
          model = User
          fields = ('username', 'email' , 'first_name', 'last_name', 'is_superuser', 'groups', 'is_active', 'user_permissions' )
