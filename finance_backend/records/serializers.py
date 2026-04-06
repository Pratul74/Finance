from rest_framework import serializers
from .models import Record, Category

class RecordSerializer(serializers.ModelSerializer):

    user=serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive")
        return value

    class Meta:
        model = Record
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ['id', 'title', 'user']