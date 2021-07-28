from django.forms import ModelForm, fields, models
from posts.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'descripcion', 'imagen')
        

