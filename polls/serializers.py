from django.contrib.auth.models import User
from rest_framework import serializers
from polls.models import Choice


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('id',  'question_text', 'question_desc', 'pub_date')
