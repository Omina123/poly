import os
from django.conf import settings
from django.shortcuts import render,redirect
from .models import NoticeBoard, Partner
from .forms import NoticeForm
def home(request):
    # 1. Fetch dynamic folder images for your main banner sliders
    slider_folder = os.path.join(settings.STATIC_ROOT, 'img', 'sliders') # or settings.STATICFILES_DIRS
    try:
        # Grabs all filenames inside your static slider folder automatically
        slider_images = [f for f in os.listdir(slider_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    except FileNotFoundError:
        slider_images = []

    context = {
        'slider_images': slider_images,
        'memos': NoticeBoard.objects.filter(category='memo').order_by('-created_at'),
        'news': NoticeBoard.objects.filter(category='news').order_by('-created_at'),
        'announcements': NoticeBoard.objects.filter(category='announcement').order_by('-created_at'),
        'partners': Partner.objects.all(),
    }
    return render(request, 'home.html', context)

# Optional: Ensures only logged-in portal users can post
def create_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user  # Assign the logged-in user as author
            notice.save()
            return redirect('home')  # Redirect back to your home view page
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