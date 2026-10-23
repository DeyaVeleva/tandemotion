from django.contrib import admin

from profiles.models import CoachProfile, AthleteProfile

admin.site.register(CoachProfile)
admin.site.register(AthleteProfile)
