from django.urls import include, path

from reviews.views import AthleteReflectionListView, AthleteReflectionCreateView
from trainings.views import TrainingListView, TrainingDetailView, TrainingCreateView, TrainingUpdateView, \
    TrainingDeleteView

urlpatterns = [
    path('training/', include([
        path('', TrainingListView.as_view(), name='training-list'),
        path('<int:pk>/', TrainingDetailView.as_view(), name='training-detail'),
        path('add/', TrainingCreateView.as_view(), name='training-create'),
        path('edit/<int:pk>/', TrainingUpdateView.as_view(), name='training-edit'),
        path('delete/<int:pk>/', TrainingDeleteView.as_view(), name='training-delete'),
        path('reflections/<int:training_pk>/', AthleteReflectionListView.as_view(), name='reflection-list'),
        path('reflections/<int:training_pk>/add', AthleteReflectionCreateView.as_view(), name='reflection-create'),
    ]))
]