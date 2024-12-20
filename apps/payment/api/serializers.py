from rest_framework import serializers

from apps.orders.models import Shipping
from apps.payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields =[ "id","created_at","updated_at","status","amount","orders","id","user"]