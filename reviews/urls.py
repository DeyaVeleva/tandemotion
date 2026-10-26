from django.urls import path, include

from coaching.views import CompetitionListView, CompetitionDetailView, CompetitionCreateView, CompetitionUpdateView, \
    CompetitionDeleteView
from reviews.views import AthleteReflectionListView, AthleteReflectionDetailView, AthleteReflectionCreateView, \
    AthleteReflectionUpdateView, AthleteReflectionDeleteView

urlpatterns =[
    path('reflections/', include([
        path('<int:pk>/', AthleteReflectionDetailView.as_view(), name='reflection-detail'),

        path('edit/<int:pk>/', AthleteReflectionUpdateView.as_view(), name='reflection-edit'),
        path('delete/<int:pk>', AthleteReflectionDeleteView.as_view(), name='reflection-delete'),
    ]) )
]