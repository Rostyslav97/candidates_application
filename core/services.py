from datetime import datetime, timedelta
from functools import total_ordering

from .serializers import WorkExperienceSerializer


def get_formated_work_experience(work_experience: dict) -> dict:
    """Get the data in format `Jul 2018` and return Python date object"""
    return {k: datetime.strptime(v, "%b %Y").date() for k, v in work_experience.items()}


def commit_work_experience(work_experience: dict, candidate_id: int) -> None:
    for we in work_experience:
        work_experience_serializer = WorkExperienceSerializer(
            data=we | {"candidate": candidate_id}
        )
        work_experience_serializer.is_valid(raise_exception=True)
        work_experience_serializer.save()


def get_total_experience(work_experience: dict) -> int:
    total_exp = timedelta(days=0)
    for we in work_experience:
        total_exp += we["end"] - we["start"]

    return total_exp.days // 365
