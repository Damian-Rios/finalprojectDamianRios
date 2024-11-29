from django import forms

class SetFilterForm(forms.Form):
    series = forms.MultipleChoiceField(
        choices=[('XY', 'XY'), ('Sun & Moon', 'Sun & Moon'), ('Sword & Shield', 'Sword & Shield')],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    set_id = forms.CharField(required=False)
    name = forms.CharField(required=False)
