from django import forms
from django_countries.fields import CountryField
from ..models.dancer import (
    PRIMARY_DANCE_ROLE_CHOICES,
    COMP_LEVEL_CHOICES,
    YEARS_DANCING_CHOICES,
    OTHER_DANCES
)


class DancerForm(forms.Form):
    primary_dance_role = forms.ChoiceField(
        choices=PRIMARY_DANCE_ROLE_CHOICES,
        label='Primary Dance Role',
        required=False
    )
    competitive_level = forms.ChoiceField(
        choices=COMP_LEVEL_CHOICES,
        label='Competitive Dance Level',
        required=False
    )
    years_dancing = forms.ChoiceField(
        choices=YEARS_DANCING_CHOICES,
        label='Years',
        required=False
    )
    age = forms.IntegerField(min_value=6, label='Age', required=False)
    dj = forms.BooleanField(label='DJ', required=False)
    teacher = forms.BooleanField(label='Teacher', required=False)
    other_dances = forms.BooleanField(label='Other Dances', required=False)
    other_dance_styles = forms.MultipleChoiceField(
        choices=OTHER_DANCES, label='Other Dance Styles', required=False
    )
    countries = CountryField()
    region = forms.ChoiceField(choices=countries.choices,
                               label='Region', required=False)
    def clean(self):
        cleaned_data = super(DancerForm, self).clean()
        primary_dance_role = cleaned_data.get('primary_dance_role')
