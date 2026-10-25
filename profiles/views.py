from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from profiles.forms import AthleteProfileForm, CoachProfileForm
from profiles.models import AthleteProfile, CoachProfile


def home_page_view(request):

    return render(request, 'home-page/home.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

class AthleteProfileDetailView(DetailView):
    model = AthleteProfile
    template_name = 'profiles/profile_details.html'
    context_object_name = 'profile'
    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_url_name'] = 'athlete-edit'
        context['delete_url_name'] = 'athlete-delete'
        return context

class AthleteProfileListView(ListView):
    model = AthleteProfile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profiles'
    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Our Athletes'
        context['page_description'] = 'Meet our athletes.'
        context['detail_url_name'] = 'athlete-details'
        context['create_url_name'] = 'athlete-add'
        context['create_button_label'] = 'Add Athlete'

        return context

class AthleteProfileCreateView(CreateView):
    model = AthleteProfile
    form_class = AthleteProfileForm
    template_name = 'profiles/profile_form.html'
    success_url = reverse_lazy('athletes-list')

class AthleteProfileUpdateView(UpdateView):
    model = AthleteProfile
    form_class = AthleteProfileForm
    template_name = 'profiles/profile_form.html'
    def get_success_url(self):
        return reverse_lazy('athletes-details', kwargs={'pk': self.object.pk})

class AthleteProfileDeleteView(DeleteView):
    model = AthleteProfile
    template_name = 'shared/confirm_delete.html'
    success_url = reverse_lazy('athletes-list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url_name'] = 'athlete-details'
        return context


class CoachProfileListView(ListView):
    model = CoachProfile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profiles'

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Our Coaches'
        context['page_description'] = 'Meet our coaches.'
        context['detail_url_name'] = 'coach-details'
        context['create_url_name'] = 'coach-add'
        context['create_button_label'] = 'Add Coach'
        return context

class CoachProfileDetailView(DetailView):
    model = CoachProfile
    template_name = 'profiles/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_url_name'] = 'coach-edit'
        context['delete_url_name'] = 'coach-delete'
        return context

class CoachProfileCreateView(CreateView):
    model = CoachProfile
    form_class = CoachProfileForm
    template_name = 'profiles/profile_form.html'
    success_url = reverse_lazy('coaches-list')

class CoachProfileUpdateView(UpdateView):
    model = CoachProfile
    form_class = CoachProfileForm
    template_name = 'profiles/profile_form.html'
    def get_success_url(self):
        return reverse_lazy('coaches-details', kwargs={'pk': self.object.pk})

class CoachProfileDeleteView(DeleteView):
    model = CoachProfile
    template_name = 'shared/confirm_delete.html'
    success_url = reverse_lazy('coaches-list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url_name'] = 'coach-details'
        return context
