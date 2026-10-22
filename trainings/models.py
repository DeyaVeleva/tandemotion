from django.db import models

from profiles.models import CoachProfile, AthleteProfile


class Training(models.Model):
    TYPE_CHOICES = ( #can change name
        ('PLYOMETRIC_TRAINING', 'Plyometric Training'),
        ('SAQ_TRAINING', 'SAQ Training'),
        ('HIIT', 'High-intensity interval training'),
        ('FLEXIBILITY', 'Flexibility training'),
        ('STRENGTH_TRAINING', 'Strength Training'),
        ('TACTICAL_TRAINING', 'Tactical Training'),
        ('TECHNICAL_TRAINING', 'Technical Training'),
        ('OTHER', 'Other'), # make a text field

    )
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    finish = models.TimeField()
    location = models.TextField(
        blank = True,
    )
    description = models.TextField(
        blank = True,
    )
    type =models.CharField(
        max_length=100,
        choices = TYPE_CHOICES, #make it choose more than one, a model
    )
    coaches = models.ManyToManyField(
        CoachProfile,
    )
    athletes = models.ManyToManyField(
        AthleteProfile,
    )

    class Meta:
        ordering = ('-date',)


