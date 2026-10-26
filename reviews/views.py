from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from reviews.forms import AthleteReflectionForm
from reviews.models import AthleteReflection
from trainings.models import Training


class AthleteReflectionListView(ListView):
    model = AthleteReflection
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        self.training = get_object_or_404(Training, pk=self.kwargs['training_pk'])
        return AthleteReflection.objects.filter(training=self.training)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Athlete reflection'
        context['page_description'] = 'A dedicated space to process training sessions and games. Use this page to track what went well, learn from mistakes, and set a clear focus for your next workout.'
        context['training'] = self.training
        return context

class AthleteReflectionDetailView(DetailView):
    model = AthleteReflection
    template_name = 'reviews/review_details.html'
    context_object_name = 'review'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AthleteReflectionCreateView(CreateView):
    model = AthleteReflection
    form_class = AthleteReflectionForm
    template_name = 'reviews/review_form.html'
    def dispatch(self, request, *args, **kwargs):
        self.training = get_object_or_404(Training, pk=kwargs['training_pk'])
        return super().dispatch(request, *args, **kwargs)
    def get_form(self, form_class=None):
        form= super().get_form(form_class)
        form.instance.training = self.training
        return form

    def form_valid(self, form):
        form.instance.training = self.training
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('reflection-list', kwargs={'training_pk': self.training.pk})

class AthleteReflectionUpdateView(UpdateView):
    model = AthleteReflection
    form_class = AthleteReflectionForm
    template_name = 'reviews/review_form.html'

    def get_success_url(self):
        return reverse_lazy('reflection-detail', kwargs={'pk': self.object.pk})

class AthleteReflectionDeleteView(DeleteView):
    model = AthleteReflection
    template_name = 'shared/confirm_delete.html'
    def get_success_url(self):
        return reverse('reflection-list', kwargs={'training_pk': self.object.training.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url_name'] = 'reflection-detail'
        return context
