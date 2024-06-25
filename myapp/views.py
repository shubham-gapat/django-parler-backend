from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response
from .models import Product
from .serializers import (
    CreateProductSerializer, GetProductSerializer
)
from .utils import (convert_data, ResponseInfo)


class CreateProductView(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = CreateProductSerializer

    def __init__(self, **kwargs):
        """
        Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(CreateProductView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        translated_data = {
            "name": request.data['name'],
            "description": request.data['description']
        }
        formatted_data = {
            "translations": convert_data(translated_data),
            "price": request.data['price']
        }
        print(formatted_data)
        product_serializer = self.get_serializer(data=formatted_data)
        if product_serializer.is_valid(raise_exception=True):
            product_serializer.save()
            self.response_format["status_code"] = status.HTTP_201_CREATED
            self.response_format["data"] = product_serializer.data
            self.response_format["message"] = ["Product created successfully."]

        return Response(self.response_format, status=self.response_format["status_code"])


class GetProductListView(ListAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = GetProductSerializer

    def __init__(self, **kwargs):
        """
        Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(GetProductListView, self).__init__(**kwargs)

    def get_queryset(self):
        lang_code = self.request.query_params.get("language")
        queryset = Product.objects.language(lang_code).all()
        return queryset

    def get(self, request, *args, **kwargs):
        serializer = super().list(request, *args, **kwargs)
        self.response_format["data"] = serializer.data
        return Response(self.response_format, status=self.response_format["status_code"])


class deleteAllProductView(DestroyAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = GetProductSerializer

    def __init__(self, **kwargs):
        """
        Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(deleteAllProductView, self).__init__(**kwargs)

    def delete(self, request, *args, **kwargs):
        Product.objects.all().delete()
        return Response(self.response_format, status=self.response_format["status_code"])