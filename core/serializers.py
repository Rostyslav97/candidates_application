from rest_framework import serializers

from core.models import Candidate, WorkExperience


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ["start", "end", "candidate"]


class CandidateSerializer(serializers.ModelSerializer):
    work_experience = serializers.SerializerMethodField()

    class Meta:
        model = Candidate
        fields = ("name", "total_experience", "work_experience")
        read_only_fields = ("total_experience",)

    def get_work_experience(self, obj):
        qs = WorkExperience.objects.filter(candidate=obj)
        return WorkExperienceSerializer(qs, many=True).data