from django import forms

from reviews.models import AthleteReflection


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

