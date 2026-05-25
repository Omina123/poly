import os
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


# --- PORTAL TRACKING MODELS ---

class NoticeBoard(models.Model):
    """
    Central Information Hub Model handling corporate institutional clearance documentation:
    - Official Memos (Maroon)
    - Campus News Matrix (Green)
    - Urgent Announcements (Gold/Yellow)
    """
    CATEGORY_CHOICES = [
        ('memo', 'Official Institutional Memo'),
        ('news', 'Campus News Matrix Post'),
        ('announcement', 'Urgent Operational Registry Announcement'),
    ]

    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='memo',
        help_text="Determines which structural column feed this notice loads under."
    )
    title = models.CharField(
        max_length=255, 
        help_text="The main heading text displayed on the notice card wrapper."
    )
    reference_number = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text="Optional catalog index parameter (e.g., TENP/EX/05/26), mostly used for internal memos."
    )
    content = models.TextField(
        help_text="Main informational paragraph context block detailing the update payload."
    )
    file_attachment = models.FileField(
        upload_to=get_notice_file_path,
        blank=True,
        null=True,
        help_text="Accepts document variants like PDFs or Docs for instant client download."
    )
    image = models.ImageField(
        upload_to=get_notice_image_path,
        blank=True,
        null=True,
        help_text="Dynamic graphic asset used uniquely within the news column layout matrix."
    )
    # author = models.ForeignKey(
    #     User,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     help_text="Maps publishing administration user parameters."
    # )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Automatic timestamp record entry used for downstream ordering arrays (-created_at)."
    )

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