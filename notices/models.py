from django.db import models
from accounts.models import User

class Notice(models.Model):
    CATEGORY_CHOICES = [
        ('holiday', 'Holiday'),
        ('event', 'Event'),
        ('general', 'General'),
    ]
    title      = models.CharField(max_length=200)
    content    = models.TextField()
    category   = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    posted_by  = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title