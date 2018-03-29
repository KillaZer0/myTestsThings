from shop.models import Contact, ProductCategory
from rest_framework import serializers


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'email')


class ProducrCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'root_id')