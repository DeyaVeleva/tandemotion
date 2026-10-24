from django import forms
from django.utils import timezone

from coaching.models import Assignment, Message, Competition


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ['status','created_at']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'athletes': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'coach': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Title',
            'athletes': 'Athletes',
            'deadline': 'Deadline',
            'description': 'Description',
            'coach': 'Coach',
        }
        help_texts = {
            'deadline': 'Select the final date and time for athletes to complete their assignment.',
            'description': 'Provide a detailed overview of the assignment.',
        }
        error_messages = {
            'title': {
                'required':'Please, enter a title.',
            },
            'coach': {
                'required':'Please, select a coach.',
            },
            'deadline': {
                'required':'Please, select a deadline.',
            },
            'description': {
                'required':'Please, enter a description.',
            },
            'athletes': {
                'required':'Please, select at least one athlete.',
            },

        }
    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        if deadline and deadline <= timezone.now():
            raise forms.ValidationError('Please, choose a deadline in the future!')
        return deadline

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = [ 'created_at']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message'}),
            'athletes': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'coach': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Title',
            'message': 'Message',
            'athletes': 'Athletes',
            'coach': 'Coach',
        }
        help_texts = {
            'message': 'Write a message for the athletes.',
        }
        error_messages = {
            'title': {
                'required':'Please, enter a title.',
            },
            'message': {
                'required':'Please, type a message.',
            },
            'coach': {
                'required':'Please, select a coach.',
            },
            'athletes': {
                'required':'Please, select at least one athlete.',
            },
        }

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Competition's name"}),
            'sport': forms.TextInput(attrs={'placeholder': 'Sport'}),
            'category': forms.TextInput(attrs={'placeholder': 'Category'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'coaches': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'athletes': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
            'sport': 'Sport',
            'category': 'Category',
            'date': 'Date',
            'location': 'Location',
            'description': 'Description',
            'coaches': 'Coaches',
            'athletes': 'Athletes',
        }
        help_texts = {
            'category': 'Specify the age group, weight class, or skill division.',
            'description': 'Type any additional details about the competition.',
        }
        error_messages = {
            'name': {
                'required':'Please enter a title.',
            },
            'sport': {
                'required':'Please enter a sport.',
            },
            'category': {
                'required':'Please enter a competition category.',
            },
            'date': {
                'required':'Please select a competition date.',
            },
            'location': {
                'required':'Please enter a location.',
            },

        }
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date <= timezone.localdate():
            raise forms.ValidationError('Please choose a date in the future!')
        return date