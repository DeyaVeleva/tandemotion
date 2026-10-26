from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from trainings.forms import TrainingForm
from trainings.models import Training


class TrainingListView(ListView):
    model = Training
    template_name = 'trainings/training_list.html'
    context_object_name = 'trainings'
    def get_context_data(self, **kwargs):
        context = super(TrainingListView, self).get_context_data(**kwargs)
        context[ 'page_title'] = 'Trainings'
        context['page_description'] = 'Training list.'
        return context

class TrainingDetailView(DetailView):
    model = Training
    template_name = 'trainings/training_details.html'
    context_object_name = 'training'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TrainingCreateView(CreateView):
    model = Training
    form_class = TrainingForm
    template_name = 'trainings/training_form.html'
    success_url = reverse_lazy('training-list')

class TrainingUpdateView(UpdateView):
    model = Training
    form_class = TrainingForm
    template_name = 'trainings/training_form.html'
    def get_success_url(self):
        return reverse_lazy('training-detail', kwargs={'pk': self.object.pk})

class TrainingDeleteView(DeleteView):
    model = Training
    template_name = 'shared/confirm_delete.html'
    success_url = reverse_lazy('training-list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url_name'] = 'training-detail'
        return context