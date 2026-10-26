from django.utils import timezone

from django import forms

from trainings.models import Training


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'finish': forms.TimeInput(attrs={'type': 'time'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'types': forms.TextInput(attrs={'placeholder': 'Type of Training'}),
            'coaches': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'athletes': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Title',
            'start': 'Start Time',
            'finish': 'Finish Time',
            'location': 'Location',
            'description': 'Description',
            'types': 'Type of Training',
            'coaches': 'Coaches',
            'athletes': 'Athletes',
        }
        help_texts = {
            'description': 'Provide a detailed overview of the training.',
        }
        error_messages = {
            'title': {
                'required': 'Please, enter a title.',
            },
            'start': {
                'required': 'Please, enter a start time.',
            },
            'finish': {
                'required': 'Please, enter a finish time.',
            },
            'types': {
                'required': 'Please, enter a type of training.',
            },
            'coaches': {
                'required': 'Please, select coaches.',
            },
            'athletes': {
                'required': 'Please, select athletes.',
            }
        }

    def clean_start(self):
        start = self.cleaned_data.get('start')
        if start and start<timezone.now():
            raise forms.ValidationError('Start time must be in the future!')
        return start

    def clean(self):
        cleaned_data = super().clean()
        start = self.cleaned_data.get('start')
        finish = self.cleaned_data.get('finish')
        if start and finish and start.time() >= finish:
            raise forms.ValidationError('The finish time must be later than the start time!')
        return cleaned_data

    def __str__(self):
        return f"{self.title} - {self.start} : {self.finish}"

