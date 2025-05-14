from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    test_questions = QuestionSerializer(many=True, source='questions')
    category = CategorySerializer()

    class Meta:
        model = Test
        fields = ['title', 'category', 'description', 'image', 'created_at', 'id', 'test_questions']


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
