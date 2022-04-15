from dataclasses import field
from .models import Movie, Comment
from django import forms

class MovieForm(forms.ModelForm):
    
    title = forms.CharField(
        max_length=20,
        label='title',
        widget=forms.TextInput(
            attrs = {
                'class':'mytitle form-control',
                'placeholder' : '제목',
            }
        )
    )
    
    description = forms.CharField(
        label='description',
        widget=forms.Textarea(
            attrs = {
                'class':'mydescription form-control',
                'placeholder' : '내용',
            }
        )
    )
    
    class Meta:
        model = Movie
        fields = ('title', 'description',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='content',
        widget=forms.Textarea(
            attrs = {
                'class':'mycontent form-control',
                'placeholder' : '덧글',
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('content',)