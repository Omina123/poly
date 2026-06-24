import os
from pyexpat.errors import messages
from django.conf import settings
from django.shortcuts import get_object_or_404, render,redirect
from .models import NoticeBoard, Partner
from .forms import NoticeForm
from django.shortcuts import render, redirect
from django.utils import timezone
from django.db import models
from .models import NoticeBoard, Partner
from .forms import NoticeForm
import os
from django.conf import settings

def home(request):
    slider_folder = os.path.join(settings.STATIC_ROOT, 'img', 'sliders')
    try:
        slider_images = [f for f in os.listdir(slider_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    except FileNotFoundError:
        slider_images = []

    now = timezone.now()

    # ✅ Active notices: start_date <= now AND (expiry_date IS NULL OR expiry_date >= now)
    active_notices = NoticeBoard.objects.filter(
        start_date__lte=now
    ).filter(
        models.Q(expiry_date__isnull=True) | models.Q(expiry_date__gte=now)
    )

    context = {
        'slider_images': slider_images,
        'memos': active_notices.filter(category='memo').order_by('-created_at'),
        'news': active_notices.filter(category='news').order_by('-created_at'),
        'announcements': active_notices.filter(category='announcement').order_by('-created_at'),
        'partners': Partner.objects.all(),
    }
    return render(request, 'home.html', context)

def create_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            # notice.author = request.user   # if you have a user field
            notice.save()
            return redirect('home')
    else:
        form = NoticeForm()
    return render(request, 'create_notice.html', {'form': form})
def council(request):
    return render(request, 'council.html')
def Higher_diploma(request):
    return render(request, 'higher_diploma.html')
def certificate(request):
    return render(request, 'diploma.html')
def diploma(request):
    return render(request, 'diploma.html')
def artisan(request):
    return render(request, 'artisan.html')
def Contact(request):
    return render(request, 'contact.html')
from .models import Research
from .forms import ResearchForm

def research_view(request):
    research_items = Research.objects.all().order_by('-created_at')
    
    # Filter by type if specified
    research_type = request.GET.get('type')
    if research_type:
        research_items = research_items.filter(research_type=research_type)
    
    context = {
        'research_items': research_items,
        'research_types': Research.RESEARCH_TYPES,
    }
    return render(request, 'research.html', context)

def create_research(request):
    if request.method == 'POST':
        form = ResearchForm(request.POST, request.FILES)
        if form.is_valid():
            research = form.save(commit=False)
            # research.author = request.user  # uncomment if you have user auth
            research.save()
            # messages.success(request, 'Research item added successfully!')
            # message.success(request, 'Research item added successfully!')
            return redirect('research')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ResearchForm()
    
    context = {
        'form': form,
        'is_creating': True,
    }
    return render(request, 'create_research.html', context)

def research_detail(request, pk):
    research = get_object_or_404(Research, pk=pk)
    context = {
        'research': research,
    }
    return render(request, 'research_detail.html', context)