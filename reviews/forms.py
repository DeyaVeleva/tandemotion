from django import forms

from reviews.models import AthleteReflection, CoachFeedback


class AthleteReflectionForm(forms.ModelForm):
    class Meta:
        model = AthleteReflection
        exclude = ['created_at', 'updated_at', 'training', 'competition'] # when you click on it you can write reflection about it so you shouldnt choose which training or competition your writing about
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'rating':forms.NumberInput(attrs={ 'placeholder': 'Rating'}),
            'main_goals': forms.Textarea(attrs={'placeholder': 'Main Goals'}),
            'reflection': forms.Textarea(attrs={'placeholder': 'Reflection'}),
            'author': forms.Select(attrs={'placeholder': 'Athlete'}),
        }
        labels = {
            'title': 'Title',
            'rating': 'Rating',
            'main_goals': 'Main Goals',
            'reflection': 'Reflection',
            'author': 'Athlete',
        }
        help_texts = {
            'rating': 'Rate your experience from 1 to 10.',
            'main_goals': 'Type what your main goals were.',
            'reflection': 'Analyze your thoughts, emotions and mechanics.',
        }
        error_messages = {
            'title': {
                'required': 'Please, enter a title.',
            },
            'rating': {
                'required': 'Please, enter a rating.',
            },
            'main_goals': {
                'required': 'Please, enter your main goals.',
            },
            'reflection': {
                'required': 'Please, enter your reflection.',
            },
            'author': {
                'required': 'Please, select an athlete.',
            }

        }

class CoachFeedbackForm(forms.ModelForm):
    class Meta:
        model = CoachFeedback
        exclude = ['created_at', 'updated_at', 'training', 'competition', 'to_athlete'] #click on the athletes reflection
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'feedback': forms.Textarea(attrs={'placeholder': 'Feedback'}),
            'author': forms.Select(attrs={'placeholder': 'Coach'}),
        }
        labels = {
            'title': 'Title',
            'feedback': 'Feedback',
            'author': 'Coach',
        }
        help_texts = {
            'feedback': 'Type what your feedback is.',
        }
        error_messages = {
            'title': {
                'required': 'Please, enter a title.',
            },
            'feedback': {
                'required': 'Please, enter a feedback.',
            },
            'author': {
                'required': 'Please, select a coach.',
            }
        }
