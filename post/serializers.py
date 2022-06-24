from rest_framework import serializers
from .models import JobPost as JobPostModel


class JobPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobPostModel
        fields = "__all__"