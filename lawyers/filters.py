from django.db.models import fields
import django_filters
from .models import *


class IdFilter(django_filters.FilterSet):
    class Meta:
        model = LawyerSpecilization
        fields = 'Lawyer.id'