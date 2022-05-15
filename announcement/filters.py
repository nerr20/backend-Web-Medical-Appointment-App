from django_filters import rest_framework as drf_filters
from .models import Announcement


class AnnouncementFilter(drf_filters.FilterSet):
    class Meta:
        model = Announcement
        fields = ['author', 'category']