from django import forms
from django.forms import ModelForm, Textarea
from ..models import SongAndDancer
from django_countries.fields import CountryField


class SongAndDancerForm(ModelForm):
    class Meta:
        model = SongAndDancer
        fields = '__all__'
        age = forms.IntegerField(min_value=6)
        region = CountryField(default={'country': 'US'})
        widgets = {
            'features': Textarea(attrs={
                'placeholder': 'In your own words, what about this song makes it so danceable?',
                'rows': 3
            })
        }
        labels = {
            'primary_dance_role': 'What is your usual role as a dancer? ',
            'competitive_level': 'What is your competitive level? ',
            'years_dancing': 'How long have you been dancing? ',
            'age': 'How old are you? ',
            'dj': 'Do you DJ WCS events (of any size)? ',
            'teacher': 'Do you teach WCS? ',
            'region': 'Where are you from? ',
            'other_dance_styles': 'What other dances do you do? '
        }
