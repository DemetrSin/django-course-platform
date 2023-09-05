from django import forms
from .models import Course, Comments


class UserAddCourse(forms.ModelForm):
    slug = forms.SlugField(
        label='Name of URL:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL name:'}),
    )
    title = forms.CharField(
        label='Name of course:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course name:'}),
    )
    description = forms.CharField(
        label='Description:',
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter course description:'}),
    )
    img = forms.ImageField(
        label='Add photo:',
        required=False,
        widget=forms.FileInput,
    )

    class Meta:
        model = Course
        fields = ['slug', 'title', 'description', 'img']


class AddComment(forms.ModelForm):
    comment = forms.CharField(
        label='Add your comment:',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment:'}),
    )

    class Meta:
        model = Comments
        fields = ['comment']
