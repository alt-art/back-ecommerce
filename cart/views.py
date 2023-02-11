from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializer import PostCartSerializer, CartSerializer
from rest_framework import status

class CartList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        carts = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request):
        post_serializer = PostCartSerializer(data=request.data)
        if not post_serializer.is_valid():
            return Response({
                'message': post_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        product = post_serializer.validated_data['product']
        quantity = post_serializer.validated_data['quantity']
        user = request.user
        cart = Cart.objects.filter(product=product, user=user)
        if cart.exists():
            cart = cart.first()
            cart.quantity += quantity
            cart.save()
            serializer = CartSerializer(cart)
            return Response(serializer.data)

        cart = Cart.objects.create(
            product=product,
            quantity=quantity,
            user=request.user
        )

        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def patch(self, request):
        post_serializer = PostCartSerializer(data=request.data)
        if not post_serializer.is_valid():
            return Response({
                'message': post_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        product = post_serializer.validated_data['product']
        quantity = post_serializer.validated_data['quantity']
        user = request.user
        cart = Cart.objects.filter(product=product, user=user)
        if not cart.exists():
            return Response({
                'message': 'Cart not found'
            })
        cart.quantity = quantity
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def delete(self, request):
        product = request.data.get('product')
        if not product:
            return Response({
                'message': 'Product is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        cart = Cart.objects.filter(product=product, user=user)
        if not cart.exists():
            return Response({
                'message': 'Cart item not found'
            }, status=status.HTTP_404_NOT_FOUND)
        cart.delete()
        return Response({
            'message': 'Cart deleted'
        })
