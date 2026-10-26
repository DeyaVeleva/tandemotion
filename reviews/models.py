from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from coaching.models import Competition
from profiles.models import AthleteProfile, CoachProfile
from trainings.models import Training

class BaseReview(models.Model):
    title = models.CharField(max_length=100)
    training = models.ForeignKey(
        Training,
        on_delete=models.CASCADE,
        related_name='reflections',
        blank=True,
        null=True,
    )
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if bool(self.training) == bool(self.competition):
            raise ValidationError( 'You have to have a training or a competition. ')

    @property
    def event_title(self):
        if self.training:
            return self.training.title
        else:
            return self.competition.name

    def __str__(self):
        return f'{self.title} | {self.event_title}'

class AthleteReflection(BaseReview):
    rating = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
    )
    main_goals = models.TextField()
    reflection = models.TextField()
    author = models.ForeignKey(AthleteProfile, on_delete=models.CASCADE)








