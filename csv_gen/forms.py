from django import forms
from .models import NewSchema


class NewSchemaForm(forms.ModelForm):
    class Meta:
        model = NewSchema
        fields = ['column_name', 'type', '_from', 'to', 'order']
        widgets = {
            'column_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control', 'id': 'sel'}),
            '_from': forms.NumberInput(attrs={'class': 'form-control t_width_low', 'id': 'id_from'}),
            'to': forms.NumberInput(attrs={'class': 'form-control t_width_low', 'id': 'id_to'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),

        }

