from django.contrib.auth import forms
from django.contrib import admin
from django.contrib.auth.models import User

from blog.models import Tag, Post, Comment


# Register your models here.


class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


admin.site.register(Tag)

admin.site.register(Post)

admin.site.register(Comment)



