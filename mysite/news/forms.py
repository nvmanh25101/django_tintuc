from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Comment


class SignupForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username')
    email = forms.EmailField(max_length=100, label='Email')
    password1 = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=100, label='Confirm Password', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']

            if password2 == password1 and password1:
                return password2
        raise forms.ValidationError("Password does not match")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Username can only contain alphanumeric characters and the underscore.")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Username is already taken.")

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.article = kwargs.pop('article', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.article = self.article
        comment.save()

    class Meta:
        model = Comment
        fields = ['content']  # cac field muon hien thi tren form
