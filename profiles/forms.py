from django import forms
from django.utils import timezone

from profiles.models import AthleteProfile, CoachProfile


class AthleteProfileForm(forms.ModelForm):
    class Meta:
        model = AthleteProfile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Athlete's first name"}),
            'last_name': forms.TextInput(attrs={'placeholder': "Athlete's last name"}),
            'profile_pic': forms.FileInput(attrs={'placeholder': "Upload a profile picture"}),
            'email': forms.EmailInput(attrs={'placeholder': "Email address"}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'sport': forms.TextInput(attrs={'placeholder': "Primary sport"}),
            'main_competition_category': forms.TextInput(attrs={'placeholder': "Main competition category"}),
            'other_competition_categories': forms.TextInput(attrs={'placeholder': "Other competition categories"}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_pic': 'Profile Picture',
            'email': 'Email Address',
            'date_of_birth': 'Date of Birth',
            'sport': 'Sport',
            'main_competition_category': 'Main Competition Category',
            'other_competition_categories': 'Other Competition Categories',
        }
        help_texts = {
            'main_competition_category': 'Type the primary category you will be competing in, based on parameters like age, skill level, or weight class.',
            'other_competition_categories': 'Type any additional age groups, skill levels, or open divisions you wish to enter alongside your main event.'
        }
        error_messages = {
            'first_name': {
                'required':'Please, enter your first name.',
            },
            'last_name': {
                'required':'Please, enter your last name.',
            },
            'email': {
                'invalid':'Please, enter a valid email address.',
                'required': 'Please, enter an email address.',
            },
            'date_of_birth': {
                'required':'Please, enter date of birth.',
            },
            'sport': {
                'required':'Please, enter a sport.',
            },
        }

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth and date_of_birth >= timezone.localdate():
            raise forms.ValidationError('Date of birth must be in the past!')
        return date_of_birth

    def clean(self):
        cleaned_data = super(AthleteProfileForm, self).clean()

        if cleaned_data.get('first_name') and cleaned_data.get('last_name') and cleaned_data.get('first_name') == cleaned_data.get('last_name') :
            raise forms.ValidationError('Please, enter valid names.')
        return cleaned_data

class CoachProfileForm(forms.ModelForm):
    class Meta:
        model = CoachProfile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Coach's first name"}),
            'last_name': forms.TextInput(attrs={'placeholder': "Coach's last name"}),
            'email': forms.EmailInput(attrs={'placeholder': "Email address"}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'sport': forms.TextInput(attrs={'placeholder': "Primary sport"}),
            'specialty': forms.Select(attrs={'placeholder': "Specialty"}),
            'athletes': forms.CheckboxSelectMultiple(attrs={'placeholder': "Athletes"}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_pic': 'Profile Picture',
            'email': 'Email Address',
            'date_of_birth': 'Date of Birth',
            'sport': 'Sport',
            'specialty': 'Specialty',
            'athletes': 'Athletes',
        }
        help_texts = {
            'profile_pic': 'Upload a profile picture (optional).',
            'specialty': 'Select your primary areas of expertise.',#make a specialty model :(
            'athletes' : 'Select the athletes you are working with.',
        }
        error_messages = {
            'first_name': {
                'required': 'Please, enter your first name.',
            },
            'last_name': {
                'required': 'Please, enter your last name.',
            },
            'email': {
                'invalid': 'Please, enter a valid email address.',
                'required': 'Please, enter an email address.',
                'unique': 'This email address is already in use.',
            },
            'date_of_birth': {
                'required': 'Please, enter date of birth.',
            },
            'sport': {
                'required': 'Please, enter a sport.',
            },
            'specialty': {
                'required': 'Please, enter your primary areas of expertise.',
            }
        }

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            today = timezone.now()
            age = today.year - date_of_birth.year
            if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
                age-=1
            if age<18:
                raise forms.ValidationError('Coaches must be at least 18 years old!')
        return date_of_birth

    def clean(self):
        cleaned_data = super(CoachProfileForm, self).clean()
        if cleaned_data.get('first_name') and cleaned_data.get('last_name') and cleaned_data.get('first_name') == cleaned_data.get('last_name'):
            raise forms.ValidationError('Please, enter valid names.')
        return cleaned_data
