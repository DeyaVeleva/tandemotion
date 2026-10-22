from django.db import models

class Review(models.Model):
    personal_rating = models.PositiveIntegerField(default=0) #validator for max
    main_goals = models.TextField(blank=True)


