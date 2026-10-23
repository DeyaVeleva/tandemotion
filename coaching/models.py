from django.db import models
from profiles.models import CoachProfile, AthleteProfile

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    coach = models.ForeignKey(CoachProfile, on_delete=models.CASCADE)
    athletes = models.ManyToManyField(AthleteProfile, blank=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.BooleanField(default=False) # make a model
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    coach = models.ForeignKey(CoachProfile, on_delete=models.CASCADE)
    athletes = models.ManyToManyField(AthleteProfile, blank=True)
    is_read = models.BooleanField(default=False)

class Competition(models.Model):
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    athletes = models.ManyToManyField(AthleteProfile, blank=True)
    coaches = models.ManyToManyField(CoachProfile, blank=True)
    description = models.TextField()


