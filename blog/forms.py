from django import forms

from blog.models import Post, Comment, Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            widget.attrs.update({'class': 'form-control'})


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = Post
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        post = super().save(commit=False)
        post.author = self.user
        if commit:
            post.save()
            self.save_m2m()
        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'autor']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.autor = self.user
        if commit:
            comment.save()
        return comment
