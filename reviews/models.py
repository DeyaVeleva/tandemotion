from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from coaching.models import Competition
from profiles.models import AthleteProfile, CoachProfile
from trainings.models import Training

class BaseReview(models.Model):
    title = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
    )
    training = models.ForeignKey(
        Training,
        on_delete=models.CASCADE,
        blank=True,
    )
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AthleteReflection(BaseReview):
    main_goals = models.TextField()
    reflection = models.TextField()
    author = models.ForeignKey(AthleteProfile, on_delete=models.CASCADE)

class CoachFeedback(BaseReview):
    feedback = models.TextField()
    author = models.ForeignKey(CoachProfile, on_delete=models.CASCADE)
    to_athlete= models.ForeignKey(AthleteProfile , on_delete=models.CASCADE)

#class CoachReflection





