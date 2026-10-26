from django.urls import path, include

from coaching.views import CompetitionListView, CompetitionDetailView, CompetitionCreateView, CompetitionUpdateView, \
    CompetitionDeleteView
from reviews.models import AthleteReflection
from reviews.views import AthleteReflectionListView, AthleteReflectionDetailView, AthleteReflectionCreateView, \
    AthleteReflectionUpdateView, AthleteReflectionDeleteView

urlpatterns =[
    path('training/<int:training_pk>/reflections/', include([
        path ('', AthleteReflectionListView.as_view(), name='reflection-list'),
        path('<int:pk>/', AthleteReflectionDetailView.as_view(), name='reflection-detail'),
        path('add/', AthleteReflectionCreateView.as_view(), name='reflection-add'),

        path('edit/<int:pk>/', AthleteReflectionUpdateView.as_view(), name='reflection-edit'),
        path('delete/<int:pk>', AthleteReflectionDeleteView.as_view(), name='reflection-delete'),
    ]) )
]