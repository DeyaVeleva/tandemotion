from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from coaching.forms import CompetitionForm, MessageForm
from coaching.models import Competition, Message


class CompetitionListView(ListView):
    model = Competition
    template_name = 'coaching/competition_list.html'
    context_object_name = 'competitions'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Competitions'
        context['page_description'] = 'Competition list.'
        return context

class CompetitionDetailView(DetailView):
    model = Competition
    template_name = 'coaching/competition_details.html'
    context_object_name = 'competition'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class CompetitionCreateView(CreateView):
    model = Competition
    form_class = CompetitionForm
    template_name = 'coaching/competition_form.html'
    success_url = reverse_lazy('competition-list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CompetitionUpdateView(UpdateView):
    model = Competition
    form_class = CompetitionForm
    template_name = 'coaching/competition_form.html'
    def get_success_url(self):
        return reverse_lazy('competition-detail', kwargs={'pk': self.object.pk})

class CompetitionDeleteView(DeleteView):
    model = Competition
    template_name = 'shared/confirm_delete.html'
    success_url = reverse_lazy('competition-list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url_name'] = 'competition-detail'
        return context

class MessageListView(ListView):
    model = Message
    template_name = 'coaching/message_list.html'
    context_object_name = 'messages'
    ordering = '-pk'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Messages'
        context['page_description'] = 'Messages from coaches.'
        return context

class MessageDetailView(DetailView):
    model = Message
    template_name = 'coaching/message_details.html'
    context_object_name = 'message'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'coaching/message_form.html'
    def get_success_url(self):
        return reverse ('message-detail', kwargs={'pk': self.object.pk})

class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'coaching/message_form.html'
    def get_success_url(self):
        return reverse_lazy('message-detail', kwargs={'pk': self.object.pk})

class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'shared/confirm_delete.html'
    success_url = reverse_lazy('message-list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url_name'] = 'competition-detail'
        return context


