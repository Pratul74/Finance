from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Record
from .serializers import RecordSerializer
from users.permissions import IsAdmin, IsAnalystOrAdmin

class RecordViewSet(ModelViewSet):

    serializer_class = RecordSerializer
    queryset = Record.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsAnalystOrAdmin]
        else:
            permission_classes = [IsAuthenticated, IsAdmin]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user

        queryset = Record.objects.filter(user=user)

        record_type = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if record_type:
            queryset = queryset.filter(type=record_type)

        if category:
            queryset = queryset.filter(category__id=category)

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset
