from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=255)
    total_experience = models.SmallIntegerField(null=False, blank=False)


class WorkExperience(models.Model):
    start = models.DateField(null=False, blank=False)
    end = models.DateField(null=False, blank=False)

    candidate = models.ForeignKey("Candidate", models.CASCADE, null=False, blank=False)
