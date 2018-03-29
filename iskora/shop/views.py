from shop.models import Contact, ProductCategory
from rest_framework import viewsets
from shop.serializers import ContactSerializer, ProducrCategorySerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProducrCategorySerializer