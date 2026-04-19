# from django.db import models
# from accounts.models import User

# class Assignment(models.Model):
#     SUBJECT_CHOICES = [
#         ('math','Mathematics'), ('science','Science'), ('english','English'),
#         ('history','History'), ('geography','Geography'), ('physics','Physics'),
#         ('chemistry','Chemistry'), ('biology','Biology'), ('cs','Computer Science'),
#     ]
#     subject     = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
#     title       = models.CharField(max_length=200)
#     description = models.TextField()
#     due_date    = models.DateField()
#     file        = models.FileField(upload_to='assignments/', blank=True, null=True)
#     created_by  = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at  = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.title} (due: {self.due_date})"

from django.db import models
from accounts.models import User

class Assignment(models.Model):
    subject     = models.CharField(max_length=100)  # Free text now
    title       = models.CharField(max_length=200)
    description = models.TextField()
    due_date    = models.DateField()
    file        = models.FileField(upload_to='assignments/', blank=True, null=True)
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (due: {self.due_date})"