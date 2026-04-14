from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from .utils import classify_transaction, classify_want_need


@api_view(['POST'])
def add_transaction(request):
    data = request.data

    description = data.get('description')
    amount = float(data.get('amount'))

    # ML classification
    category = classify_transaction(description)

    # Logic layer
    tag = classify_want_need(category, amount)

    # Save to DB
    transaction = Transaction.objects.create(
        amount=amount,
        description=description,
        category=category,
        tag=tag
    )

    return Response(TransactionSerializer(transaction).data)

@api_view(['GET'])
def get_transactions(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def summary(request):
    transactions = Transaction.objects.all()

    summary_data = {}

    for t in transactions:
        summary_data[t.category] = summary_data.get(t.category, 0) + t.amount

    return Response(summary_data)

@api_view(['DELETE'])
def clear_transactions(request):
    Transaction.objects.all().delete()
    return Response({"message": "All transactions deleted"})