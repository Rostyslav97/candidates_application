from django.contrib import admin

from .models import Candidate, WorkExperience


class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    inlines = [WorkExperienceInline]
