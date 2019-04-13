from __future__ import unicode_literals

from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response

class RestaurantViewSet(viewsets.ModelViewSet):

    serializer_class = RestaurantSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user', None)
        if user_id is not None:
            queryset = Restaurant.objects.all()
            queryset = queryset.filter(user=user_id)
            return queryset

        name = self.request.query_params.get('name', None)
        address = self.request.query_params.get('address', None)
        city = self.request.query_params.get('city', None)
        popular = self.request.query_params.get('popular', False)
        if popular:
            queryset = Restaurant.objects.order_by('-rating','-ratings_count')
        else:
            queryset = Restaurant.objects.all()

        if name is not None:
            queryset = queryset.filter(name=name)
        if address is not None:
            queryset = queryset.filter(address=address)
        if city is not None:
            queryset = queryset.filter(city=city)
        return queryset


class RestaurantCatViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantCatSerializer
    queryset = RestaurantCat.objects.all()

    def retrieve(self, request, pk=None):
        cat_l = RestaurantCat.objects.filter(restaurant=pk)
        l = []
        for c in cat_l:
            l += [c.title]
        return Response({"restaurant":pk, "categories":l}, status=status.HTTP_200_OK)

    def get_queryset(self):
        cat = self.request.query_params.get('catogory', None)
        queryset = RestaurantCat.objects.all()
        if cat is not None:
            queryset = queryset.filter(title=cat)
        return queryset
