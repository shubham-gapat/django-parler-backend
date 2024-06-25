from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers
from .models import Product


class CreateProductSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product)

    class Meta:
        model = Product
        fields = ("translations", "price")


class GetProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("name", "description", "price")
