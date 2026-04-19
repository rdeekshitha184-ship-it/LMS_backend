from django.db import models

class TimetableEntry(models.Model):
    DAY_CHOICES = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
    ]
    day          = models.CharField(max_length=3, choices=DAY_CHOICES)
    period       = models.PositiveIntegerField()
    subject      = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    start_time   = models.TimeField()
    end_time     = models.TimeField()

    class Meta:
        unique_together = ('day', 'period')
        ordering = ['day', 'period']

    def __str__(self):
        return f"{self.day} | P{self.period} | {self.subject}"