from django.db import models
from profiles.models import CoachProfile, AthleteProfile

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    coach = models.ForeignKey(CoachProfile, on_delete=models.CASCADE)
    athletes = models.ManyToManyField(AthleteProfile)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    coach = models.ForeignKey(CoachProfile, on_delete=models.CASCADE)
    athletes = models.ManyToManyField(AthleteProfile)

    def __str__(self):
        return self.title

class Competition(models.Model):
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    athletes = models.ManyToManyField(AthleteProfile, blank=True)
    coaches = models.ManyToManyField(CoachProfile, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

