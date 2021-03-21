from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Element, Category, Type
from .serializer import ElementSerializer, CategorySerializer, TypeSerializer
 
class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    @action(detail=True, methods=['get'])
    def categories(self, request, pk=None):
        queryset = Category.objects.filter(id=pk)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    '''def list(self, request):
        queryset = Category.Objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)'''

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    @action(detail=True, methods=['get'])
    def tipos(self, request, pk=None):
        queryset = Type.objects.filter(id=pk)
        serializer = TypeSerializer(queryset, many=True)
        return Response(serializer.data)