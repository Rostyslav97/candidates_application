from datetime import datetime, timedelta

from django.http.response import JsonResponse
from rest_framework.generics import ListCreateAPIView

from .models import Candidate
from .serializers import CandidateSerializer, WorkExperienceSerializer
from .services import (commit_work_experience, get_formated_work_experience,
                       get_total_experience)


class CandidateListCreateAPI(ListCreateAPIView):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all().order_by("-total_experience")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        candidate = serializer.save()

        work_experience_request = request.data.get("workExperience", [])
        work_experience = [
            get_formated_work_experience(we) for we in work_experience_request
        ]

        commit_work_experience(work_experience, candidate.id)

        candidate.total_experience = get_total_experience(work_experience)
        candidate.save()

        return JsonResponse(data=serializer.data)
        