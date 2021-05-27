from django.shortcuts import render
from .models import Code
from .serializers import CodeSerializer

from rest_framework.viewsets import ModelViewSet


class CodeView(ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer


    """def create(self, request, *args, **kwargs):
        user = request.user.profile  #профаил это рилэйтед нэйм user в профайле))) вытаскиваем нашего юзера
        address_from_data = request.data.get('address')
        order_products = request.data.get('order_products')

        order_created = Order.objects.create(client=user, address=address_from_data)

        total_sum = 0

        for product in order_products:
            price = Product.objects.get(id=product.get('product_id')).price
            total_sum += price * product.get('count')

            OrderProducts.objects.create(
                order=order_created,
                product_id=product.get('product_id'),
                count=product.get('count')
            )

        order_created.total_price = total_sum
        order_created.save()

        return Response('Success')"""