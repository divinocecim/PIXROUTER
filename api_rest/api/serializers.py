from rest_framework import serializers

from api_rest.models import Enviapix, Chavespix


class EnviapixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enviapix
        fields = '__all__'

class ChavepixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chavespix
        fields = '__all__'
        
