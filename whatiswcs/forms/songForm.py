from django import forms


class SongForm(forms.Form):
    title = forms.CharField(max_length=200, label='Title')
    artist = forms.CharField(max_length=200, label='Artist')
    features = forms.CharField(
        max_length=2048,
        widget=forms.Textarea(attrs={
            'placeholder': 'In your own words, what about this song makes it so danceable?'
        }),
        label='Features',
        required=False
    )

    def clean(self):
        cleaned_data = super(SongForm, self).clean()
        title = cleaned_data.get('title')
        artist = cleaned_data.get('artist')
        features = cleaned_data.get('features')
        if not title:
            raise forms.ValidationError("Title is a very important, and very required field. :)")
        if not artist:
            raise forms.ValidationError("Artist? We don't need no stinkin' artist! "
                                        "But really, we kinda do; it's a required field.")

