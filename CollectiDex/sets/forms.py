from django import forms

class SetFilterForm(forms.Form):
    SERIES_CHOICES = [
        ('scarlet & violet', 'Scarlet & Violet'),
        ('sword & shield', 'Sword & Shield'),
        ('sun & moon', 'Sun & Moon'),
        ('xy', 'XY'),
        ('black & white', 'Black & White'),
        ('heartgold & soulsilver', 'HeartGold & SoulSilver'),
        ('platinum', 'Platinum'),
        ('diamond & pearl', 'Diamond & Pearl'),
        ('ex', 'EX'),
        ('base', 'Base'),
        ('other_series', 'Other'),
    ]
    series = forms.MultipleChoiceField(
        choices=SERIES_CHOICES,
        required=False,
        label='Series',
        widget=forms.CheckboxSelectMultiple
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'list': 'dataListOptions',
                   'placeholder': 'Search for a set',
                   }),
        label="Name",
        max_length=100,
        required=False)
