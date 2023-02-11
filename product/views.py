from .models import Product
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductList(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        products = Product.objects.values()
        return Response(list(products))
