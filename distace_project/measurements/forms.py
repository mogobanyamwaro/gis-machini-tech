from django import forms
from .models import Measurement


class MeasurementModelForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ('destination', 'description',
                  'station', 'operation', 'serviceNumber', 'codeName')
