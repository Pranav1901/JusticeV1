from rest_framework import fields, serializers
from .models import LawyerSpecilization, Lawyers


class allSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Lawyers
        fields='__all__'
class allSpecilizationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = LawyerSpecilization
        fields='__all__'
        depth = 1

class allSerailizerread(serializers.ModelSerializer):
    class Meta:
        model = LawyerSpecilization
        fields=['Lawyer']
        depth =1