from .models import Announcement
from .serializers import AnnouncementModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import AnnouncementFilter

from rest_framework import status
from rest_framework.response import Response
from collections import OrderedDict

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
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        ret = OrderedDict(dict(id=response.data.pop('id')))
        return Response(ret, status=response.status_code, headers=response.headers)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        ret = response.data.copy()
        ret.pop('id')
        return Response(ret)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)
