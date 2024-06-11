# forms.py

from django import forms
from .models import URL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'placeholder': 'Enter the URL to shorten',
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super(URLForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Shorten', css_class='btn btn-primary btn-block'))
