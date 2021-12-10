from django.urls import path

from .views import CandidateListCreateAPI

app_name = "core"

urlpatterns = [
    path("candidates/", CandidateListCreateAPI.as_view(), name="candidates_list_create"),
]
