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
from .models import Research

class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = [
            'title', 'description', 'research_type', 
            'image', 'video_url', 'document',
            'researchers', 'year', 'status'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter research title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe the research...'}),
            'research_type': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.youtube.com/watch?v=...'}),
            'document': forms.FileInput(attrs={'class': 'form-control'}),
            'researchers': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dr. John Doe, Prof. Jane Smith'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2024'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
        help_texts = {
            'video_url': 'Paste a YouTube or Vimeo link. It will be embedded automatically.',
            'document': 'Upload PDF, DOC, or other research documents.',
            'researchers': 'Separate multiple names with commas.',
        }