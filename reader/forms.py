from django import forms
from .validator import validate_file_extension


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select csv file',
        validators=[validate_file_extension]
    )