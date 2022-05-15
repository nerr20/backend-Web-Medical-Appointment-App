from .models import Announcement
from .serializers import AnnouncementModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import AnnouncementFilter


class AnnouncementModelViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementModelSerializer

    # # pagination
    # pagination_class = PageNumberPagination
    # pagination_class.page_size = 5

    # filter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = AnnouncementFilter
    search_fields = ['title', 'body']
    ordering_fields = ['created_time', 'modified_time']