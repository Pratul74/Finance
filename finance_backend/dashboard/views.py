from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from records.models import Record
from users.permissions import IsAnalystOrAdmin

class DashboardView(APIView):

    permission_classes=[IsAuthenticated, IsAnalystOrAdmin]

    def get(self, request):
        user=request.user

        records=Record.objects.filter(user=user)

        total_income=records.filter(type="income").aggregate(
            total=Sum('amount')
        )['total'] or 0

        total_expense=records.filter(type='expense').aggregate(
            total=Sum('amount')
        )['total'] or 0

        net_balance=total_income-total_expense

        return Response({
            'total_income': total_income,
            "total_expense": total_expense,
            'net_balance': net_balance
        })
    
class CategoryWiseView(APIView):
    permission_classes=[IsAuthenticated, IsAnalystOrAdmin]

    def get(self, request):
        user=request.user

        data=(
            Record.objects
            .filter(user=user)
            .values(category='category_title')
            .annotate(total=Sum('amount'))
        )

        return Response(data)
    
class RecentRecordsView(APIView):

    permission_classes = [IsAuthenticated, IsAnalystOrAdmin]

    def get(self, request):
        user = request.user

        records = (
            Record.objects
            .filter(user=user)
            .order_by('-date')[:5]
        )

        from records.serializers import RecordSerializer
        serializer = RecordSerializer(records, many=True)

        return Response(serializer.data)

    

    







