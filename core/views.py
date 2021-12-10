from rest_framework.generics import ListCreateAPIView

from .models import Candidate  
from .serializers import CandidateSerializer

class CandidateListCreateAPI(ListCreateAPIView):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()

    def create(self, request, *args, **kwargs):
        breakpoint()