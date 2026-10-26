from django.db import models

class BaseProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    email = models.EmailField(max_length = 100, unique = True)
    sport = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    #class Meta:
    #    abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class CoachProfile(BaseProfile):
    SPECIALTY_CHOICES = (
        ('HEAD_COACH', 'Head Coach'),
        ('ASSISTANT_COACH', 'Assistant Coach'),
        ('STRENGTH_AND_CONDITIONING_COACH', 'Strength and Conditioning Coach'),
        ('MENTAL_SKILL_COACH', 'Mental Skill Coach'),
        ('SKILL_COACH', 'Skill Coach'),
        ('YOUTH_COACH', 'Youth Coach'),
        ('OTHER_COACH', 'Other Coach'),
    )
    specialty = models.CharField(max_length = 50, choices = SPECIALTY_CHOICES)
    athletes = models.ManyToManyField(
        'AthleteProfile',
        related_name='coaches',
        blank = True,
    )

class AthleteProfile(BaseProfile):

    main_competition_category = models.CharField(max_length = 100, blank=True)
    other_competition_categories = models.CharField(max_length = 100, blank = True)
