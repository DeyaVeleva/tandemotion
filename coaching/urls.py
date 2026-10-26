

from django.urls import path, include

from coaching.views import CompetitionListView, CompetitionDetailView, CompetitionCreateView, CompetitionUpdateView, \
    CompetitionDeleteView

urlpatterns = [
    path('competitions/', include([
        path('', CompetitionListView.as_view(), name='competition-list'),
        path('<int:pk>/', CompetitionDetailView.as_view(), name='competition-detail'),
        path('add/', CompetitionCreateView.as_view(), name='competition-add'),
        path('edit/<int:pk>/', CompetitionUpdateView.as_view(), name='competition-edit'),
        path('delete/<int:pk>/', CompetitionDeleteView.as_view(), name='competition-delete'),
    ])),
]