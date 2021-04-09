from django import forms
from .models import BlogPost
# Import From THIRDPARTY Package
from markdownx.models import MarkdownxFormField

class BlogForm(forms.ModelForm):
    content = MarkdownxFormField()
    class Meta:
        model = BlogPost
        fields= "__all__"
    