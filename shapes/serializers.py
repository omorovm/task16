from rest_framework import serializers
from .models import Triangle

class TriangleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triangle
        fields = '__all__'
    
    def validate_triangle(self, sides):
        if (sides[1]+sides[0]<=sides[3]) or (sides[2]+sides[0]<=sides[1]) or (sides[1]+sides[3]<=sides[2]):
            return serializers.ValidationError('Такого треугольника не существует') 
        return sides
    
    def validate(self, attrs):
        self.validate_triangle(attrs)
        return super().validate(attrs)