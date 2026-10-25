from django.urls import path, include

from profiles.models import AthleteProfile
from profiles.views import home_page_view, AthleteProfileDetailView, CoachProfileDetailView, AthleteProfileListView, \
    CoachProfileListView, AthleteProfileCreateView, CoachProfileCreateView, AthleteProfileUpdateView, \
    CoachProfileUpdateView, AthleteProfileDeleteView, CoachProfileDeleteView

urlpatterns = [
    path('athletes/', include([
        path('', AthleteProfileListView.as_view(), name = 'athletes-list' ),
        path('<int:pk>/', AthleteProfileDetailView.as_view(), name="athlete-details"),
        path('add/', AthleteProfileCreateView.as_view(), name='athlete-add'),
        path('edit/<int:pk>/', AthleteProfileUpdateView.as_view(), name='athlete-edit'),
        path('delete/<int:pk>/', AthleteProfileDeleteView.as_view(), name='athlete-delete'),
    ])),
    path('coaches/', include([
        path('', CoachProfileListView.as_view(), name = 'coaches-list' ),
        path('<int:pk>/', CoachProfileDetailView.as_view(), name="coach-details"),
        path('add/', CoachProfileCreateView.as_view(), name='coach-add'),
        path('edit/<int:pk>/', CoachProfileUpdateView.as_view(), name='coach-edit'),
        path('delete<int:pk>/', CoachProfileDeleteView.as_view(), name='coach-delete'),
    ])),

]