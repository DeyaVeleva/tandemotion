from django.db import models

from profiles.models import CoachProfile, AthleteProfile


class Training(models.Model):
    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    finish = models.TimeField()
    location = models.TextField(
        blank = True,
    )
    description = models.TextField(
        blank = True,
    )
    types =models.CharField(max_length=100)
    coaches = models.ManyToManyField(
        CoachProfile,
    )
    athletes = models.ManyToManyField(
        AthleteProfile,
    )
    def __str__(self):
        return f'{self.title}'
    class Meta:
        ordering = ['-start']

