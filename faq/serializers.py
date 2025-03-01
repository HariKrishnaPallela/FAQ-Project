from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['question', 'answer']

    def get_question(self, obj):
        lang = self.context['request'].query_params.get('lang', 'en')
        return obj.get_translated(lang)['question']

    def get_answer(self, obj):
        lang = self.context['request'].query_params.get('lang', 'en')
        return obj.get_translated(lang)['answer']