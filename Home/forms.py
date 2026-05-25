from django import forms
from .models import NoticeBoard

class NoticeForm(forms.ModelForm):
    class Meta:
        model = NoticeBoard
        fields = ['category', 'title', 'reference_number', 'content', 'file_attachment', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter notice title'}),
            'reference_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., TENP/EX/05/26'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your notice body context here...'}),
            'file_attachment': forms.FileInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }