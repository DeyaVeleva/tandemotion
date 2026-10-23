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
    types =models.ManyToManyField('TrainingType')
    coaches = models.ManyToManyField(
        CoachProfile,
    )
    athletes = models.ManyToManyField(
        AthleteProfile,
    )

    class Meta:
        ordering = ['-start']

class TrainingType(models.Model):
    title = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.title
