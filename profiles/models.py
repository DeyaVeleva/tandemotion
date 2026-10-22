from django.db import models

class BaseProfile(models.Model):
    ROLE_CHOICES = (
        ('COACH', 'Coach'),
        ('ATHLETE', 'Athlete'),
    )

    username = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    #password = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    profile_pic = models.ImageField(upload_to = 'media/profile_pics')
    #role = models.CharField(max_length = 10, choices = ROLE_CHOICES)
    sport = models.CharField(max_length = 100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.username

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
        blank = True,
    )

class AthleteProfile(BaseProfile):

    main_competition_category = models.CharField(max_length = 100)
    other_competition_categories = models.CharField(max_length = 100)
    #Do a competition category model
    #coaches = models.ManyToManyField(
     #   'CoachProfile',
    #    blank = True,
   #)
