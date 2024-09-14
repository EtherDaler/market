from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance or instance is None:
            return Response({'message': 'Не найдено товара в базе данных'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def create(self, request, *args, **kwargs):
        if 'name' not in request.data.keys():
            return Response({'message': 'Отсутствует поле name!'}, status=status.HTTP_400_BAD_REQUEST)
        if 'description' not in request.data.keys():
            return Response({'message': 'Отсутствует поле description!'}, status=status.HTTP_400_BAD_REQUEST)
        if 'price' not in request.data.keys():
            return Response({'message': 'Отсутствует поле price!'}, status=status.HTTP_400_BAD_REQUEST)

        name = request.data['name']
        description = request.data['description']
        price = float(request.data['price'])

        # Тут мы проверим не состоят ли наши название и описание только из числа или чисел через пробел
        check_name = list(map(lambda x: int(x.isdigit()), name.split()))
        check_description = list(map(lambda x: int(x.isdigit()), description.split()))
        if sum(check_name) == len(name.split()) or sum(check_description) == len(description.split()):
            return Response({'message': 'Название или описание не может быть цифрой!'},
                            status=status.HTTP_400_BAD_REQUEST)

        if price < 0:
            return Response({'message': 'Цена не может быть отрицательной!'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def main(request):
    return render(request, template_name='./main.html', context={})
