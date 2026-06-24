from datetime import timezone
import os
from django.utils import timezone

from django.db import models
# from django.contrib.auth.models import User

# --- UPLOAD HELPER PIPELINES ---
def get_notice_file_path(instance, filename):
    """Saves uploaded PDFs/Docs into media/notice_board/docs/"""
    return os.path.join('notice_board', 'docs', filename)

def get_notice_image_path(instance, filename):
    """Saves uploaded news display metrics images into media/notice_board/images/"""
    return os.path.join('notice_board', 'images', filename)

def get_partner_logo_path(instance, filename):
    """Saves partner brand graphics into media/partners/"""
    return os.path.join('partners', filename)


# --- PORTAL TRACKING MODELS ---from django.utils import timezone   # ✅ correct
from django.db import models
import os

# ... (upload helpers unchanged) ...
class Research(models.Model):
    RESEARCH_TYPES = [
        ('project', 'Research Project'),
        ('publication', 'Publication'),
        ('innovation', 'Innovation'),
        ('collaboration', 'Collaboration'),
        ('conference', 'Conference'),
    ]

    title = models.CharField(max_length=255, help_text="Title of the research/innovation")
    description = models.TextField(help_text="Detailed description of the research")
    research_type = models.CharField(max_length=20, choices=RESEARCH_TYPES, default='project')
    
    # Media fields
    image = models.ImageField(
        upload_to='research/images/',
        blank=True,
        null=True,
        help_text="Main image for the research item"
    )
    video_url = models.URLField(
        blank=True,
        null=True,
        help_text="YouTube or Vimeo URL (e.g., https://www.youtube.com/watch?v=...)"
    )
    document = models.FileField(
        upload_to='research/docs/',
        blank=True,
        null=True,
        help_text="PDF or document file"
    )
    
    # Additional info
    researchers = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Names of researchers involved (comma separated)"
    )
    year = models.IntegerField(
        blank=True,
        null=True,
        help_text="Year of publication/completion"
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('ongoing', 'Ongoing'),
            ('completed', 'Completed'),
            ('published', 'Published'),
            ('pending', 'Pending Review'),
        ],
        default='ongoing'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Research Item"
        verbose_name_plural = "Research Items"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_video_embed_url(self):
        """Convert YouTube URL to embed URL"""
        if not self.video_url:
            return None
        # Extract video ID for YouTube
        if 'youtube.com/watch?v=' in self.video_url:
            video_id = self.video_url.split('v=')[1]
            if '&' in video_id:
                video_id = video_id.split('&')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        elif 'youtu.be/' in self.video_url:
            video_id = self.video_url.split('youtu.be/')[1]
            return f'https://www.youtube.com/embed/{video_id}'
        elif 'vimeo.com/' in self.video_url:
            return self.video_url
        return None
class NoticeBoard(models.Model):
    CATEGORY_CHOICES = [
        ('memo', 'Official Institutional Memo'),
        ('news', 'Campus News Matrix Post'),
        ('announcement', 'Urgent Operational Registry Announcement'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='memo')
    title = models.CharField(max_length=255)
    reference_number = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    file_attachment = models.FileField(upload_to=get_notice_file_path, blank=True, null=True)
    image = models.ImageField(upload_to=get_notice_image_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ✅ NEW fields
    start_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Notice Board Entry"
        verbose_name_plural = "Notice Board Entries"
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.get_category_display()}] - {self.title}"

class Partner(models.Model):
    """
    Tracks external industry collaborative network profiles.
    Loads dynamic logo assets grayscale-inverted into the bottom platform section.
    """
    name = models.CharField(
        max_length=150, 
        unique=True, 
        help_text="The official company name of the technical attachment placement partner."
    )
    logo = models.ImageField(
        upload_to=get_partner_logo_path,
        help_text="High-resolution brand asset mark (handled automatically with institutional CSS filters)."
    )
    website_url = models.URLField(
        blank=True, 
        null=True, 
        help_text="Optional hyperlink destination pointer for student placement inquiries."
    )
    date_added = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Industry Partner"
        verbose_name_plural = "Industry Partners"
        ordering = ['name']

    def __str__(self):
        return self.name