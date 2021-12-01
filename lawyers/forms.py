from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import LawyerSpecilization, Lawyers

class LawyerForm(ModelForm):
    class Meta:
        model = Lawyers
        fields = '__all__'

class SpecializationForm(ModelForm):
    class Meta:
        model = LawyerSpecilization
        fields ='__all__'