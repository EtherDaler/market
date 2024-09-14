from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        pre_represented_data = super().to_representation(instance)
        return pre_represented_data

    def create(self, validated_data):
        try:
            data = {
                'name': validated_data['name'],
                'description': validated_data['description'],
                'price': validated_data['price']
            }
        except:
            raise KeyError("Отправлены не все данные. Проверьте названия параметров!")
        instance = Product.objects.create(**data)
        return instance