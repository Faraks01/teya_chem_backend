from rest_framework import serializers

from feedback_form.models import FeedbackForm


class FeedbackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackForm
        fields = '__all__'
